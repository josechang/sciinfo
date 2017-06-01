# pyPdf available at http://pybrary.net/pyPdf/
from pyPdf import PdfFileWriter, PdfFileReader
import os
import re


k = 1;
h = 0; # number of 'none'
os.chdir('C:\Users\Wu\Desktop/100article') #change path
for fileName in os.listdir('.'):
    try:


        if fileName.lower()[-3:] != "pdf": continue
        input1 = PdfFileReader(file(fileName, "rb"))
####################### test #######################################
        z = re.findall(r'\d+', input1.getDocumentInfo().title)
        z = str(z)
        z = z.replace('u','').replace(',','').replace('[','').replace(']','').replace(' ','').replace("'",'')
####################################################################

        if len(input1.getDocumentInfo().title)>7 and len(z)<5:
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
