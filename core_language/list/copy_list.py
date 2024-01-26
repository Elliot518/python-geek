"""
    with and without copy
"""

import copy


# without copy
def eggs(someParameter):
    someParameter.append('Hello')


spam = [1, 2, 3]
eggs(spam)
print(spam)

spam = ['A', 'B', 'C', 'D']
# print memory address
print(id(spam))

cheese = copy.copy(spam)
# print memory address
print(id(cheese))

cheese[1] = 42
print(spam)
print(cheese)
