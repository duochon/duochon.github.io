from urllib.request import Request, urlopen
from urllib.error import URLError, HTTPError
from bs4 import BeautifulSoup as bs4s
import datetime
import csv

print('\nPhần mềm kiểm tra Visa Bulletin (bắt đầu từ năm 2016)')
print('o0o Coded by Hon Tran v1 o0o----\n')
print('Vui lòng chọn:\n')
print('1/ Hồ sơ Truyền thống')
print('2/ Hồ sơ Chuyển diện')
selection = int(input('\nTruyền thống gõ 1, Chuyển diện gõ 2, sau đó nhấn Enter: '))

if (selection == 1):
	choice = int(input('Nhập năm tài khóa cần kiểm tra: '))
	print('Đang lấy dữ liệu Truyền thống...')
	print('Xin chờ vài phút nha...')
	nam_truoc = choice - 1 
	october = 'october' + '-' + str(nam_truoc)
	november = 'november' + '-' + str(nam_truoc)
	december = 'december' + '-' + str(nam_truoc)
	january = 'january' + '-' + str(choice)
	february = 'february' + '-' + str(choice)
	march = 'march' + '-' + str(choice)
	april = 'april' + '-' + str(choice)
	may = 'may' + '-' + str(choice)
	june = 'june' + '-' + str(choice)
	july = 'july' + '-' + str(choice)
	august = 'august' + '-' + str(choice)
	september = 'september' + '-' + str(choice)

	fiscal_year = [october,november,december,january,february,march,april,may,june,july,august,september]
	year = choice

	# Tao file theo ngay gio
	file_gio = datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
	file_tao = str(file_gio) + "_" + str(year) + "_truyenthong" + ".csv"

	with open(file_tao, 'w') as output_csv:
		header = "Queried time,Fiscal year,Month,Priority Date\n"
		output_csv.write(header)
	  
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

			# Lay thong tin thang va nam
			month = bs.title.get_text()

			# Tim cac bang trong trang visa bulletin
			tables = bs.find_all('table')

			# Tim bang B - Date for Filing
			# eb = tables[8].find_all('td')

			# Find employment table
			tables_new = []

			for table in tables:
				if table.td.get_text().startswith('Employment'):
					tables_new.append(table)

			# List tables_new gom 2 bang truyen thong va chuyen dien

			truyenthong = tables_new[0].find_all('td')
			chuyendien = tables_new[1].find_all('td')

			# Clean tag trong list  va gan vo list clean[]
			clean_chuyendien = []
			clean_truyenthong = []

			for i in range(len(chuyendien)):
				clean_chuyendien.append(chuyendien[i].get_text())
			
			for i in range(len(truyenthong)):
				clean_truyenthong.append(truyenthong[i].get_text())

			# Tim vi tri index cua 'Other Workers'
			vitri_chuyendien = clean_chuyendien.index('Other Workers')
			vitri_truyenthong = clean_truyenthong.index('Other Workers')
			
			# Lay thong tin eb3 unskill - chuyen dien
			eb3_unskill_chuyendien = clean_chuyendien[vitri_chuyendien + 1]
			eb3_unskill_truyenthong = clean_truyenthong[vitri_truyenthong + 1]

			# print(str(gio),month,':',eb3_unskill)
			record = str(gio) + ',' + str(choice) + ',' + month[18:] + ',' + eb3_unskill_truyenthong

			# Ghi file
			with open(file_tao, 'a', newline='') as output_csv:  
				output_csv.write(record+'\n')

	except HTTPError as e:
	    # do something
	    # print('Coming Month: ', 'Opps...Not Released Yet')
		error = "Coming Month: Opps...Not Released Yet"
		with open(file_tao, 'a', newline='') as output_csv:  
			output_csv.write(error+'\n')

	except URLError as e:
	    # do something
	    print('Reason: ', e.reason)

	bye = "\nHoàn thành. Dữ liệu lưu ở file tên là " + file_tao
	print(bye)

else:
	print('Đang lấy dữ liệu Chuyển diện - AOS...')
	print('Xin chờ vài phút nha...')

	file_gio = datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
	file_tao = str(file_gio) + "_chuyendien-aos" + ".csv"

	with open(file_tao, 'w') as output_csv:
		header = "Queried time,Month,Priority Date\n"
		output_csv.write(header)
	 

	# Check month by month in the year
	try:
		for i in range(0,200):
			# i = 0 --- Feb-2016
			# i = 200 --- Sep-2032
			
			url_1 = 'https://www.uscis.gov/green-card/green-card-processes-and-procedures/visa-availability-priority-dates/when-to-file-your-adjustment-of-status-application-for-family-sponsored-or-employment-based-'
			url_2 = url_1 + str(i)
			html = urlopen(url_2)
			bs = bs4s(html.read(), "html.parser")

			# Lay thong tin current time
			gio = datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S")

			# Lay thong tin thang va nam
			month = bs.title.get_text()

			# Tim cac bang trong trang
			tables = bs.find_all('table')

			if len(tables) == 2:
				table = tables[1]
			else:
				table = tables[len(tables)-1]


			# Tim bang B - Date for Filing
			# eb = tables[8].find_all('td')

			# Find employment table
			for employee_data in table.find_all('tbody'):
				rows = employee_data.find_all('tr')

			# Chon dong Other Worker
			eb3 = rows[3].find_all('td')
			vidu = eb3[0].get_text().strip()
			select = ''
			if vidu == 'Other Workers':
				select = eb3[1].get_text().strip()
			else:
				select = vidu

			# print(str(gio),month,':',eb3_unskill)
			record = gio + ',' + month[110:-8]+ ',' + select

			# Ghi file
			with open(file_tao, 'a', newline='') as output_csv:  
				output_csv.write(record+'\n')

	except HTTPError as e:
	    # do something
	    # print('Coming Month: ', 'Opps...Not Released Yet')
		error = "Coming Month: Opps...Not Released Yet"
		with open(file_tao, 'a', newline='') as output_csv:  
			output_csv.write(error+'\n')

	except URLError as e:
	    # do something
	    print('Reason: ', e.reason)

	bye = "\nHoàn thành. Dữ liệu lưu ở file tên là " + file_tao
	print(bye)
