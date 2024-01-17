"""
    Finding a Value in a List with the index() Method
"""

spam = ['hello', 'hi', 'howdy', 'heyas']
print(spam.index('hello'))
print(spam.index('heyas'))
spam = ['Zophie', 'Pooka', 'Fat-tail', 'Pooka']
print(spam.index('Pooka'))

# if not exits will raise error
print(spam.index('notexist'))