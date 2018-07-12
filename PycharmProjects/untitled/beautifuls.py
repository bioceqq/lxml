from bs4 import BeautifulSoup
import re
html ='''
<html><head><title>The Dormouse's story</title></head>
<body>
        <p class="title" name="dromouse"><b>The Dormouse's story</b></p>
        <p class="story">Once upon a time there were three little sisters; and their names were
        <a href="http://example.com/elsie" class="sister" id="link1"><!-- Elsie --></a>,
        <a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
        <a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
        and they lived at the bottom of a well.</p>
<p class="story">...</p>
'''
#创建BeautifulSoup对象
soup = BeautifulSoup(html,"lxml")
# print(soup.prettify())
#直接获取标签内容，不需要正则表达式
print(soup.head)
print(soup.title)
print(soup.head.name)
print(soup.p.attrs)
print(soup.p.string)#如果一个标签里面没有标签了，那么 .string 就会返回标签里面的内容。如果标签里面只有唯一的一个标签了，那么 .string 也会返回最里面的内容。
#如果tag包含了多个子节点,tag就无法确定，string 方法应该调用哪个子节点的内容, .string 的输出结果是 None
print(type(soup.p.string))#可遍历的字符串bs4.element.NavigableString
print(soup.head.children)#children不是list，所以需要遍历打印
for child in soup.head.children:
    print(child)
for child1 in soup.descendants:#descendants是打印所有的子孙节点
    print(child1)
f1 = soup.find_all("p")
print("这是找出来的p",f1)
for tag in soup.find_all(re.compile("^b")):
    print(tag.name)
    for tag1 in soup.find_all(True):
        print(tag1.name)
