# 클리앙 계시판 Crawling
import urllib.request
from bs4 import BeautifulSoup

url = 'http://www.clien.net/cs2/bbs/board.php?bo_table=use'
response = urllib.request.urlopen(url)
# 대부분의 국내 웹사이트는 utf-8방식으로 저장된다
page = response.read().decode('utf-8', 'ignore')
soup = BeautifulSoup(page, 'html5lib')
list = soup.findAll('td', attrs={'class':'post_subject'})

for idx, item in enumerate(list):
    if idx <= 1:
        # 헤더는 제외
        continue
    try:
        title = item.find('a').text
        print(title)
    except:
        print('error')