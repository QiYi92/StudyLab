# #数据保存
#
#
# f=xlwt.Workbook(encoding='utf-8')
#     sheet01=f.add_sheet(u'sheet1',cell_overwrite_ok=True)
#     sheet01.write(0,0,'name') #第一行第一列
#     sheet01.write(0,1,'score')
#     sheet01.write(0,2,'price')
#     sheet01.write(0,3,'recommand_ratio')
#     sheet01.write(0,4,'people_num')
#     sheet01.write(0,5,'location')
#     #写内容
#     for i in range(len(DATA)):
#         sheet01.write(i+1,0,DATA[i]['name'])
#         sheet01.write(i+1,1,DATA[i]['score'])
#         sheet01.write(i+1,2,DATA[i]['price'])
#         sheet01.write(i+1,3,DATA[i]['recommend_ratio'])
#         sheet01.write(i+1,4,DATA[i]['people_num'])
#         sheet01.write(i+1,5,DATA[i]['location'])
#     f.save(u'E:\\猫眼电影.xls')

urls = ['https://s.taobao.com/search?q=口红s={}'.format(i*44) for i in range（1,11）]