from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen('http://pythonscraping.com/pages/page3.html')
bs = BeautifulSoup(html, 'html.parser')

twoAttrsTags = bs.find_all(lambda tag: len(tag.attrs) == 2)

for tag in twoAttrsTags:
    print(tag)