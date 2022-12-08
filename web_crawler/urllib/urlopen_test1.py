from urllib.request import urlopen
import ssl

# This restores the same behavior as before.
context = ssl._create_unverified_context()

html = urlopen('http://pythonscraping.com/pages/page1.html', context=context)
print(html.read())
