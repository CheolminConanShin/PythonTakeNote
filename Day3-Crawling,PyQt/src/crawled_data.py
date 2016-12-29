# BeautifulSoup 연습
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