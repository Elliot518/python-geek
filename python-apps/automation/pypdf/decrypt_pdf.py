import PyPDF2

pdfReader = PyPDF2.PdfReader(open('encrypted.pdf', 'rb'))
print(pdfReader.is_encrypted)

pdfReader.decrypt('rosebud')
pageObj = pdfReader.pages[0]
print(pageObj.extract_text)
