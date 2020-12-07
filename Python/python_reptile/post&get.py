# import urllib.request as urllib2
# import urllib.parse
# import urllib
#
# values = {"username":"xxxxxx@qq.com","password":"xxxx"}
# data = urllib.parse.urlencode(values)
# url = "https://passport.csdn.net/account/login?from=http://my.csdn.net/my/mycsdn"
# # 以csdn为例
# request = urllib.request.Request(url,data)
# response = urllib.request.urlopen(request)
# print(response.read())

# import urllib
# import urllib.parse
# import urllib.request as urllib2
#
# values = {}
# values['username'] = "1016903103@qq.com"
# values['password'] = "XXXX"
# data = urllib.parse.urlencode(values)
# url = "http://passport.csdn.net/account/login?from=http://my.csdn.net/my/mycsdn"
# request = urllib2.Request(url, data)
# response = urllib2.urlopen(request)
# print(response.read())


# import urllib.parse
# import urllib.request as urllib2
#
# values = {}
# values['username'] = "xxxxxxx@qq.com"
# values['password'] = "XXXX"
# data = urllib.parse.urlencode(values)
# url = "http://passport.csdn.net/account/login"
# geturl = url + "?" + data
# request = urllib2.Request(geturl)
# response = urllib2.urlopen(request)
# # print(response.read())
# print(geturl)

# import urllib.parse
# import urllib.request
#
#
# url = 'http://www.server.com/login'
# user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
# values = {'username': 'cqc', 'password': 'XXXX'}
# headers = {'User-Agent': user_agent}
# data = urllib.parse.urlencode(values)
# request = urllib.request.Request(url, data, headers)
# response = urllib.request.urlopen(request)
# page = response.read()

# import urllib.request
#
# enable_proxy = True
# proxy_handler = urllib.request.ProxyHandler({"http":'http://代理网站.com:8080'})
# null_proxy_handler = urllib.request.ProxyHandler({})
# if enable_proxy:
#     opener = urllib.request.build_opener(proxy_handler)
# else:
#     opener = urllib.request.build_opener(null_proxy_handler)
# urllib.request.install_opener(opener)
#
# import urllib.request
# response = urllib.request.urlopen('http://www.baidu.com',data, 10)
#
#
# import urllib.request
# request = urllib.request.Request(url, data=data)
# request.get_method = lambda: 'PUT' # or 'DELETE'
# response = urllib.request.urlopen(request)