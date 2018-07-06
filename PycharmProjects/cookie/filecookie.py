from urllib import request
from urllib import parse
from http import cookiejar
filename = "cookie.txt"
cookie = cookiejar.MozillaCookieJar(filename)
handler = request.HTTPCookieProcessor(cookie)
opener = request.build_opener(handler)
reponse = opener.open("http://baidu.com")
cookie.save(ignore_discard=True,ignore_expires=True)