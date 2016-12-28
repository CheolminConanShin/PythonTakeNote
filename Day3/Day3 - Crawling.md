
### Beautifulsoup4 설치 방법
```
pip install setuptools --upgrade
pip install beautifulsoup4
pip install --upgrade html5lib==1.0b8
```
beautifulsoup4 설치 후 재부팅 필요할 수 있음


### 네이버 웹톤 목록 Crawling
```python
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
```

### Sample Data Crawling
다양한 방법으로 Data parsing하기
```python
from bs4 import BeautifulSoup
import re
doc = ['<html><head><title>Page title</title></head>',
'<body><p id="firstpara" align="center">This is paragraph <b>one</b>',
'<p id="secondpara" align="blah">This is a paragraph <b>two</b>',
'</html>']
soup = BeautifulSoup(''.join(doc), 'html5lib')
print(soup.prettify())

# all b tags
print(soup.findAll('b'))
# tag names starting with 'b'
tags_starting_with_b = soup.findAll(re.compile('^b'))
print([tag.name for tag in tags_starting_with_b])
# title and p tags
print(soup.findAll(['title', 'p']))
# tags having more than 2 attributes
print(soup.findAll(lambda tag : len(tag.attrs) == 2))
# id ends with para
print(soup.findAll(id=re.compile('para$')))
# b tags with class name lime
print(soup.findAll('b'), {"class":"lime"})
```

### Add / Change Attributes of Tags
데이터 속성 수정
```python
from bs4 import BeautifulSoup
soup = BeautifulSoup("<b id='2'>연습</b>", "html5lib")
print(soup) # <html><head></head><body><b id="2">연습</b></body></html>
b = soup.b
# Change id of a 'b' tag
b['id'] = 3
print(soup); # <html><head></head><body><b id="3">연습</b></body></html>
b['class'] = 'extra class'
print(soup) # <html><head></head><body><b class="extra class" id="3">연습</b></body></html>
```

### 클리앙 Crawling
```python
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
```

### Key Word Search
클리앙 계시판 페이지 1~6 중에서 '청와대' 키워드로 Data Crawling
```python
from bs4 import BeautifulSoup
import urllib.request
import re 
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
```