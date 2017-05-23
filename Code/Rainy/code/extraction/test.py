from pyPdf import PdfFileReader
f = open('file_1.pdf','rb')
p = PdfFileReader(f)
o=p.getDocumentInfo()
print o
