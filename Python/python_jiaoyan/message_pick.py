#coding:utf-8
x=input('请输入你的18位身份证号：')
e=int(x[:17])
if e<11111111111111111:
    print('输入有误，请输入正确的18位身份证！')
elif e>99999999999999999:
    print('输入有误，请输入正确的18位身份证！')
else:
    a=e//1000000000000000
    b=e%10
    c=e%100000000000//10000000
    month=e%10000000//100000
    day=e%100000//1000
    d={11:'北京市',12:'天津市',13:'河北省',14:'山西省',15:'内蒙古自治区',21:'辽宁省',22:'吉林省',23:'黑龙江省',31:'上海市',32:'江苏省',33:'浙江省',34:'安徽省',35:'福建省',36:'江西省',37:'山东省',41:'河南省',42:'湖北省',43:'湖南省',44:'广东省',45:'广西壮族自治区',46:'海南省',50:'重庆市',51:'四川省',52:'贵州省',53:'云南省',54:'西藏自治区',61:'陕西省',62:'甘肃省',63:'青海省',64:'宁夏回族自治区',65:'新疆维吾尔自治区',71:'台湾省',81:'香港特别行政区',91:'澳门特别行政区'}
    if(month>12 or month<1 or day>31 or day<1):
        print('输入有误，请输入正确的18位身份证！')
    else:
        print("该身份证号码属于{}".format(d.get(a)))
        print('号主出生{}年{}月{}日'.format(c,month,day))
        if (b% 2) == 0:
            print('号主性别为女')
        else:
            print('号主性别为男')
        s= {0:'鼠',1:'牛',2:'虎',3:'兔',4:'龙',5:'蛇',6:'马',7:'羊',8:'猴',9:'鸡',10:'狗',11:'猪'}
        print('号主生肖是{}'.format(s[(c-1972)%12]))
        m=['水瓶座','双鱼座','白羊座','金牛座','双子座','巨蟹座','狮子座','处女座','天秤座','天蝎座','射手座','魔蝎座']
        y=(20,19,21,20,21,22,23,23,23,24,23,22)
        month = month-1
        if  day>y[month]:
            print("号主星座是{}".format(m[month]))
        else :
             print("号主星座是{}".format(m[month-1]))
