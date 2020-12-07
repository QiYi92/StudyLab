# import urllib.request
# import http.cookiejar
# # 声明一个CookieJar对象实例来保存cookie
# cookie = http.cookiejar.CookieJar()
# # 利用urllib2库的HTTPCookieProcessor对象来创建cookie处理器
# handler = urllib.request.HTTPCookieProcessor(cookie)
# # 通过handler来构建opener
# opener = urllib.request.build_opener(handler)
# # 此处的open方法同urllib2的urlopen方法，也可以传入request
# response = opener.open('http://www.baidu.com')
# for item in cookie:
#     print('Name = '+item.name)
#     print('Value = '+item.value)

# import http.cookiejar
# import urllib.request
#
# # 设置保存cookie的文件，同级目录下的cookie.txt
# filename = 'cookie.txt'
# # 声明一个MozillaCookieJar对象实例来保存cookie，之后写入文件
# cookie = http.cookiejar.MozillaCookieJar(filename)
# # 利用urllib2库的HTTPCookieProcessor对象来创建cookie处理器
# handler = urllib.request.HTTPCookieProcessor(cookie)
# # 通过handler来构建opener
# opener = urllib.request.build_opener(handler)
# # 创建一个请求，原理同urllib2的urlopen
# response = opener.open("http://www.baidu.com")
# # 保存cookie到文件
# cookie.save(ignore_discard=True, ignore_expires=True)

# import http.cookiejar
# import urllib.request
#
# # 创建MozillaCookieJar实例对象
# cookie = http.cookiejar.MozillaCookieJar()
#
# # 从文件中读取cookie内容到变量
# cookie.load('cookie.txt', ignore_discard=True, ignore_expires=True)
#
# # 创建请求的request
# req = urllib.request.Request("http://www.baidu.com")
#
# # 利用urllib2的build_opener方法创建一个opener
# opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cookie))
#
# response = opener.open(req)
# print(response.read())


# -*- coding: UTF-8 -*-

import urllib.parse
import urllib.request
import http.cookiejar

filename = 'cookie.txt'
# 声明一个MozillaCookieJar对象实例来保存cookie，之后写入文件
cookie = http.cookiejar.MozillaCookieJar(filename)
opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cookie))
postdata = urllib.parse.urlencode({
    'login': '20192344011',
    'pwd': '123456'
})
postdata = urllib.parse.urlencode(postdata).encode('utf-8')
# 登录教务系统的URL
loginUrl = 'http://jwxt.sdu.edu.cn:7890/pls/wwwbks/bks_login2.login'
# 模拟登录，并把cookie保存到变量
result1 = opener.open(loginUrl, postdata).decode('utf-8')
# 保存cookie到cookie.txt中
cookie.save(ignore_discard=True, ignore_expires=True)
# 利用cookie请求访问另一个网址，此网址是成绩查询网址
gradeUrl = 'http://jwxt.sdu.edu.cn:7890/pls/wwwbks/bkscjcx.curscopre'
# 请求访问成绩查询网址
result2 = opener.open(gradeUrl)
print(result2.read())
