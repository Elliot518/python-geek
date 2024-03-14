import openpyxl
from openpyxl.styles import Font

wb = openpyxl.Workbook()
sheet = wb['Sheet']

# create a font
italic24Font = Font(size=24, italic=True)
# Apply the font to A1
sheet['A1'].font = italic24Font
sheet['A1'] = 'Hello, world!'

fontObj1 = Font(name='Times New Roman', size=24, color="FF1493", bold=True)
sheet['B3'].font = fontObj1
sheet['B3'] = 'Bold Times New Roman'

wb.save('styles.xlsx')
print("Workbook Saved!")

