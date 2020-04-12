#encoding:utf-8

class PyLuaTblParser:
    def __init__(self):
        self.special_signal={'\t','\n','\\','\'','\"','\a','\b','\f','\r','\v'}
        self.string_loc=list()#字符串的位置下标
        # self.DeepLayer=list()#记录每个下标所在层深度的list
        self.norm_Table='' #去空格标准化后的table
        self.Dict=dict()#python格式字典
        pass

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
                stack_bracket.pop()
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

        print(keys,values)
        print('_')
        for i in range(sum-1):
            # print (keys[i],values[i])
            listall.append((keys[i],values[i]))
        return listall

    def str2list(self,str):
        '''
        一定要逐个读
        :param str:
        :return:
        '''
        return list(str)

    def rmblank(self,input):
        '''
        去空格
        :param input:
        :return:
        '''
        s_blankless=input

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
            # print s
            s_blankless=self.rmblank(s)
            self.norm_Table=s_blankless #规范化Table
        except:
            raise Exception("The format of input is wrong")

        pass

    def loadDict(self,d):
        '''
        读取dict中的数据，存入类中
        :return:
        '''

        pass
    def loadLuaTable(self,f):
        '''
        从文件中读取Lua table字符串
        :return:
        '''
        pass

    def dump(self):
        '''
        根据类中数据返回Lua table字符串
        :return:
        '''
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
                    value=value[contain_index+1:]

                # print('key__:',(key))

                child_Dict[key]=self.child_trans(value) #套娃
                print ('Dict___', child_Dict)
        else:
            return self.str2list(input)
        return child_Dict
    def dumpDict(self):
        '''
        返回一个dict，包含类中的数据
        :return:
        '''

        self.child_trans(self.norm_Table)#可自身递归的函数
        pass
    def dumpLuaTable(self,f):
        '''
        将类中的内容以Lua table格式存入文件
        :return:
        '''

        pass




if __name__ == '__main__':
    file_path='/Users/zhangwei/Desktop'#保存地址，以Lua table格式存入文件

    a1 = PyLuaTblParser()
    a2 = PyLuaTblParser()
    a3 = PyLuaTblParser()
    # test_str = '{array = {65,23,5,},dict = {mixed = {43,54.33,false,9,string = "value",},array = {3,6,4,},string = "value",},}'
    test_str = '{array={65,23,5,},dict={mixed={43,54.33,false,9,string="value",},array = {3,6,4,},string = "value",},}'
    # test_str = '{65,23,5,}'
    a1.load(test_str)
    d1 = a1.dumpDict()
    # a2.loadDict(d1)
    # a2.dumpLuaTable(file_path)
    # a3.loadLuaTable(file_path)
    # d3 = a3.dumpDict()