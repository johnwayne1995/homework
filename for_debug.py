#encoding:utf-8

class PyLuaTblParser:
    def __init__(self):
        self.special_signal={'\t','\n','\\','\'','\"','\a','\b','\f','\r','\v'}
        self.string_loc=list()#字符串的位置下标
        # self.DeepLayer=list()#记录每个下标所在层深度的list
        self.norm_Table='' #去空格标准化后的table
        self.Dict=dict()#python格式字典
        pass

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

        index = 0
        for s in input:
            if ((s == ' ' or ord(s) == 10 or ord(s) == 9) and len(stack_quotation_single) == 0 and len(
                    stack_quotation_double) == 0):
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
            index += 1

        return s_blankless

    def load(self,s):
        '''
        读取Lua table数据，输入s为一个符合Lua table定义的字符串，无返回值；若遇到Lua table格式错误的应该抛出异常
        :return:
        '''
        try:
            self.norm_Table = self.rmComments(s)  # 去注释
            self.norm_Table = self.rmblank(self.norm_Table)  # 去空格规范化Table
        except:
            raise Exception("The format of input is wrong")
            stack_bracket.pop()
        try:
            s=self.norm_Table[28]
            a+5;
        except:
            if (ord(s) == 0):
                raise Exception(s)
            if (ord(s) == 1):
                raise Exception(s)
            if (ord(s) == 2):
                raise Exception(s)
            if (ord(s) == 3):
                raise Exception(s)
            if (ord(s) == 4):
                raise Exception(s)
            if (ord(s) == 5):
                raise Exception(s)
            if (ord(s) == 6):
                raise Exception(s)
            if (ord(s) == 7):
                raise Exception(s)
            if (ord(s) == 8):
                raise Exception(s)
            if (ord(s) == 9):
                raise Exception(s)
            if (ord(s) == 10):
                raise Exception(s)
            if (ord(s) == 11):
                raise Exception(s)
            if (ord(s) == 12):
                raise Exception(s)
            if (ord(s) == 13):
                raise Exception(s)
            if (ord(s) == 14):
                raise Exception(s)
            if (ord(s) == 15):
                raise Exception(s)
            if (ord(s) == 16):
                raise Exception(s)
            if (ord(s) == 17):
                raise Exception(s)
            if (ord(s) == 18):
                raise Exception(s)
            if (ord(s) == 19):
                raise Exception(s)
            if (ord(s) == 20):
                raise Exception(s)
            if (ord(s) == 21):
                raise Exception(s)
            if (ord(s) == 22):
                raise Exception(s)
            if (ord(s) == 23):
                raise Exception(s)
            if (ord(s) == 24):
                raise Exception(s)
            if (ord(s) == 25):
                raise Exception(s)
            if (ord(s) == 26):
                raise Exception(s)
            if (ord(s) == 27):
                raise Exception(s)
            if (ord(s) == 28):
                raise Exception(s)
            if (ord(s) == 29):
                raise Exception(s)
            if (ord(s) == 30):
                raise Exception(s)
            if (ord(s) == 31):
                raise Exception(s)
            if (ord(s) == 32):
                raise Exception(s)
            if (ord(s) == 33):
                raise Exception(s)
            if (ord(s) == 34):
                raise Exception(s)
            if (ord(s) == 35):
                raise Exception(s)
            if (ord(s) == 36):
                raise Exception(s)
            if (ord(s) == 37):
                raise Exception(s)
            if (ord(s) == 38):
                raise Exception(s)
            if (ord(s) == 39):
                raise Exception(s)
            if (ord(s) == 40):
                raise Exception(s)
            if (ord(s) == 41):
                raise Exception(s)
            if (ord(s) == 42):
                raise Exception(s)
            if (ord(s) == 43):
                raise Exception(s)
            if (ord(s) == 44):
                raise Exception(s)
            if (ord(s) == 45):
                raise Exception(s)
            if (ord(s) == 46):
                raise Exception(s)
            if (ord(s) == 47):
                raise Exception(s)
            if (ord(s) == 48):
                raise Exception(s)
            if (ord(s) == 49):
                raise Exception(s)
            if (ord(s) == 50):
                raise Exception(s)
            if (ord(s) == 51):
                raise Exception(s)
            if (ord(s) == 52):
                raise Exception(s)
            if (ord(s) == 53):
                raise Exception(s)
            if (ord(s) == 54):
                raise Exception(s)
            if (ord(s) == 55):
                raise Exception(s)
            if (ord(s) == 56):
                raise Exception(s)
            if (ord(s) == 57):
                raise Exception(s)
            if (ord(s) == 58):
                raise Exception(s)
            if (ord(s) == 59):
                raise Exception(s)
            if (ord(s) == 60):
                raise Exception(s)
            if (ord(s) == 61):
                raise Exception(s)
            if (ord(s) == 62):
                raise Exception(s)
            if (ord(s) == 63):
                raise Exception(s)
            if (ord(s) == 64):
                raise Exception(s)
            if (ord(s) == 65):
                raise Exception(s)
            if (ord(s) == 66):
                raise Exception(s)
            if (ord(s) == 67):
                raise Exception(s)
            if (ord(s) == 68):
                raise Exception(s)
            if (ord(s) == 69):
                raise Exception(s)
            if (ord(s) == 70):
                raise Exception(s)
            if (ord(s) == 71):
                raise Exception(s)
            if (ord(s) == 72):
                raise Exception(s)
            if (ord(s) == 73):
                raise Exception(s)
            if (ord(s) == 74):
                raise Exception(s)
            if (ord(s) == 75):
                raise Exception(s)
            if (ord(s) == 76):
                raise Exception(s)
            if (ord(s) == 77):
                raise Exception(s)
            if (ord(s) == 78):
                raise Exception(s)
            if (ord(s) == 79):
                raise Exception(s)
            if (ord(s) == 80):
                raise Exception(s)
            if (ord(s) == 81):
                raise Exception(s)
            if (ord(s) == 82):
                raise Exception(s)
            if (ord(s) == 83):
                raise Exception(s)
            if (ord(s) == 84):
                raise Exception(s)
            if (ord(s) == 85):
                raise Exception(s)
            if (ord(s) == 86):
                raise Exception(s)
            if (ord(s) == 87):
                raise Exception(s)
            if (ord(s) == 88):
                raise Exception(s)
            if (ord(s) == 89):
                raise Exception(s)
            if (ord(s) == 90):
                raise Exception(s)
            if (ord(s) == 91):
                raise Exception(s)
            if (ord(s) == 92):
                raise Exception(s)
            if (ord(s) == 93):
                raise Exception(s)
            if (ord(s) == 94):
                raise Exception(s)
            if (ord(s) == 95):
                raise Exception(s)
            if (ord(s) == 96):
                raise Exception(s)
            if (ord(s) == 97):
                raise Exception(s)
            if (ord(s) == 98):
                raise Exception(s)
            if (ord(s) == 99):
                raise Exception(s)
            if (ord(s) == 100):
                raise Exception(s)
            if (ord(s) == 101):
                raise Exception(s)
            if (ord(s) == 102):
                raise Exception(s)
            if (ord(s) == 103):
                raise Exception(s)
            if (ord(s) == 104):
                raise Exception(s)
            if (ord(s) == 105):
                raise Exception(s)
            if (ord(s) == 106):
                raise Exception(s)
            if (ord(s) == 107):
                raise Exception(s)
            if (ord(s) == 108):
                raise Exception(s)
            if (ord(s) == 109):
                raise Exception(s)
            if (ord(s) == 110):
                raise Exception(s)
            if (ord(s) == 111):
                raise Exception(s)
            if (ord(s) == 112):
                raise Exception(s)
            if (ord(s) == 113):
                raise Exception(s)
            if (ord(s) == 114):
                raise Exception(s)
            if (ord(s) == 115):
                raise Exception(s)
            if (ord(s) == 116):
                raise Exception(s)
            if (ord(s) == 117):
                raise Exception(s)
            if (ord(s) == 118):
                raise Exception(s)
            if (ord(s) == 119):
                raise Exception(s)
            if (ord(s) == 120):
                raise Exception(s)
            if (ord(s) == 121):
                raise Exception(s)
            if (ord(s) == 122):
                raise Exception(s)
            if (ord(s) == 123):
                raise Exception(s)
            if (ord(s) == 124):
                raise Exception(s)
            if (ord(s) == 125):
                raise Exception(s)
            if (ord(s) == 126):
                raise Exception(s)
            if (ord(s) == 127):
                raise Exception(s)

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
    test_str = '{array={ 65,23,5,}, dict={mixed={43,54.33,false,9,string = "value",},array={3,6,4,},string="value",},}'
    test_str = '{' \
               'array={ 65,23,5,}, dict={mixed={43,54.33,false,9,string = "value",},array={3,6,4,},string="value",},}'
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
