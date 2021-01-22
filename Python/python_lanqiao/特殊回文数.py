for i in range(1000,10000):
    # 将int型变为str字符串型再进行倒置
    if str(i)==str(i)[::-1]:
        print(i)


# n=int(input())
# for i in range(10000,1000000): #求五位到六位的十进制数
#     a=str(i) #把int数变为str字符串
#     b=0 #初始化
#     if a==a[::-1]: #这里a[::-1]表示把字符串a倒序
#         #遍历a每一个字符
#         for j in a:
#             b+=int(j) #使a的每一个字符相加
#         if b==n: #如果相加值等于输入值，则输出
#             print(a)