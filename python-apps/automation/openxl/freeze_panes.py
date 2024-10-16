import openpyxl

wb = openpyxl.load_workbook('produceSales.xlsx')
sheet = wb.active
# Freeze the rows above B2 and the columns on the left of B2
sheet.freeze_panes = 'B2'
wb.save('freezeExample.xlsx')
print("Workbook Saved!")
