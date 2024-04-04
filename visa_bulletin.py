from urllib.request import Request, urlopen
from urllib.error import URLError, HTTPError
from bs4 import BeautifulSoup as bs4s
import datetime

# 2014
nam_2014 = ['october-2013','november-2013','december-2013','january-2014','february-2014','march-2014','april-2014','may-2014','june-2014','july-2014','august-2014','september-2014']
# 2015
nam_2015 = ['october-2014','november-2014','december-2014','january-2015','february-2015','march-2015','april-2015','may-2015','june-2015','july-2015','august-2015','september-2015']
# 2016
nam_2016 = ['october-2015','november-2015','december-2015','january-2016','february-2016','march-2016','april-2016','may-2016','june-2016','july-2016','august-2016','september-2016']
# 2017
nam_2017 = ['october-2016','november-2016','december-2016','january-2017','february-2017','march-2017','april-2017','may-2017','june-2017','july-2017','august-2017','september-2017']
# 2018
nam_2018 = ['october-2017','november-2017','december-2017','january-2018','february-2018','march-2018','april-2018','may-2018','june-2018','july-2018','august-2018','september-2018']
# 2019
nam_2019 = ['october-2018','november-2018','december-2018','january-2019','february-2019','march-2019','april-2019','may-2019','june-2019','july-2019','august-2019','september-2019']
# 2020
nam_2020 = ['october-2019','november-2019','december-2019','january-2020','february-2020','march-2020','april-2020','may-2020','june-2020','july-2020','august-2020','september-2020']
# 2021
nam_2021 = ['october-2020','november-2020','december-2020','january-2021','february-2021','march-2021','april-2021','may-2021','june-2021','july-2021','august-2021','september-2021']
# 2022
nam_2022 = ['october-2021','november-2021','december-2021','january-2022','february-2022','march-2022','april-2022','may-2022','june-2022','july-2022','august-2022','september-2022']
# 2023
nam_2023 = ['october-2022','november-2022','december-2022','january-2023','february-2023','march-2023','april-2023','may-2023','june-2023','july-2023','august-2023','september-2023']
# 2024
nam_2024 = ['october-2023','november-2023','december-2023','january-2024','february-2024','march-2024','april-2024','may-2024','june-2024','july-2024','august-2024','september-2024']


print('Phần mềm kiểm tra Visa Bulletin - dành cho Chuyển Diện (2014-2024)')
print('(Coded by Hon Tran - 20240404)\n')

fiscal_year = []

choice = str(input('Nhập năm tài khóa cần kiểm tra: '))
print('Xin chờ 1 chút nha...')


if choice == '2024':
    fiscal_year = nam_2024
elif choice == '2023':
    fiscal_year = nam_2023
elif choice == '2022':
    fiscal_year = nam_2022
elif choice == '2021':
    fiscal_year = nam_2021
elif choice == '2020':
    fiscal_year = nam_2020
elif choice == '2019':
    fiscal_year = nam_2019
elif choice == '2018':
    fiscal_year = nam_2018
elif choice == '2017':
    fiscal_year = nam_2017
elif choice == '2016':
    fiscal_year = nam_2016
elif choice == '2015':
    fiscal_year = nam_2015
elif choice == '2014':
    fiscal_year = nam_2014

# Change year here
# fiscal_year = nam_2022

# Extract and find year to input into URL
raw_year = fiscal_year[0]
year = int(raw_year[-4:]) + 1

# Tao file theo ngay gio
file_gio = datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
file_tao = str(file_gio) + "_" + str(year) + ".txt"

# Check month by month in the year
try:
	for i in fiscal_year:
		
		# Lay ten thang de input vao URL
		thang = i
		url_1 = 'https://travel.state.gov/content/travel/en/legal/visa-law0/visa-bulletin/'
		
		# Nam tai khoa
		url_2 = str(year)
		url_3 = '/visa-bulletin-for-'
		url_4 = '.html'
		
		# Final URL
		url = url_1 +  url_2 + url_3 + thang + url_4

		html = urlopen(url)
		bs = bs4s(html.read(), "html.parser")

		# Lay thong tin current time
		gio = datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S")

		# Tim cac bang trong trang visa bulletin
		tables = bs.find_all('table')

		# Lay thong tin thang va nam
		month = bs.title.get_text()

		# Tim bang B - Date for Filing
		eb = tables[8].find_all('td')

		# Clean tag trong list eb va gan vo list clean[]
		clean = []
		for i in range(len(eb)):
			clean.append(eb[i].get_text())

		# Tim vi tri index cua 'Other Workers'
		vitri = clean.index('Other Workers')
		
		# Lay thong tin eb3 unskill - chuyen dien
		eb3_unskill = clean[vitri + 1]

		# print(str(gio),month,':',eb3_unskill)
		record = str(gio) + ',' + month + ',' + eb3_unskill

		# Ghi file
		with open(file_tao, 'a') as text_file:  
			text_file.write(record+'\n')

except HTTPError as e:
    # do something
    # print('Coming Month: ', 'Opps...Not Released Yet')
	error = "Coming Month: Opps...Not Released Yet"
	with open(file_tao, 'a') as text_file:  
		text_file.write(error+'\n')

except URLError as e:
    # do something
    print('Reason: ', e.reason)

bye = "\nHoàn thành. Dữ liệu lưu ở file tên là " + file_tao
print(bye)


	


