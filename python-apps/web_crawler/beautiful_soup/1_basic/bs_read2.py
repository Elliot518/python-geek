from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup
import ssl

# This restores the same behavior as before.
context = ssl._create_unverified_context()

def get_title(url):
    try:
        html = urlopen(url, context=context)
    except HTTPError as e:
        return None

    try:
        bs = BeautifulSoup(html.read(), 'html.parser')
        ttl = bs.body.h1
    except AttributeError as e:
        return None

    return ttl


if __name__ == "__main__":
    title = get_title('http://www.pythonscraping.com/pages/page1.html')
    if title is None:
        print('Title could not be found')
    else:
        print(title)

