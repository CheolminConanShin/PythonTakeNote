# coding:utf-8
from bs4 import BeautifulSoup
import urllib.request
response = urllib.request.urlopen('http://www.clien.net/cs2/bbs/board.php?bo_table=park')
page = response.read().decode('utf-8', 'ignore')
soup = BeautifulSoup(page, 'html5lib')
list = soup.findAll('td', attrs={'class':'post_subject'})
title = list[2].find('a').text
print(title)
for item in list:
        title = item.find('a').text
        print(title)
