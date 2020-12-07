row = 1
#定义起始行
while row <= 9:
    #最大打印9行
    col = 1
    #起始列
    while col <= row:
        print("%d * %d = %d" % (row,col,row*col),end = '\t')
        col += 1
    print('')
    row += 1
