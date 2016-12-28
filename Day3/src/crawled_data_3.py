from bs4 import BeautifulSoup
import urllib.request
import re 

# Clien 계시판 페이지 1~6 중에서 청와대 키워드로 Data Crawling
hdr = {'User-agent':'Mozila/5.0 (compatible; MSIE 5.5; Windows NT)'}
for n in range(1,6):
	data ='http://www.clien.net/cs2/bbs/board.php?bo_table=park&page=' + str(n)
	req = urllib.request.Request(data, headers = hdr)
	data = urllib.request.urlopen(req).read()
	page = data.decode('utf-8', 'ignore')
	soup = BeautifulSoup(page, 'html5lib')
	list = soup.findAll('td', attrs={'class':'post_subject'})

	for item in list:
		try:
			title = item.find('a').text
			if (re.search('윈도우', title)):
				print(title)
		except:
			pass