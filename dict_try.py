<<<<<<< HEAD
Dict={"array": [65, 23, 5], "dict": { "mixed": {1: 43, 2: 54.33, 3: False, 4: 9, "string": "value" }, "array": [3, 6, 4], "string": "value" } }

=======
# Dict={"array": [65, 23, 5], "dict": { "mixed": {1: 43, 2: 54.33, 3: False, 4: 9, "string": "value" }, "array": [3, 6, 4], "string": "value" } }
import numpy as np

def sigmoid(x):
    s = 1 / (1 + np.exp(-x))
    return s
>>>>>>> solved some problem but not good
# print(type(Dict))
#
# Dict["array"]=1
# for x,y in Dict.items():
#     print x,y
<<<<<<< HEAD

a=1
Dict1={}
Dict1[a]=Dict
print(Dict1)

# print(('"a","b"'.split(",")))
# a=[("a",1),("b",2),("c",3)]
# print(type(a[1]))
# for x,y in a:
#
#     print(x,y)
#     print("-")

# a=list()
# print(len(a))
# keys=list(range(4))[1:]
# print(keys)
# a=[]
# print(len(a))
#
# a.append('f')
# a.pop()
# print(len(a))
=======
# print(isinstance(Dict ,dict))
# if isinstance(Dict ,dict):
#     print('pp')
# for key in Dict:
#     print Dict[key]
# print(Dict1)
print(chr(10))

#
# E=125.4
# print(0.5+sigmoid(-100/E))
# E=64.7
# print(0.5+sigmoid(-100/E))
# E=90.8
# print(0.5+sigmoid(-100/E))
# # print(('"a","b"'.split(",")))
# # a=[("a",1),("b",2),("c",3)]
# # print(type(a[1]))
# # for x,y in a:
# #
# #     print(x,y)
# #     print("-")
#
# # a=list()
# # print(len(a))
# # keys=list(range(4))[1:]
# # print(keys)
# # a=[]
# # print(len(a))
# #
# # a.append('f')
# # a.pop()
# # print(len(a))
# import scipy.stats
# # from scipy import stats, optimize, interpolate
# import pandas as pd
# a = np.array([[81,80],[67,70],[75,75]])
# data = pd.DataFrame(a, index=["a", "b","c"], columns=["one", "two"])
#
# correlation, pvalue = scipy.stats.pearsonr(data.one, data.two)
# print (correlation, pvalue)
# print(data)
# # 计算第一列和第二列的相关系数
# print(data.one.corr(data.two))
# # 1.0
# # 返回一个相关系数矩阵
# print(data.corr())
#
# # 计算第一列和第二列的协方差
# print(data.one.cov(data.two))
# # 9.0
# # 返回一个协方差矩阵
# print(data.cov())
#
# #
# # for i in range(128):
# #     print('if (ord(s) == '+str(i)+'):')
# #     print('\traise Exception(s)')
>>>>>>> solved some problem but not good
