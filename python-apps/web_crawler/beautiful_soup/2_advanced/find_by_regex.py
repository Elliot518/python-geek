from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import ssl

# This restores the same behavior as before.
context = ssl._create_unverified_context()

html = urlopen('http://www.pythonscraping.com/pages/page3.html', context=context)
bs = BeautifulSoup(html, 'html.parser')
images = bs.find_all('img', {'src': re.compile('\.\.\/img\/gifts/img.*\.jpg')})
for image in images:
    print(image['src'])

