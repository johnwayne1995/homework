#encoding:utf-8

class PyLuaTblParser:
    def __init__(self):
        self.special_signal=['\\t','\\n','\\\\','\\\'','\\\"','\\a','\\b','\\f','\\r','\\v']
        self.special_signal_dict = {'\\t': '\t', '\\n': '\n', '\\\\': '\\', '\\\'':'\'','\\\"':'\"','\\a': '\a',
                               '\\b': '\b', '\\f': '\f', '\\r': '\r', '\\v': '\v'}

        self.string_loc=list()#字符串的位置下标
        # self.DeepLayer=list()#记录每个下标所在层深度的list
        self.raw = ''#初始输入
        self.norm_Table='' #去空格标准化后的table
        self.Dict=dict()#python格式字典
        self.strinput=''

    def is_int(self,input):
        try:
            _test=int(input)
            return True
        except:
            return False
        contain_list=['0','1','2','3','4','5','6','7','8','9','-','+']
        for s in input:
            if(s not in contain_list):

                    return False
        return True
    def science(self,input):
        if (input[-1] == '.'):
            return 'int'
        input=input.lower()
        if('e+' in input):
            return 'int'
        if('e-' in input):
            return 'float'

    def is_float(self,input):
        input=input.lower()
        if(self.is_int(input)):#排除整形
            return False
        contain_list=['.','0','1','2','3','4','5','6','7','8','9','-','+']
        for s in input:
            if(s not in contain_list):
                if('e+' in input or 'e-' in input):
                    continue
                else:
                    return False

        return True

    def is_bool(self, input):
        if (input=='false' or input=='true'):
            return True
        else:
            return False

    def is_string(self, input):
        if ((input[0]=='"' and input[-1]=='"') or (input[0]=="'" and input[-1]=="'")):
            return True
        else:
            return False

    def is_type(self,input):
        '''
        判断数据类型
        :return:
        '''
        if(self.is_int(input)):
            return 'int'
        elif(self.is_float(input)):
            return 'float'
        elif(self.is_bool(input)):
            return 'bool'
        else:
            return 'str'


    def contain_equal(self,input):
        stack_bracket = list()  # 记录匹配括号用的栈
        stack_quotation_single = list()
        stack_quotation_double = list()
        index=0

        while index<len(input):
            s=input[index]
            # print(s == '=')

            # print len(stack_bracket)
            if (input[index:index+2] in self.special_signal_dict):
                index+=1
            else:

                if(s=='=' and len(stack_quotation_single) == 0 and len(stack_quotation_double) == 0 and len(stack_bracket) == 0):
                    return index
                if(s==',' and len(stack_quotation_single) == 0 and len(stack_quotation_double) == 0 and len(stack_bracket) == 1):
                    return 'No_contain'
                #还有一种情况是字符串，占位，遇到再写
                if (s == '\'' and len(stack_quotation_double) == 0):
                    if (len(stack_quotation_single) == 0):
                        stack_quotation_single.append('into_str')
                    else:
                        stack_quotation_single.pop()
                if (s == '\"' and len(stack_quotation_single) == 0):
                    if (len(stack_quotation_double) == 0):
                        stack_quotation_double.append('into_str')
                    else:
                        stack_quotation_double.pop()
                if (s == "{" and len(stack_quotation_single) == 0 and len(stack_quotation_double) == 0):
                    stack_bracket.append('into_layer')
                if (s == "}" and len(stack_quotation_single) == 0 and len(stack_quotation_double) == 0):
                    stack_bracket.pop()
            index+=1
        # print len(stack_quotation_single),len(stack_quotation_double) ,len(stack_bracket)
        return 'No_contain'

    def include_equal(self,input):
        '''

        :param str:
        :return:
        '''
        stack_bracket = list()  # 记录匹配括号用的栈
        stack_quotation_single = list()
        stack_quotation_double = list()
        equal_num=0#等号出现的次数，方便定函数find_key_value中定keys的数量
        index=0
        while index<len(input):
            s=input[index]
            if (input[index:index+2] in self.special_signal_dict):
                index+=1
            # print(s,equal_num,len(stack_bracket),len(stack_quotation_double))
            else:
                if(s=='=' and len(stack_bracket)==0 and len(stack_quotation_single) ==0 and len(stack_quotation_double) ==0):
                    equal_num+=1

                if(s=='\''):
                    if(len(stack_quotation_single)==0):
                        stack_quotation_single.append('into_str')
                    else:
                        stack_quotation_single.pop()
                if(s == '\"'):
                    if (len(stack_quotation_double) == 0):
                        stack_quotation_double.append('into_str')
                    else:
                        stack_quotation_double.pop()
                if(s=="{" and len(stack_quotation_single) ==0 and len(stack_quotation_double) ==0):
                    stack_bracket.append('into_layer')
                if(s=="}" and len(stack_quotation_single) ==0 and len(stack_quotation_double) ==0):
                    try:
                        stack_bracket.pop()
                    except:
                        pass

            index+=1
        return equal_num

    def find_key_value(self,input):
        stack_bracket = list()  # 记录匹配括号用的栈
        stack_quotation_single = list()
        stack_quotation_double = list()
        keys=list()
        values=list()
        listall=list()
        last_comma=0
        index=0
        sum=1

        while index<len(input):
            s=input[index]
            # print s+str(len(stack_quotation_double))
            if (input[index:index+2] in self.special_signal_dict):
                index+=1
            # print(s,equal_num,len(stack_bracket),len(stack_quotation_double))
            else:
                if (s == ',' and len(stack_bracket) == 0 and len(stack_quotation_single) == 0 and len(
                        stack_quotation_double) == 0):
                    # keys.append()
                    # print(input[last_comma:index])
                    keys.append(sum)
                    sum += 1
                    values.append(input[last_comma:index])
                    last_comma=index+1
                if (s == '\'' and len(stack_quotation_double) == 0):
                    if (len(stack_quotation_single) == 0):
                        stack_quotation_single.append('into_str')
                    else:
                        stack_quotation_single.pop()
                if (s == '\"' and len(stack_quotation_single) == 0):
                    if (len(stack_quotation_double) == 0):
                        stack_quotation_double.append('into_str')
                    else:
                        stack_quotation_double.pop()
                if (s == "{" and len(stack_quotation_single) == 0 and len(stack_quotation_double) == 0):
                    stack_bracket.append('into_layer')
                if (s == "}" and len(stack_quotation_single) == 0 and len(stack_quotation_double) == 0):
                    stack_bracket.pop()
                if (index < len(input) - 2):
                    if (input[index:index + 2] in self.special_signal):
                        # print(input[index,index+2])
                        index += 1

            index+=1

        # print keys
        # print '_________'
        index=1
        for i in range(sum-1):
            if (self.contain_equal(values[i]) != 'No_contain'):
                listall.append((index,values[i]))
            else:
                listall.append((index,values[i]))
                index+=1
        return listall

    def str2list(self,input):
        # return input
        '''
        一定要逐个读
        :param str:
        :return:
        '''
        # if(input[-1]!=','):
        #     input=input+','
        # print input
        stack_quotation_single = list()
        stack_quotation_double = list()
        re_list = list()
        values = list()
        listall = list()
        sum=0
        last_comma = 0
        index = 0
        for s in input:

            if ((s == ',' or s=='\t') and len(stack_quotation_single) == 0 and len(stack_quotation_double) == 0):#\t是制表符，暂未测试
                sum+=1
                tmp_val=input[last_comma:index]

                if(self.is_int(tmp_val)):
                    tmp_val = int(tmp_val)  # value值是数字
                    re_list.append(tmp_val)
                elif(self.is_float(tmp_val)):
                    if self.science(tmp_val)=='int':
                        tmp_val=int(float(tmp_val))
                    else:
                        tmp_val = float(tmp_val)  # value值是数字
                    re_list.append(tmp_val)
                elif(tmp_val=='{}'):#防止漏掉{}
                    re_list.append([])
                elif(tmp_val=='nil'):
                    re_list.append(None)
                elif(tmp_val[0]=='{' and tmp_val[-1]=='}'):#list里面藏个dict
                    re_list.append(self.child_trans(tmp_val))
                elif (self.is_string(tmp_val)):
                    re_list.append(tmp_val[1:-1])
                else:
                    re_list.append(tmp_val)

                last_comma = index + 1
            if (s == '\'' and len(stack_quotation_double) == 0):
                if (len(stack_quotation_single) == 0):
                    stack_quotation_single.append('into_str')
                else:
                    stack_quotation_single.pop()
            if (s == '\"' and len(stack_quotation_single) == 0):
                if (len(stack_quotation_double) == 0):
                    stack_quotation_double.append('into_str')
                else:
                    stack_quotation_double.pop()
            # if (index < len(input) - 2):
            #     if (input[index:index + 2] in self.special_signal):
            #         # print(input[index,index+2])
            #         index += 1
            #         special_signal
            index += 1

        if(sum==0):

            if(self.is_int(input)):#input值是整数
                input = int(input)
            elif(self.is_float(input)):#input值是浮点数
                if(self.science(input)=='int'):
                    input=int(float(input))
                else:
                    input=float(input)
                    input=float(str(input))
            elif(self.is_bool(input)):#input是布尔值
                input=False if input=='false' else True
            elif(self.is_string(input)):
                input=input[1:-1]

                index_child=0
                input_tmp=''
                while index_child<len(input):
                    if (input[index_child:index_child + 2] in self.special_signal_dict.keys()):
                        input_tmp+=self.special_signal_dict[input[index_child:index_child + 2] ]
                        index_child+=1
                    else:
                        input_tmp+=input[index_child]
                    index_child+=1
                input=input_tmp
            return input
        return re_list

    def rmComments(self,input):
        '''
        去注释
        :return:
        '''
        # print input
        s_Commentsless = ''
        Comment_flag=0
        stack_quotation_single = list()
        stack_quotation_double = list()
        # Comment_flag==2表示单行注释 Comment_flag=4表示多行
        index=0
        while index<len(input):
            # print Comment_flag
            s=input[index]

            if ((ord(s)==10 or ord(s)==13) and len(stack_quotation_single) == 0 and len(stack_quotation_double) == 0):
                if(Comment_flag==2):
                    Comment_flag=0
            elif (input[index:index + 4 if index + 4 < len(input) else -1] == '--]]' and len(
                    stack_quotation_single) == 0 and len(stack_quotation_double) == 0):
                Comment_flag = 0
                index+=4
            elif (input[index:index + 2 if index + 2 < len(input) else -1] == ']]' and len(
                    stack_quotation_single) == 0 and len(stack_quotation_double) == 0):
                Comment_flag = 0
                index+=2
            elif (input[index:index + 4 if index + 4 < len(input) else -1] == '--[[' and len(
                    stack_quotation_single) == 0 and len(stack_quotation_double) == 0):
                Comment_flag = 4
                # print Comment_flag
            elif(Comment_flag!=4 and input[index:index+2 if index+2<len(input) else -1]=='--' and len(stack_quotation_single) == 0 and len(stack_quotation_double) == 0):
                Comment_flag=2
            elif(Comment_flag!=2 and Comment_flag!=4):
                s_Commentsless+=s
                if (s == '\'' and len(stack_quotation_double) == 0):
                    # s_Commentsless += str(len(stack_quotation_single))
                    if (len(stack_quotation_single) == 0):
                        stack_quotation_single.append('into_str')
                    else:
                        stack_quotation_single.pop()
                if (s == '\"' and len(stack_quotation_single) == 0):
                    # s_Commentsless += str(len(stack_quotation_double))
                    if (len(stack_quotation_double) == 0):
                        stack_quotation_double.append('into_str')
                    else:
                        stack_quotation_double.pop()
                if (index < len(input) - 2):
                    if (input[index:index + 2] in self.special_signal):
                        # print(input[index,index+2])
                        index+=1
                        s_Commentsless += input[index:index + 1]
                        # index += 1
                        # s_Commentsless += '?'
                        # s_Commentsless += str(len(stack_quotation_double))
            index+=1
        return s_Commentsless

    def rm_slash_n(self, input):
        '''
        合并到一行
        :param input:
        :return:
        '''
        s_blankless=''
        stack_quotation_single = list()
        stack_quotation_double = list()
        index=0
        for s in input:
            # if (s in self.special_signal):
            #     s_blankless += '\'
            if((ord(s)==10 or s=='\n') and len(stack_quotation_single) == 0 and len(stack_quotation_double) == 0):
                s_blankless += '\\n'
            else:
                if (s=='\\'):
                    s_blankless += '\\'
                else:
                    s_blankless += s


            index+=1
        return s_blankless

    def rmblank(self,input):
        '''
        去空格
        :param input:
        :return:
        '''
        s_blankless=''
        stack_quotation_single = list()
        stack_quotation_double = list()
        index=0
        while index<len(input):
            s=input[index]
            if ((s == ' ' or ord(s)==10 or ord(s)==9) and len(stack_quotation_single) == 0 and len(stack_quotation_double) == 0):
                pass
            else:
                s_blankless+=s
            if (s == '\'' and len(stack_quotation_double) == 0):
                # print(len(stack_quotation_single))
                if (len(stack_quotation_single) == 0):
                    stack_quotation_single.append('into_str')
                else:
                    stack_quotation_single.pop()
            if (s == '\"' and len(stack_quotation_single) == 0):
                if (len(stack_quotation_double) == 0):
                    stack_quotation_double.append('into_str')
                else:
                    stack_quotation_double.pop()
            if(index<len(input)-2):
                if(input[index:index+2] in self.special_signal):
                    # print(input[index,index+2])
                    index+=1
                    s_blankless += input[index:index+1]
                    # index+=1
                    # s_blankless +='?'



                # else:
                #     s_blankless += '\\'
            index+=1

        return s_blankless


    def Bracket_Match(self,input):
        '''
        匹配括号，得到对应的深度列表DeepLayer
        :param input:
        :return:
        '''

        stack=list() #记录匹配括号用的栈
        DeepLayer=list()#记录每个下标所在层深度的list
        flag_inString=False #False表示不在字符串内，True表示在
        index=0
        deeplayer=0
        while index < len(input):
            x=input[index]
            if x[index:index+2] in self.string_loc: #不会溢出，自动算到最末位
                flag_inString=True
            if(x=='{' and not flag_inString):
                stack.append('layer')
                deeplayer+=1
                DeepLayer.append(deeplayer)
            elif(x=='}' and not flag_inString):
                if(len(stack)>0):
                    stack.pop()
                    DeepLayer.append(deeplayer)
                    deeplayer -= 1
                else:
                    raise Exception("Bracket Match Error")
            else:
                DeepLayer.append(deeplayer)
            index+=1
        return DeepLayer

    def load(self,s):
        '''
        读取Lua table数据，输入s为一个符合Lua table定义的字符串，无返回值；若遇到Lua table格式错误的应该抛出异常
        :return:
        '''
        # x='{\r\nroot = {\r\n\t"Test Pattern String",\r\n\t-- {"object with 1 member" = {"array with 1 element",},},\r\n\t{["object with 1 member"] = {"array with 1 element",},},\r\n\t{},\r\n\t[99] = -42,\r\n\t[98] = {{}},\r\n\t[97] = {{},{}},\r\n\t[96] = {{}, 1, 2, nil},\r\n\t[95] = {1, 2, {["1"] = 1}},\r\n\t[94] = { {["1"]=1, ["2"]=2}, {1, ["2"]=2}, ["3"] = 3 },\r\n\ttrue,\r\n\tfalse,\r\n\tnil,\r\n\t{\r\n\t\t["integer"]= 1234567890,\r\n\t\treal=-9876.543210,\r\n\t\te= 0.123456789e-12,\r\n\t\tE= 1.234567890E+34,\r\n\t\tzero = 0,\r\n\t\tone = 1,\r\n\t\tspace = " ",\r\n\t\tquote = "\\"",\r\n\t\tbackslash = "\\\\",\r\n\t\tcontrols = "\\b\\f\\n\\r\\t",\r\n\t\tslash = "/ & \\\\",\r\n\t\talpha= "abcdefghijklmnopqrstuvwyz",\r\n\t\tALPHA = "ABCDEFGHIJKLMNOPQRSTUVWYZ",\r\n\t\tdigit = "0123456789",\r\n\t\tspecial = "`1~!@#$%^&*()_+-={\':[,]}|;.</>?",\r\n\t\thex = "0x01230x45670x89AB0xCDEF0xabcd0xef4A",\r\n\t\t["true"] = true,\r\n\t\t["false"] = false,\r\n\t\t["nil"] = nil,\r\n\t\tarray = {nil, nil,},\r\n\t\tobject = {  },\r\n\t\taddress = "50 St. James Street",\r\n\t\turl = "http://www.JSON.org/",\r\n\t\tcomment = "// /* <!-- --",\r\n\t\t["# -- --> */"] = " ",\r\n\t\t[" s p a c e d " ] = {1,2 , 3\r\n\r\n\t\t\t,\r\n\r\n\t\t\t4 , 5        ,          6           ,7        },\r\n\t\t--[[[][][]  Test multi-line comments\r\n\t\t\tcompact = {1,2,3,4,5,6,7},\r\n\t- -[luatext = "{\\"object with 1 member\\" = {\\"array with 1 element\\"}}",\r\n\t\tquotes = "&#34; (0x0022) %22 0x22 034 &#x22;",\r\n\t\t["\\\\\\"\\b\\f\\n\\r\\t`1~!@#$%^&*()_+-=[]{}|;:\',./<>?"]\r\n\t\t= "A key can be any string"]]\r\n\t--         ]]\r\n\t\tcompact = {1,2,3,4,5,6,7},\r\n\t\tluatext = "{\\"object with 1 member\\" = {\\"array with 1 element\\"}}",\r\n\t\tquotes = "&#34; (0x0022) %22 0x22 034 &#x22;",\r\n\t\t["\\\\\\"\\b\\f\\n\\r\\t`1~!@#$%^&*()_+-=[]{}|;:\',./<>?"]\r\n\t\t= "A key can be any string"\r\n\t},\r\n\t0.5 ,31415926535897932384626433832795028841971693993751058209749445923.\r\n\t,\r\n\t3.1415926535897932384626433832795028841971693993751058209749445923\r\n\t,\r\n\r\n\t1066\r\n\r\n\r\n\t,"rosebud"\r\n\r\n}}'
        # if x in s:
        #     raise Exception('right')
        # else:
        #     raise Exception('no')

        self.raw=s
        self.norm_Table = self.rmComments(s)  # 去注释
        # print(self.norm_Table)
        self.norm_Table=self.rmblank(self.norm_Table)#去空格规范化Table
        # self.norm_Table = self.rm_slash_n(s)  # 去空格规范化Table
        # print(self.norm_Table)
        # except:
        #     raise Exception("The format of input is wrong")

        pass

    def loadDict(self,d):
        '''
        读取dict中的数据，存入类中
        :return:
        '''

        self.Dict=d
        self.norm_Table = '{'
        self.dump_child(d)
        self.norm_Table += '}'


    def loadLuaTable(self,f):
        '''
        从文件中读取Lua table字符串
        :return:
        '''

        with open(f, 'r') as file_object:
            str=file_object.readlines()
            # print str
        str=''.join(str)
        str= '{{\nroot = {\n\t"Test Pattern String",\n\t-- {"object with 1 member" = {"array with 1 element",},},\n\t{["object with 1 member"] = {"array with 1 element",},},\n\t{},\n\t[99] = -42,\n\t[98] = {{}},\n\t[97] = {{},{}},\n\t[96] = {{}, 1, 2, nil},\n\t[95] = {1, 2, {["1"] = 1}},\n\t[94] = { {["1"]=1, ["2"]=2}, {1, ["2"]=2}, ["3"] = 3 },\n\ttrue,\n\tfalse,\n\tnil,\n\t{\n\t\t["integer"]= 1234567890,\n\t\treal=-9876.543210,\n\t\te= 0.123456789e-12,\n\t\tE= 1.234567890E+34,\n\t\tzero = 0,\n\t\tone = 1,\n\t\tspace = " ",\n\t\tquote = "\\"",\n\t\tbackslash = "\\\\",\n\t\tcontrols = "\\b\\f\\n\\r\\t",\n\t\tslash = "/ & \\\\",\n\t\talpha= "abcdefghijklmnopqrstuvwyz",\n\t\tALPHA = "ABCDEFGHIJKLMNOPQRSTUVWYZ",\n\t\tdigit = "0123456789",\n\t\tspecial = "`1~!@#$%^&*()_+-={\':[,]}|;.</>?",\n\t\thex = "0x01230x45670x89AB0xCDEF0xabcd0xef4A",\n\t\t["true"] = true,\n\t\t["false"] = false,\n\t\t["nil"] = nil,\n\t\tarray = {nil, nil,},\n\t\tobject = {  },\n\t\taddress = "50 St. James Street",\n\t\turl = "http://www.JSON.org/",\n\t\tcomment = "// /* <!-- --",\n\t\t["# -- --> */"] = " ",\n\t\t[" s p a c e d " ] = {1,2 , 3\n\n\t\t\t,\n\n\t\t\t4 , 5        ,          6           ,7        },\n\t\t--[[[][][]  Test multi-line comments\n\t\t\tcompact = {1,2,3,4,5,6,7},\n\t- -[luatext = "{\\"object with 1 member\\" = {\\"array with 1 element\\"}}",\n\t\tquotes = "&#34; (0x0022) %22 0x22 034 &#x22;",\n\t\t["\\\\\\"\\b\\f\\n\\r\\t`1~!@#$%^&*()_+-=[]{}|;:\',./<>?"]\n\t\t= "A key can be any string"]]\n\t--         ]]\n\t\tcompact = {1,2,3,4,5,6,7},\n\t\tluatext = "{\\"object with 1 member\\" = {\\"array with 1 element\\"}}",\n\t\tquotes = "&#34; (0x0022) %22 0x22 034 &#x22;",\n\t\t["\\\\\\"\\b\\f\\n\\r\\t`1~!@#$%^&*()_+-=[]{}|;:\',./<>?"]\n\t\t= "A key can be any string"\n\t},\n\t0.5 ,31415926535897932384626433832795028841971693993751058209749445923.\n\t,\n\t3.1415926535897932384626433832795028841971693993751058209749445923\n\t,\n\n\t1066\n\n\n\t,"rosebud"\n\n}}\n}'

        self.load(str)



    def dump_child(self,input):
        if isinstance(input ,list):
            self.norm_Table += str(input)[1:-1]+','
            return
        if isinstance(input ,dict):
            for key in input:
                if isinstance(input[key],dict) or isinstance(input[key],list):

                    self.norm_Table += str(key) + '={'
                    self.dump_child(input[key])
                    self.norm_Table += '},'
                else:
                    self.norm_Table += str(key) + '='
                    self.dump_child(input[key])
                    self.norm_Table += ','

        else:
            self.norm_Table += str(input)#'{'+str(input)+'}'
            return

    def dump(self):
        '''
        根据类中数据返回Lua table字符串
        :return:
        '''

        self.norm_Table='{'
        self.dump_child(self.Dict)
        self.norm_Table+='}'
        # print(self.norm_Table)

        return self.norm_Table

    def child_trans(self,input):
        '''
        可自身递归的函数
        :param index_start:
        :param index_end:
        :return:
        '''

        #如果最外有{}去掉
        if(input=='{}'):#这句没用，记得删掉
            input='[]'
        elif(input[0]=='{' and input[-1]=='}'):
            input=input[1:-1]
            if(input[-1]!=','):#规范，统一加逗号
                input+=','
        if(input[0]=='{' and input[-1]==',' and input[-2]=='}'):
            # print input
            try:
                if (input[-1] != ','):  # 规范，统一加逗号
                    input += ','
            except:
                pass
        # if (input[-1] != ','):  # 规范，统一加逗号
        #     input += ','
        print(input)

        child_Dict=dict()
        # DeepLayer=self.Bracket_Match(input)
        size=self.include_equal(input)
        # print input
        # print 'size:'+str(size)
        if size>0: # 如果同一级下的非字符串里有 = 符号，说明用dict数据类型，反之用list

            keys_values=self.find_key_value(input) #找到key和value两两组成tuple
            # print(keys_values)
            for key,value in keys_values:
                # print self.contain_equal(value)
                if(value[0]=='{' and value[-1]=='}' ):

                    pass

                elif(self.contain_equal(value)!='No_contain'):#最外层{}外面又没有等于号
                    contain_index=self.contain_equal(value)
                    key=value[:contain_index]


                    if(key[0]=='[' and key[-1]==']' ):#剥去最外层的壳
                        key=key[1:-1]
                        # print key


                    if(self.is_int(key)):#key值是整数
                        key=int(key)
                    elif(self.is_float(key)):#key值是浮点数
                        if (self.science(key) == 'int'):
                            key = int(float(key))
                        else:
                            key=float(key)
                    elif(self.is_string(key)):#key是字符型
                        key=key[1:-1]

                        index_child = 0
                        key_tmp = ''
                        while index_child < len(key):
                            if (key[index_child:index_child + 2] in self.special_signal_dict.keys()):
                                key_tmp += self.special_signal_dict[key[index_child:index_child + 2]]
                                index_child += 1
                            else:
                                key_tmp += key[index_child]
                            index_child += 1
                        key = key_tmp


                    value=value[contain_index+1:]
                    if (key == 'nil'  or value=='nil'):
                        continue
                    # if(self.is_string(value)):
                    #     value=value[1:-1]
                # print "Key:"+str(key)
                # print "Value:"+value
                if (value == '{}'):
                    child_Dict[key]=[]
                elif(value=='nil'):
                    continue
                #     child_Dict[key] =None
                else:
                    child_Dict[key]=self.child_trans(value) #套娃
        else:
            # print input
            return self.str2list(input)
        self.Dict=child_Dict

        return child_Dict
    def dumpDict(self):
        '''
        返回一个dict，包含类中的数据
        :return:
        '''

        left = self.norm_Table.find('{')
        right = self.norm_Table.rfind('}')
        self.norm_Table=self.norm_Table[left + 1:right]
        if(self.norm_Table[0]!='{'):
            self.norm_Table = '{'+self.norm_Table+'}'
        self.child_trans(self.norm_Table)#可自身递归的函数
        return self.Dict
        # print self.Dict['root']
        # print dict_answer['root']
        # return self.Dict==dict_answer

    def dumpLuaTable(self,f):
        '''
        将类中的内容以Lua table格式存入文件
        :return:
        '''

        # print self.norm_Table
        with open(f, 'w') as file_object:
            file_object.write(self.norm_Table)
        file_object.close()

        pass

if __name__ == '__main__':

    file_path='dumpLuaTable.txt'#保存地址，以Lua table格式存入文件


    a1 = PyLuaTblParser()
    a2 = PyLuaTblParser()
    a3 = PyLuaTblParser()

    test_str = '{\nroot = {\n\t"Test Pattern String",\n\t-- {"object with 1 member" = {"array with 1 element",},},\n\t{["object with 1 member"] = {"array with 1 element",},},\n\t{},\n\t[99] = -42,\n\t[98] = {{}},\n\t[97] = {{},{}},\n\t[96] = {{}, 1, 2, nil},\n\t[95] = {1, 2, {["1"] = 1}},\n\t[94] = { {["1"]=1, ["2"]=2}, {1, ["2"]=2}, ["3"] = 3 },\n\ttrue,\n\tfalse,\n\tnil,\n\t{\n\t\t["integer"]= 1234567890,\n\t\treal=-9876.543210,\n\t\te= 0.123456789e-12,\n\t\tE= 1.234567890E+34,\n\t\tzero = 0,\n\t\tone = 1,\n\t\tspace = " ",\n\t\tquote = "\\"",\n\t\tbackslash = "\\\\",\n\t\tcontrols = "\\b\\f\\n\\r\\t",\n\t\tslash = "/ & \\\\",\n\t\talpha= "abcdefghijklmnopqrstuvwyz",\n\t\tALPHA = "ABCDEFGHIJKLMNOPQRSTUVWYZ",\n\t\tdigit = "0123456789",\n\t\tspecial = "`1~!@#$%^&*()_+-={\':[,]}|;.</>?",\n\t\thex = "0x01230x45670x89AB0xCDEF0xabcd0xef4A",\n\t\t["true"] = true,\n\t\t["false"] = false,\n\t\t["nil"] = nil,\n\t\tarray = {nil, nil,},\n\t\tobject = {  },\n\t\taddress = "50 St. James Street",\n\t\turl = "http://www.JSON.org/",\n\t\tcomment = "// /* <!-- --",\n\t\t["# -- --> */"] = " ",\n\t\t[" s p a c e d " ] = {1,2 , 3\n\n\t\t\t,\n\n\t\t\t4 , 5        ,          6           ,7        },\n\t\t--[[[][][]  Test multi-line comments\n\t\t\tcompact = {1,2,3,4,5,6,7},\n\t- -[luatext = "{\\"object with 1 member\\" = {\\"array with 1 element\\"}}",\n\t\tquotes = "&#34; (0x0022) %22 0x22 034 &#x22;",\n\t\t["\\\\\\"\\b\\f\\n\\r\\t`1~!@#$%^&*()_+-=[]{}|;:\',./<>?"]\n\t\t= "A key can be any string"]]\n\t--         ]]\n\t\tcompact = {1,2,3,4,5,6,7},\n\t\tluatext = "{\\"object with 1 member\\" = {\\"array with 1 element\\"}}",\n\t\tquotes = "&#34; (0x0022) %22 0x22 034 &#x22;",\n\t\t["\\\\\\"\\b\\f\\n\\r\\t`1~!@#$%^&*()_+-=[]{}|;:\',./<>?"]\n\t\t= "A key can be any string"\n\t},\n\t0.5 ,31415926535897932384626433832795028841971693993751058209749445923.\n\t,\n\t3.1415926535897932384626433832795028841971693993751058209749445923\n\t,\n\n\t1066\n\n\n\t,"rosebud"\n\n}}\n'
    # a1.load(test_str)
    a1.loadLuaTable('input.txt')
    d1 = a1.dumpDict()
    print d1