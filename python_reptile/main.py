# import urllib.request
#
# request = urllib.request.Request("https://blog.csdn.net/xixi880928/article/details/78339157")
# response = urllib.request.urlopen(request)
# print(response.read())

# import requests
# import re
#
# url='https://maoyan.com/board/4?'
# headers={
#         "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36"
#         }
#
# def get_page(url):
#     # 伪装&发送请求
#     try:
#         response = requests.get(url,headers=headers)
#         if response.status_code==200:
#             return response.text
#     except Exception as e:
#         # 获取异常信息
#         print(e)
#
# def get_info(page):
#     items=re.findall('board-index .*?>(\d+)</i>.*?class="name"><.*?>(.*?)</a></p>',page,re.S)
#     for item in items:
#         data={}
#         data['rank']=item[0]
#         data['title']=item[1]
#         print(data)
#
# urls=['https://maoyan.com/board/4?offset={}'.format(i*10) for i in range(10)]
# DATA=[]
# for url in urls:
#     page=get_page(url)
#     datas=get_info(page)
#     for data in datas:
#         DATA.append(data)
# # 将所有数据添加到DATA里

import requests
import re
import xlwt

url = 'https://maoyan.com/board/4?'
headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36"
}


def get_page(url):
    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            return response.text
        else:
            print('获取网页失败')
    except Exception as e:
        print(e)


def get_info(page):
    items = re.findall('board-index .*?>(\d+)</i>.*?class="name"><.*?>(.*?)</a></p>.*?<p class="star">.*?' +
                       '主演：(.*?) .*?</p>.*?<p class="releasetime">(.*?)</p>.*?<p class="score"><i class="integer">' +
                       '(.*?)</i><i class="fraction">(\d+)</i></p>', page, re.S)
    for item in items:
        data = {}
        data['rank'] = item[0]
        data['title'] = item[1]
        actors = re.sub('\n', '', item[2])
        data['actors'] = actors
        data['date'] = item[3]
        data['score'] = str(item[4]) + str(item[5])
        yield data


urls = ['https://maoyan.com/board/4?offset={}'.format(i * 10) for i in range(10)]
DATA = []
for url in urls:
    page = get_page(url)
    datas = get_info(page)
    for data in datas:
        DATA.append(data)  # 将所有的数据添加到DATA里

f = xlwt.Workbook(encoding='utf-8')
sheet01 = f.add_sheet(u'sheet1', cell_overwrite_ok=True)
sheet01.write(0, 0, 'rank')  # 第一行第一列
sheet01.write(0, 1, 'title')
sheet01.write(0, 2, 'actors')
sheet01.write(0, 3, 'date')
sheet01.write(0, 4, 'score')
# 写内容
for i in range(len(DATA)):
    sheet01.write(i + 1, 0, DATA[i]['rank'])
    sheet01.write(i + 1, 1, DATA[i]['title'])
    sheet01.write(i + 1, 2, DATA[i]['actors'])
    sheet01.write(i + 1, 3, DATA[i]['date'])
    sheet01.write(i + 1, 4, DATA[i]['score'])
    print('p', end='')
f.save('E:\\猫眼电影.xls')