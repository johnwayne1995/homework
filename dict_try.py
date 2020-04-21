# #encoding:utf-8
dict={}
#
# # x=1.234567890E+34
# # controls = "\b\f\n\r\t",
# controls1 = '\\\\\\"\\b\\f\\n\\r\\tafasg'
# # dict['a']=controls1
# print (dict)
# # print (str.encode(controls1))
#
# strEncodeDecode = {
#             '\\a': '\a', '\\b': '\b', '\\f': '\f', '\\n': '\n', '\\r': '\r',
#             '\\t': '\t', '\\v': '\v', "\\'": "\'", '\\"': '\"', '\\?': '\?'
#         }
# strEncodeDecode_four={'\\\\': '\\'}
#
# print strEncodeDecode.items()
# print strEncodeDecode
# # for key in strEncodeDecode:
# #     print key
# #     print strEncodeDecode[key]
#     # if a in controls1:
#     #     print a
# new_controls=''
# index=0
# while index<len(controls1):
#     # print (controls1[index+2] in strEncodeDecode.keys())
#     s=controls1[index]
#     if controls1[index:index+2] in strEncodeDecode.keys():
#         print '------'
#         new_controls+=strEncodeDecode[controls1[index:index+2]]
#         index+=1
#     elif(controls1[index:index+2] in strEncodeDecode_four.keys()):
#         print 'YES'
#         new_controls += strEncodeDecode_four[controls1[index:index + 2]]
#         index +=1
#     else:
#         new_controls+=s
#     index+=1
# dict['a']=new_controls
# print dict
#



e= 1.23456789e-13
var1=3.1415926535897932384626433832795028841971693993751058209749445923
# var2=float(var1)
var2=float(str(var1))
print var2
dict['a']=var2
print dict

dict1={1:[1,2,3]}

print dict1

str=['{\n', ' ', 'root']
x='{\n root'
str=''.join(str)
print str==x