# 네이버 웹톤 목록 Crawling
import urllib.request
from bs4 import BeautifulSoup

url = "http://comic.naver.com/webtoon/list.nhn?titleId=20853&weekday=fri"
data = urllib.request.urlopen(url);
soup = BeautifulSoup(data, 'html5lib')

#웹툰 제목 찾기
cartoons = soup.findAll('td', attrs={'class':'title'})

for item in cartoons:
    title = item.find('a').text
    print(title)