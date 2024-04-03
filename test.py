from urllib.request import urlopen
from bs4 import BeautifulSoup as bs4s

html = urlopen('https://travel.state.gov/content/travel/en/legal/visa-law0/visa-bulletin/2023/visa-bulletin-for-october-2022.html')
bs = bs4s(html.read(), "html.parser")

	# Tim cac bang trong trang visa bulletin
tables = bs.find_all('table')

	# Tim bang B - Date for Filing
eb = tables[8].find_all('td')
clean = []

for i in range(len(eb)):
	clean.append(eb[i].get_text())

a = clean.index('Other Workers')

print(a)

print(clean[a+1])

# a = "<td>Other Workers</td>"
# b = eb.index(a)
# # print(eb[28])
# print(b)

# if a in eb:
# 	b = eb.index(a)
# 	print(b)

# 	# Lay thong tin thang va nam
# month = bs.title.get_text()

# 	# Lay thong tin eb3 unskill - chuyen dien
# eb3_unskill = eb[25].get_text()

# print(month,':',eb3_unskill)
