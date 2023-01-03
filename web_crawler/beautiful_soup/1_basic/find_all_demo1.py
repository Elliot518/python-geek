from bs4 import BeautifulSoup
import re

SEP = "-------------------------------------------------------------------------------------"

html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""

'''
    1. Find all by tag name
'''
print("1. Find all by tag name")
soup = BeautifulSoup(html_doc, 'html.parser')

# [<title>The Dormouse's story</title>]
print(soup.find_all("title"))

print(SEP)

'''
    2. Find all by keyword
'''
print("2. Find all by keyword")
# [<a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>]
print(soup.find_all(id='link2'))

# [<a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>]
print(soup.find_all(href=re.compile("elsie")))
