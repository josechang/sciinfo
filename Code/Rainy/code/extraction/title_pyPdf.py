# pyPdf available at http://pybrary.net/pyPdf/
from pyPdf import PdfFileWriter, PdfFileReader
import os

for fileName in os.listdir('.'):
    #try:
        if fileName.lower()[-3:] != "pdf": continue
        input1 = PdfFileReader(file(fileName, "rb"))

        # print the title of document1.pdf
        #print '##1', fileName, '##2', input1.getDocumentInfo().title
        if len(input1.getDocumentInfo().title)>7:
            print  input1.getDocumentInfo().title
        else:
            print "none"
    #I need to consider number in title latter
    #except:
        #print "none"
