from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

# This restores the same behavior as before.
context = ssl._create_unverified_context()

html = urlopen('http://www.pythonscraping.com/pages/page1.html', context=context)
bs = BeautifulSoup(html.read(), 'html.parser')
print(bs.h1)

