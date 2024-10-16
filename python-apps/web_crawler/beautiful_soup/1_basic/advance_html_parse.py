from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl


# This restores the same behavior as before.
context = ssl._create_unverified_context()

html = urlopen('http://www.pythonscraping.com/pages/warandpeace.html', context=context)
bs = BeautifulSoup(html, "html.parser")
nameList = bs.findAll('span', {'class': 'green'})
for name in nameList:
    print(name.get_text())




