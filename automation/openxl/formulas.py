import openpyxl

wb = openpyxl.Workbook()
sheet = wb.active
sheet['A1'] = 200
sheet['A2'] = 300
# Set the formula
sheet['A3'] = '=SUM(A1:A2)'
wb.save('writeFormula.xlsx')
print("Workbook Saved!")

