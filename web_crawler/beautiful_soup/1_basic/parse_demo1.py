from bs4 import BeautifulSoup

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
    1. Html Parse
'''
print("1. Html Parse")
soup = BeautifulSoup(html_doc, 'html.parser')
print(soup.prettify())

print(SEP)

'''
    2. Get title attributes of html
'''
print("2. Get title attributes of html")
# <title>The Dormouse's story</title>
print(soup.title)
# title
print(soup.title.name)
# The Dormouse's story'
print(soup.title.string)
# head
print(soup.title.parent.name)
# html
print(soup.title.parent.parent.name)
