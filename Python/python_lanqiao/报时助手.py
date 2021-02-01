# 创建字典
Time={'0':'zero','1':'one','2':'two','3':'three','4':'four','5':'five','6':'six',\
      '7':'seven','8':'eight','9':'nine','10':'ten','11':'eleven','12':'twelve',\
      '13':'thirteen','14':'fourteen','15':'fifteen','16':'sixteen','17':'seventeen',\
      '18':'eighteen','19':'nineteen','20':'twenty','30':'thirty','40':'forty','50':'fifty'}
nowtime=list(map(int,input().split())) # 输入hour,minute添加到nowtime
for i in range(len(nowtime)):
    if nowtime[1]==0: # 当输入minute为0时，也就是整点(列表从0开始)
        print(Time[str(nowtime[i])]+" o'clock")
        break
    elif nowtime[i]<=20 or nowtime[i]%10==0: # 当值比20小或者为整数时直接转换输出
        print(Time[str(nowtime[i])],end=' ')
    else:
        # 大于20的数且不为整的数不在字典内，所以需减去个位，转换完成后再加上个位
        print(Time[str(nowtime[i]-nowtime[i]%10)] +' '+ Time[str(nowtime[i]%10)],end=' ')
