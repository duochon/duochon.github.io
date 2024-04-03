from urllib.request import urlopen
from bs4 import BeautifulSoup as bs4s

html = urlopen("http://pythonscraping.com/pages/warandpeace.html")
bs = bs4s(html.read(), "html.parser")


# print(bs)

# nameList = bs.find_all('span', {'class':'green'})
# for name in nameList:
# 	print(name.get_text())

# nameList = bs.find_all(text='the prince')
# print(nameList)

title = bs.find_all(class_='green')

for i in title:
	print(i)