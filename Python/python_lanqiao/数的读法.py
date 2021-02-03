d={'1':'yi','2':'er','3':'san','4':'si','5':'wu','6':'liu','7':'qi','8':'ba','9':'jiu','0':'ling'}
n=input().strip() #str.strip()就是把字符串头和尾的空格，以及头尾的\n和\t之类的删掉
a=[]
b=[] #b储存逆序的读法，最后再逆序输出结果

def numexchange(i): #数字交换
    i=i[::-1] #逆序输出i; 7009-->9007
    for j in range(len(i)): #因为上面进行逆序，所以for循环从左到右就是个 十 百 千
        if j==0: #个位
            if i[j]!='0':
                b.append(d[i[j]]) #i的第j个数 替换成对应拼音 添加到b列表
        elif j==1: #十位
            if i[j]=='0' and i[0]!='0': #十位为0，个位不为0
                b.append(d['0']) #ling
            elif i[j]=='1'and len(i)==2: #十位为1，i长度为2
                b.append('shi')
            elif i[j]!='0': #十位不为0
                b.append('shi')
                b.append(d[i[j]]) #值为2就是二十
        elif j==2: #百位
            if i[j]=='0' and i[1]!='0': #百位为0，十位不为0
                b.append(d['0'])
            elif i[j]!='0':
                b.append('bai') #值为2就是二百
                b.append(d[i[j]])
        elif j==3: #千位
            if i[j]!='0': #千位不为0时
                b.append('qian')
                b.append(d[i[j]])
            elif i[j]=='0' and i[2]!='0': #千位为0，百位不为0
                b.append(d['0'])


while n!='': #倒着取数，每四位为一组字符串加到a列表，当不足四位后结束循环
    if len(n)>=4: #如果n的长度大于等于4
        s=n[-4:] #取后四位
        n=n[:-4] #删除后四位; [:-4]的意思是除掉后四位取全部
        a.append(s)
    else:
        a.append(n)
        n='' #结束循环
for i in range(len(a)):
    if i==0:
        numexchange(a[i])
    elif i==1:
        b.append('wan')
        numexchange(a[i])
    elif i==2:
        b.append('yi')
        numexchange(a[i])
for i in range(len(b)-1,-1,-1): #从尾部到头部进行循环
    if i == len(b)-1: #从尾部开始时
        print(b[i],end='') #因为开始时不需要空格
    else:
        print(' %s'%(b[i]),end='') #将%后面的东西赋到%s里，注意' %s'，在%s前边有空格
