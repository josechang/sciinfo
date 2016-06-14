Python 2.7.11 (v2.7.11:6d1b6a68f775, Dec  5 2015, 20:32:19) [MSC v.1500 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.

>>> document=mendeley.document.create_from_file("1022e.pdf")

Traceback (most recent call last):
  File "<pyshell#0>", line 1, in <module>
    document=mendeley.document.create_from_file("1022e.pdf")
NameError: name 'mendeley' is not defined
>>> from pdfminer.pdfparser import PDFParser
from pdfminer.pdfdocument import PDFDocument

# Open a PDF document.
fp = open('mypdf.pdf', 'rb')
parser = PDFParser(fp)
document = PDFDocument(parser, password)

# Get the outlines of the document.
outlines = document.get_outlines()
for (level,title,dest,a,se) in outlines:
    print (level, title)
    
>>> 
