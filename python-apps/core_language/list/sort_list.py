"""
    Sorting the Values in a List with the sort() Method
"""

spam = [2, 5, 3.14, 1, -7]
spam.sort()
print(spam)

spam = ['ants', 'cats', 'dogs', 'badgers', 'elephants']
spam.sort()
print(spam)

# use the reverse keyword argument to sort the values in reverse order
spam.sort(reverse=True)
print(spam)

# sort() uses “ASCIIbetical order” rather than actual alphabetical order
spam = ['Alice', 'ants', 'Bob', 'badgers', 'Carol', 'cats']
spam.sort()
print(spam)

# sort the values in regular alphabetical order, pass str.lower
spam = ['a', 'z', 'A', 'Z']
spam.sort(key=str.lower)
print(spam)
