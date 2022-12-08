from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

SEP = '---------------------------------------------------------------------------------------'

# This restores the same behavior as before.
context = ssl._create_unverified_context()

html = urlopen('http://www.pythonscraping.com/pages/page3.html', context=context)
bs = BeautifulSoup(html, 'html.parser')

for child in bs.find('table', {'id': 'giftList'}).children:
    print(child)

print(SEP)

print(bs.find('img',
              {'src':'../img/gifts/img1.jpg'})
      .parent.previous_sibling.get_text())

print(SEP)