def f(num):
    # 定义几个空列表存放四平方和的元素及结果
    a=[]
    b=[]
    c=[]
    d=[]
    res=[]
    # 类型判断，若n不是正整数int型，则返回(0,0,0,0)
    if type(num) != int: #类型判断
        res.append('无')
        print('(0,0,0,0)')
    # 遍历0-9随机数获取四平方和元素
    for item in range(0,9): # 遍历到9，所以range(0,9+1)
        a.append(item) # a[0,1,2,3,4,5,6,7,8,9]
        b.append(item) # b[0,1,2,3,4,5,6,7,8,9]
        c.append(item) # c[0,1,2,3,4,5,6,7,8,9]
        d.append(item) # d[0,1,2,3,4,5,6,7,8,9]
    for item1 in a:
        for item2 in b:
            for item3 in c:
                for item4 in d:
                    w = item1
                    x = item2
                    y = item3
                    z = item4
                    # 进行判断条件元素的元素组合
                    if w**2+x**2+y**2+z**2 == num:
                        # 将满足条件元素添加到空列表
                        res.append((w,x,y,z))
    #对满足条件元素做排序取出答案
    print('最佳分解方案:',min(res))

print(f(int(input())))