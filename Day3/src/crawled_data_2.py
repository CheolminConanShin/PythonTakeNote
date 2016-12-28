from bs4 import BeautifulSoup

data = """Bob's<b>Bold</b>Barbeque Sauce now available <b class="hickory">Hickory</b> and <b class="lime">Lime</a>"""
soup = BeautifulSoup(data, "html5lib")
# print(soup.prettify())

# print(soup.find('b', {"class":"lime"}))

soup = BeautifulSoup("<b id='2'>연습</b>", "html5lib")
print(soup) # <html><head></head><body><b id="2">연습</b></body></html>
b = soup.b
# Change id of a 'b' tag
b['id'] = 3
print(soup); # <html><head></head><body><b id="3">연습</b></body></html>
b['class'] = 'extra class'
print(soup) # <html><head></head><body><b class="extra class" id="3">연습</b></body></html>