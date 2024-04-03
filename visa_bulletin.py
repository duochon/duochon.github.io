from urllib.request import Request, urlopen
from urllib.error import URLError, HTTPError
from bs4 import BeautifulSoup as bs4s

# 2021
nam_2021 = ['october-2020','november-2020','december-2020','january-2021','february-2021','march-2021','april-2021','may-2021','june-2021','july-2021','august-2021','september-2021']
# 2022
nam_2022 = ['october-2021','november-2021','december-2021','january-2022','february-2022','march-2022','april-2022','may-2022','june-2022','july-2022','august-2022','september-2022']
# 2023
nam_2023 = ['october-2022','november-2022','december-2022','january-2023','february-2023','march-2023','april-2023','may-2023','june-2023','july-2023','august-2023','september-2023']
# 2024
nam_2024 = ['october-2023','november-2023','december-2023','january-2024','february-2024','march-2024','april-2024','may-2024','june-2024','july-2024','august-2024','september-2024']

# Change year here
fiscal_year = nam_2021
 

# Extract and find current year to input into URL
raw_year = fiscal_year[0]
year = int(raw_year[-4:]) + 1

# Check month by month in the year
try:
	for i in fiscal_year:
		thang = i
		url_1 = 'https://travel.state.gov/content/travel/en/legal/visa-law0/visa-bulletin/'
		url_2 = str(year)
		url_3 = '/visa-bulletin-for-'
		url_4 = '.html'
		url = url_1 +  url_2 + url_3 + thang + url_4

		html = urlopen(url)
		bs = bs4s(html.read(), "html.parser")

		# Tim cac bang trong trang visa bulletin
		tables = bs.find_all('table')

		# Lay thong tin thang va nam
		month = bs.title.get_text()

		# Tim bang B - Date for Filing
		eb = tables[8].find_all('td')

		# Clean tag trong list eb
		clean = []
		for i in range(len(eb)):
			clean.append(eb[i].get_text())

		# Tim vi tri index cua 'Other Workers'

		vitri = clean.index('Other Workers')
		
		# Lay thong tin eb3 unskill - chuyen dien
		eb3_unskill = clean[vitri + 1]

		print(month,':',eb3_unskill)

except HTTPError as e:
    # do something
    print('Coming Month: ', 'Opps...Not Released Yet')
except URLError as e:
    # do something
    print('Reason: ', e.reason)
	


