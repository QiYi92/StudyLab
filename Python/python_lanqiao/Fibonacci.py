# while True:
#     try:
#         n=int(input()) #输入
#         F1,F2 = 1,1
#         for i in range(3,n+1):
#             F1,F2=F2%10007,(F1+F2)%10007
#         print(F2)
#     except:
#         break
while True:
    try: #try except异常处理机制
        n=int(input()) #输入
        F1,F2=1,1
        for i in range(3,n+1): #斐波那契数列从3开始到n+1
            #F1等于数列里的下一个数，也就是F2
            #F2等于前两项相加
            F1, F2 = F2 % 10007, (F1 + F2) % 10007
        print(F2) #输出在for循环外，不可与for循环同行
    except:
        break