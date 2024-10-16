import openpyxl

wb = openpyxl.load_workbook('example.xlsx')
# get a list of all the sheet names in the workbook
print(wb.sheetnames)

# get a sheet by name from the workbook
sheet = wb['Sheet3']
print(type(sheet))
print(sheet.title)

# get the active sheet
anotherSheet = wb.active
print(anotherSheet.title)
