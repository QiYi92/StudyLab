# #十六转八
# n=int(input())
# for i in range(n):
#     if n<=10:
#         s=input() #输入要转换的字符串
#         if len(s)<=100000:
#             res_1=int(s,16) #这里的int(s,16)代表把16进制的s转化成10进制
#             res_2=oct(res_1) #这里的oct代表把一个整数转化为八进制
#             print(res_2[2:]) #这里的[2:]是代表结果从第三位开始输出

# #十六转十
# n=input() #十六进制不用int()
# res_1=int(n,16)
# print(res_1)

#十转十六
a=int(input())
if a>=0 and a<=2147483647:
    res_1=hex(a).upper() #十转十六用hex()函数换算
    #str.upper() 将小写变成大写
    #str.lower() 将大写变成小写
    print(res_1[2:])

