import PyPDF2

minutesFile = open('meetingminutes.pdf', 'rb')
pdfReader = PyPDF2.PdfReader(minutesFile)
page = pdfReader.pages[0]
page.rotate(90)
pdfWriter = PyPDF2.PdfWriter()
pdfWriter.add_page(page)
resultPdfFile = open('rotatedPage.pdf', 'wb')
pdfWriter.write(resultPdfFile)
resultPdfFile.close()
minutesFile.close()
print("Pdf rotated!")

