def An(n,i=1):
#A1=sin1
#A2=sin(1-sin2)
#A3=sin(1-sin(2+sin(3)))
    if i==n:
        return 'sin('+str(n)+')'
    else:
        if i%2==0: #判断i的奇偶性
            s='+'
        else:
            s='-'
        return 'sin('+str(i)+s+An(n,i+1)+')'
def Sn(m,i=1):
#S1=A1+1
#S2=(A1+2)A2+1
#S3=((A1+3)A2+2)A3+1
    if m==1:
        return An(m)+'+'+str(i) #S1=A1+1
    else:
        return '('+Sn(m-1,i+1)+')'+An(m)+'+'+str(i)

num=int(input())
print(Sn(num))