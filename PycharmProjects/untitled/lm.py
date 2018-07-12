# from lxml import etree

from lxml import etree
text = '''
<div>
    <ul>
         <li class="item-0"><a href="link1.html">first item</a></li>
         <li class="item-1"><a href="link2.html">second item</a></li>
         <li class="item-inactive"><a href="link3.html">third item</a></li>
         <li class="item-1"><a href="link4.html"><span class="bold">fourth item</a></li>
         <li class="item-0"><a href="link5.html">fifth item</a>
     </ul>
</div>
'''
html1= etree.parse("hello.html")
# result = etree.tostring(html1,pretty_print=True)
# print(html1)
# print(type(html1))
html = etree.HTML(text)
result = etree.tostring(html)
xp = html.xpath("//li/@class")
xp1 = html.xpath("//li//span")#span不是li下的子元素，所以要用“//”
result1 = html.xpath('//li/a//@class')
result2 = html.xpath('//li[last()-1]/a')
print(result2[0].text)
# print (result1)
# print(xp,xp1)