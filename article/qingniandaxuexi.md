---
title: 青年大学习完成截图爬虫
date: 
author: galileocat
img: 
top: false
cover: false
coverImg: 
password: 
toc: false
mathjax: false
summary: 青年大学习完成截图爬虫
categories: Python
tags:
  - Python
  - 爬虫
---
青年大学习截图爬虫脚本

1.自动爬取青年大学习完成截图

2.该脚本无法对微信记录进行修改，只能生成最新期的截图

3.直接下载.exe文件运行即可，脚本会在同目录下生成截图.jpg文件
![](https://cdn.jsdelivr.net/gh/QiYi92/ImageHost/img/202108072043652.jpeg)
[Github项目地址](https://github.com/QiYi92/Youth_Learning_Reptile)
[Github下载地址](https://github.com/QiYi92/Youth_Learning_Reptile/releases)

### 核心源码
```python
#中青报主页
    url = 'http://news.cyol.com/node_67071.htm'
    #发送get请求,获取网页
    response = requests.get(url, verify=False)
    print("响应状态%d"%response.status_code)
    #解析网页
    html = etree.HTML(response.text)
    newest = html.xpath('/html/body/div[@class="mianbody"]/dl[@class="listMM"]/dd[@class="picB"]/ul[@class="movie-list"]/li[1]/a/@href')[0]
    img_path = newest.replace('m.html', 'images/end.jpg').replace('index.html', 'images/end.jpg')
```
