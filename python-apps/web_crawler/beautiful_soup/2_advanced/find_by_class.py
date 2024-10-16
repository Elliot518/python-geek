from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl


SEP = '---------------------------------------------------------------------------------------'

# This restores the same behavior as before.
context = ssl._create_unverified_context()

html = urlopen('http://www.pythonscraping.com/pages/warandpeace.html', context=context)
bs = BeautifulSoup(html, "html.parser")


titles = bs.find_all(['h1', 'h2','h3','h4','h5','h6'])
print([title for title in titles])

print(SEP)

nameList = bs.findAll('span', {'class': 'green'})
for name in nameList:
    print(name.get_text())

print(SEP)

allText = bs.find_all('span', {'class':{'green', 'red'}})
print([text for text in allText])

print(SEP)

nameList = bs.find_all(text='the prince')
print(nameList)
print(len(nameList))

