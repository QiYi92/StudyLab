# 2029回文串
n = int(input())
for i in range(n):
    s=str(input())
    l = 0
    r = len(s) - 1
    switch = True
    for j in range(int(len(s)/2)):
        if s[l]==s[r]:
            l+=1
            r-=1
        else:
            print('no')
            switch = False
            break
    if switch == True:
            print('yes')
