from urllib.request import urlopen
from bs4 import BeautifulSoup as bs4s

html = urlopen("http://pythonscraping.com/pages/page3.html")
bs = bs4s(html.read(), "html.parser")

# print(bs.table.tr.get_text())

# print(bs.find('table',{'id':'giftList'}).children)

# for sibling in bs.table.tr:
# 	print(sibling)

# for sibling in bs.find('table',{'id':'giftList'}).tr:
# 	print(sibling)

# print(bs.find('img',{'src':'../img/gifts/img1.jpg'}).parent.previous_sibling.get_text( ))

for im in bs.find('img').parent:
	print(im)