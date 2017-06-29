# pyPdf available at http://pybrary.net/pyPdf/
from pyPdf import PdfFileWriter, PdfFileReader
import os
import re


k = 1;
h = 0;
os.chdir('C:\Users\Wu/nordron-sciinfo\Code\Rainy\code\extraction\PDF') #please change the path
for fileName in os.listdir('.'):
    try:


        if fileName.lower()[-3:] != "pdf": continue #read only pdf file
        input1 = PdfFileReader(file(fileName, "rb"))

############ get arabic numerals in title #############
        z = re.findall(r'\d+', input1.getDocumentInfo().title)
        z = str(z)
        z = z.replace('u','').replace(',','').replace('[','').replace(']','').replace(' ','').replace("'",'')
#######################################################

        if len(input1.getDocumentInfo().title)>7 and len(z)<5: # block title which has too little words(7words) and too many arabic numerals(5 number)
            print "%d %s \n filename: %s" %(k,input1.getDocumentInfo().title,fileName)
            pass
        else:
            print "%d None \n filename: %s" %(k,fileName)
            h += 1
        k += 1
    except:
        print "%d None \n filename: %s" %(k,fileName)
        k += 1
        h += 1
print "%d articles have no title" %(h)
