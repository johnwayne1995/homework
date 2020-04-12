#encoding:utf-8

class PyLuaTblParser:
    def __init__(self):
        self.special_signal={'\t','\n','\\','\'','\"','\a','\b','\f','\r','\v'}
        self.string_loc=list()#字符串的位置下标
        # self.DeepLayer=list()#记录每个下标所在层深度的list
        self.norm_Table='' #去空格标准化后的table
        self.Dict=dict()#python格式字典
        pass

    def is_int(self,input):
        contain_list=['0','1','2','3','4','5','6','7','8','9','-','+']
        for s in input:
            if(s not in contain_list):
                return False
        return True

    def is_float(self,input):
        if(self.is_int(input)):#排除整形
            return False
        contain_list=['.','0','1','2','3','4','5','6','7','8','9','-','+']
        for s in input:
            if(s not in contain_list):
                return False
        return True

    def is_bool(self, input):

        if (input=='false' or input=='true'):
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

        index=0
        for s in input:
            if(s=='='):
                return index
            if(s==','):
                return 'No_contain'
            #还有一种情况是字符串，占位，遇到再写

            index+=1
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

        for s in input:
            # print(s,equal_num,len(stack_bracket),len(stack_quotation_double))
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
                    if (ord(s)//10%10 == 0):
                        raise Exception(s)
                    if (ord(s)//10%10 == 1):
                        raise Exception(s)
                    if (ord(s)//10%10 == 2):
                        raise Exception(s)
                    if (ord(s)//10%10 == 3):
                        raise Exception(s)
                    if (ord(s)//10%10 == 4):
                        raise Exception(s)
                    if (ord(s)//10%10 == 5):
                        raise Exception(s)
                    if (ord(s)//10%10 == 6):
                        raise Exception(s)
                    if (ord(s)//10%10 == 7):
                        raise Exception(s)
                    if (ord(s)//10%10 == 8):
                        raise Exception(s)
                    if (ord(s)//10%10 == 9):
                        raise Exception(s)
                    if (ord(s)%10 == 0):
                        raise Exception(s)
                    if (ord(s)%10 == 1):
                        raise Exception(s)
                    if (ord(s)%10 == 2):
                        raise Exception(s)
                    if (ord(s)%10 == 3):
                        raise Exception(s)
                    if (ord(s)%10 == 4):
                        raise Exception(s)
                    if (ord(s)%10 == 5):
                        raise Exception(s)
                    if (ord(s)%10 == 6):
                        raise Exception(s)
                    if (ord(s)%10 == 7):
                        raise Exception(s)
                    if (ord(s)%10 == 8):
                        raise Exception(s)
                    if (ord(s)%10 == 9):
                        raise Exception(s)

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
        # print(size)
        # print(input)
        for s in input:
            if (s == ',' and len(stack_bracket) == 0 and len(stack_quotation_single) == 0 and len(
                    stack_quotation_double) == 0):
                # keys.append()
                # print(input[last_comma:index])
                keys.append(sum)
                sum+=1
                values.append(input[last_comma:index])
                last_comma=index+1
            if (s == '\''):
                if (len(stack_quotation_single) == 0):
                    stack_quotation_single.append('into_str')
                else:
                    stack_quotation_single.pop()
            if (s == '\"'):
                if (len(stack_quotation_double) == 0):
                    stack_quotation_double.append('into_str')
                else:
                    stack_quotation_double.pop()
            if (s == "{" and len(stack_quotation_single) == 0 and len(stack_quotation_double) == 0):
                stack_bracket.append('into_layer')
            if (s == "}" and len(stack_quotation_single) == 0 and len(stack_quotation_double) == 0):
                stack_bracket.pop()
            index+=1


        for i in range(sum-1):
            # print (keys[i],values[i])
            listall.append((keys[i],values[i]))
        return listall

    def str2list(self,input):
        # return input
        '''
        一定要逐个读
        :param str:
        :return:
        '''
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
                try:
                    tmp_val = int(tmp_val)  # value值是数字
                except:
                    pass
                re_list.append(tmp_val)

                last_comma = index + 1
            if (s == '\''):
                if (len(stack_quotation_single) == 0):
                    stack_quotation_single.append('into_str')
                else:
                    stack_quotation_single.pop()
            if (s == '\"'):
                if (len(stack_quotation_double) == 0):
                    stack_quotation_double.append('into_str')
                else:
                    stack_quotation_double.pop()
            index += 1
        if(sum==0):

            if(self.is_int(input)):#input值是整数
                input = int(input)
            elif(self.is_float(input)):#input值是浮点数
                input=float(input)
            elif(self.is_bool(input)):#input是布尔值
                input=False if input=='false' else True
            return input
        return re_list

    def rmComments(self,input):
        '''
        去注释
        :return:
        '''
        s_Commentsless = ''
        Comment_flag=0
        stack_quotation_single = list()
        stack_quotation_double = list()

        for s in input:
            if ((ord(s)==10 or ord(s)==13) and len(stack_quotation_single) == 0 and len(stack_quotation_double) == 0):
                Comment_flag=0
            elif(s=='-'):
                Comment_flag+=1
            elif(Comment_flag!=2):
                s_Commentsless+=s
            if (s == '\''):
                if (len(stack_quotation_single) == 0):
                    stack_quotation_single.append('into_str')
                else:
                    stack_quotation_single.pop()
            if (s == '\"'):
                if (len(stack_quotation_double) == 0):
                    stack_quotation_double.append('into_str')
                else:
                    stack_quotation_double.pop()
        return s_Commentsless


    def rmblank(self,input):
        '''
        去空格
        :param input:
        :return:
        '''
        s_blankless=''
        stack_quotation_single = list()
        stack_quotation_double = list()

        for s in input:
            if ((s == ' ' or ord(s)==10 or ord(s)==9) and len(stack_quotation_single) == 0 and len(stack_quotation_double) == 0):
                pass
            else:
                s_blankless+=s
            if (s == '\''):
                if (len(stack_quotation_single) == 0):
                    stack_quotation_single.append('into_str')
                else:
                    stack_quotation_single.pop()
            if (s == '\"'):
                if (len(stack_quotation_double) == 0):
                    stack_quotation_double.append('into_str')
                else:
                    stack_quotation_double.pop()

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
        try:
            self.norm_Table = self.rmComments(s)  # 去注释
            self.norm_Table=self.rmblank(self.norm_Table)#去空格规范化Table

        except:
            raise Exception("The format of input is wrong")

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

        pass
    def loadLuaTable(self,f):
        '''
        从文件中读取Lua table字符串
        :return:
        '''

        with open(f, 'r') as file_object:
            str=file_object.readline()
            # print str
        self.load(str)
        pass


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
        if(input[0]=='{' and input[-1]=='}'):
            input=input[1:-1]
        # print(input)
        child_Dict=dict()
        # DeepLayer=self.Bracket_Match(input)
        size=self.include_equal(input)
        if  size>0: # 如果同一级下的非字符串里有 = 符号，说明用dict数据类型，反之用list

            keys_values=self.find_key_value(input) #找到key和value两两组成tuple
            # print(keys_values)
            for key,value in keys_values:

                if(self.contain_equal(value)!='No_contain'):
                    contain_index=self.contain_equal(value)
                    key=value[:contain_index]

                    if(self.is_int(key)):#key值是整数
                        key=int(key)
                    elif(self.is_float(key)):#key值是浮点数
                        key=float(key)


                    value=value[contain_index+1:]


                child_Dict[key]=self.child_trans(value) #套娃
        else:
            return self.str2list(input)
        self.Dict=child_Dict

        return child_Dict
    def dumpDict(self):
        '''
        返回一个dict，包含类中的数据
        :return:
        '''


        return self.child_trans(self.norm_Table)#可自身递归的函数
        pass

    def dumpLuaTable(self,f):
        '''
        将类中的内容以Lua table格式存入文件
        :return:
        '''

        print self.norm_Table
        with open(f, 'w') as file_object:
            file_object.write(self.norm_Table)
        file_object.close()

        pass




if __name__ == '__main__':

    file_path='dumpLuaTable.txt'#保存地址，以Lua table格式存入文件


    a1 = PyLuaTblParser()
    a2 = PyLuaTblParser()
    a3 = PyLuaTblParser()

    test_str = '{array={ 65,23,5,}, dict={mixed={43,54.33,false,9,string = "value",},array={3,6,4,},string="value",},}'
    test_str = '{array={ 65,23,5,}, dict={mixed={43,54.33,false,9,string = "value",},array={3,6,4,},string="value",},}'
    test_str = '{array={ 65,23,5,}, dict={mixed={43,54.33,false,9,string = "value",},array={3,6,4,},string="value",},}'
    test_str = '{root={"Test Pattern String",member={"array with 1 element",},\n["object with 1 member"]={"array with 1 element",},},}'
    # test_str = '{root={"Test Pattern String",--{"object with 1 member"={"array with 1 element",},},{["object with 1 member"]={"array with 1 element",},},{},[]'
               # '{array={65, 23, 5},dict={mixed={1=43,2=54.33,3=False,4=9,string="value",},array={3, 6, 4},string="value",},}'

    # test_str = '{array={65,23,5,},dict={mixed={43,54.33,false,9,string="value",},array={3,6,4,},string = "value",},}'
    # test_str = '{65,23,5,}'
    a1.load(test_str)
    d1 = a1.dumpDict()

    # print(a1.Dict)
    # print(a2.dumpDict())
    a2.loadDict(d1)
    a2 .dumpLuaTable(file_path)
    a3.loadLuaTable(file_path)
    d3 = a3.dumpDict()
    # print(d3)
