import PyPDF2

minutesFile = open('meetingminutes.pdf', 'rb')
pdfReader = PyPDF2.PdfReader(minutesFile)
#watermarkedPage = pdfReader.pages[0]
pdfWatermarkReader = PyPDF2.PdfReader(open('watermark.pdf', 'rb'))
# minutesFirstPage.merge_page(pdfWatermarkReader.pages[0])
pdfWriter = PyPDF2.PdfWriter()
# pdfWriter.add_page(minutesFirstPage)
for pageNum in range(0, len(pdfReader.pages)):
    pageObj = pdfReader.pages[pageNum]
    pageObj.merge_page(pdfWatermarkReader.pages[0])
    #pdfWriter.add_page(watermarkedPage)
    pdfWriter.add_page(pageObj)
resultPdfFile = open('watermarkedCover.pdf', 'wb')

pdfWriter.write(resultPdfFile)
minutesFile.close()
resultPdfFile.close()

print("Add watermark!")
