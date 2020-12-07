# # -*- coding: UTF-8 -*-
# from urllib import request
#
# if __name__ == "__main__":
#     req = request.Request("http://fanyi.baidu.com/")
#     response = request.urlopen(req)
#     html = response.read()
#     html = html.decode("utf-8")
#     print(html)



# -*- coding: UTF-8 -*-
# from urllib import request
#
# if __name__ == "__main__":
#     req = request.Request("http://fanyi.baidu.com/")
#     response = request.urlopen(req)
#     print("geturl打印信息：%s"%(response.geturl()))
#     print('**********************************************')
#     print("info打印信息：%s"%(response.info()))
#     print('**********************************************')
#     print("getcode打印信息：%s"%(response.getcode()))

import urllib.request
import urllib.error

req = urllib.request.Request('http://blog.csdn.net/cqcre')
try:
    urllib.request.urlopen(req)
except urllib.error.URLError as e:
    if hasattr(e, "reason"):
        print(e.reason) #获取错误原因 (e.code获取错误代码)
else:
    print("OK")