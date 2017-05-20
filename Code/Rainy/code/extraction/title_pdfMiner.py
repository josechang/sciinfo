from pdfminer.pdfparser import PDFParser
from pdfminer.pdfdocument import PDFDocument

fp = open('Tjarnberg2017_GeneSPIDER_Advance_article_C7MB00058H.pdf', 'rb')
parser = PDFParser(fp)
doc = PDFDocument(parser)

print doc.info  # The "Info" metadata
