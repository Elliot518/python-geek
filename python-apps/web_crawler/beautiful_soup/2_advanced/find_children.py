from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

# This restores the same behavior as before.
context = ssl._create_unverified_context()

html = urlopen('http://www.pythonscraping.com/pages/page3.html', context=context)
bs = BeautifulSoup(html, 'html.parser')
for child in bs.find('table', {'id': 'giftList'}).children:
    # find the first td
    first_td = child.findNext('td')
    if first_td:
        print("First Td: %s" % first_td.get_text())
        second_td = first_td.findNext('td')
        if second_td:
            print("Second Td: %s" % second_td.get_text())
    print('-------------------------------------------------------------------------')

