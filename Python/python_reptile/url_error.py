# # -*- coding: UTF-8 -*-
# from urllib import request
# from urllib import error
#
# if __name__ == "__main__":
#     #一个不存在的连接
#     url = "http://www.iloveyou.com/"
#     req = request.Request(url)
#     try:
#         response = request.urlopen(req)
#         html = response.read().decode('utf-8')
#         print(html)
#     except error.URLError as e:
#         print(e.reason)

# -*- coding: UTF-8 -*-
# from urllib import request
# from urllib import error
#
# if __name__ == "__main__":
#     #一个不存在的连接
#     url = "http://www.mcbbs.net/Jack_Cui.html"
#     req = request.Request(url)
#     try:
#         responese = request.urlopen(req)
#         # html = responese.read()
#     except error.HTTPError as e:
#         print(e.code)

# -*- coding: UTF-8 -*-
from urllib import request
from urllib import error

if __name__ == "__main__":
    #一个不存在的链接
    url = "http://www.mcbbs.net/jack_gui.html"
    req = request.Request(url)
try:
    responese = request.urlopen(req)
except error.HTTPError as e:
    print("HTTPError") # 先HTTP
    print(e.code)
except error.URLError as e:
    print("URLError") # 后URL
    print(e.reason)
