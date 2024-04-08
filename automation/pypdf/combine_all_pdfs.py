#! python3
# combinePdfs.py - Combines all the PDFs in the current working directory into
# into a single PDF

import PyPDF2, os

"""
    Step 1: Find All PDF Files
"""
# Get all the PDF filenames
pdfFiles = []

for filename in os.listdir('.'):
    if filename.endswith('.pdf'):
        pdfFiles.append(filename)
pdfFiles.sort(key=str.lower)
pdfWriter = PyPDF2.PdfWriter()

"""
    Step 2: Open Each PDF
"""
# Loop through all the PDF files
for filename in pdfFiles:
    pdfFileObj = open(filename, 'rb')
    pdfReader = PyPDF2.PdfReader(pdfFileObj)
    # Step 3: Add Each Page
    # TODO: Loop through all the pages (except the first) and add them
    for pageNum in range(1, len(pdfReader.pages)):
        pageObj = pdfReader.pages[pageNum]
        pdfWriter.add_page(pageObj)

"""
    Step 4: Save the Results
"""
# TODO: Save the resulting PDF to a file
pdfOutput = open('allminutes.pdf', 'wb')
pdfWriter.write(pdfOutput)
pdfOutput.close()
