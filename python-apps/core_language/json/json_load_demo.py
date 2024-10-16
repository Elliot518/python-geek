import json

employee = json.load(open("employee.json", "r"))
print(type(employee))
print('Name: %s, Age: %s, Gender: %s' % (employee['name'], employee['age'], employee['gender']))
