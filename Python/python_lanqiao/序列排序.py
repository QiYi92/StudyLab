def bublle_sort(l):
    #冒泡排序
    n=len(l)
    #一趟只归位出一个数字，如果有n个数字，需要进行n-1趟
    for j in range(n-1):
        count = 0 #计数器归零
        #归位后数字不需要比较，所以每趟只需要比较n-1-j次（j为已执行趟数）
        for i in range(0,n-1-j):
            if l[i] > l[i+1]:
                l[i],l[i+1] = l[i+1],l[i]
                count += 1 #每交换一次，计数器加一
        if 0 == count: #如果计数器为零，也就是无需交换时，结束
            break
if __name__ == "__main__":
    n=int(input())
    alist=list(map(int,input().split()))
    bublle_sort(alist)
    #如果直接print(alist)
    #会输出数组[3,4,5,6,7]
    #题目要求输出3 4 5 6 7
    #故只能用for循环依次输出
    for i in range(len(alist)):
        print(alist[i],"",end='') #" "表示空格,end=' '的作用是输出不换行

n=int(input())
if n>=1 and n<=200:
    sl=list(map(int,input().split()))
    sl.sort() #sort()排序函数，默认reverse=False从小到大输出,reverse=True则相反
    for i in range(len(sl)):
        print(sl[i],"",end='') #end=' '的作用是输出不换行