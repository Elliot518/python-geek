from urllib.request import urlopen
from urllib.error import HTTPError
from urllib.error import URLError
import ssl

# This restores the same behavior as before.
context = ssl._create_unverified_context()

try:
    html = urlopen("https://pythonscrapingthisurldoesnotexist.com", context=context)
except HTTPError as e:
    print(e)
except URLError as e:
    print("The server could not be found!")
else:
    print(html.read())