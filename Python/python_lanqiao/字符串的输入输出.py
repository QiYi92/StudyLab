n=int(input())
#n行以内的字符串直接输出
for i in range(n):
    answer=input()
    print(answer)
    print() #换行
#n行以外的字符串换行分割输出
while True:
    # .split()函数用空格切割字符串
    #"D O T CPP"--->['D','O','T','CPP']
    answer=input().split()
    for i in answer:
        print(i)
        print()
