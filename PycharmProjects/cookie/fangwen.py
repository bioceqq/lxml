#从保存的文件中读取cookie,并访问网站
from urllib import request
from  urllib import parse
from http import cookiejar

cookie = cookiejar.MozillaCookieJar()
cookie.load("cookie.txt",ignore_expires=True,ignore_discard=True)
req = request.Request("http://www.baidu.com")
opener = request.build_opener(request.HTTPCookieProcessor(cookie))
response = opener.open(req)
print(response.read())