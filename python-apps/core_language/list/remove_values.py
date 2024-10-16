"""
    Removing Values from Lists with the remove() Method
"""

spam = ['cat', 'bat', 'rat', 'elephant']
spam.remove('bat')
print(spam)

# if the value appears multiple times in the list, only the first instance of the value will be removed
spam = ['cat', 'bat', 'rat', 'cat', 'hat', 'cat']
spam.remove('cat')
print(spam)

# attempting to delete a value that does not exist in the list will result in a ValueError error
spam = ['cat', 'bat', 'rat', 'elephant']
spam.remove('chicken')