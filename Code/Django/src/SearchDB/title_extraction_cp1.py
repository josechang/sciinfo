# pyPdf available at http://pybrary.net/pyPdf/
from pyPdf import PdfFileWriter, PdfFileReader
import os
import re


def title_extractor():
    k = 1;
    h = 0; # number of 'none'
    os.chdir('100article/') #change path


    f = open('../txt/title', 'w') # creating file for recording title for Django

    for fileName in os.listdir('.'):
        try:
            if fileName.lower()[-3:] != "pdf": continue #read pdf file
            input1 = PdfFileReader(file(fileName, "rb"))

    ############ get arabic numerals in title #############
            z = re.findall(r'\d+', input1.getDocumentInfo().title)
            z = str(z)
            z = z.replace('u','').replace(',','').replace('[','').replace(']','').replace(' ','').replace("'",'')
    #######################################################
            # print z
            if len(input1.getDocumentInfo().title)>7 and len(z)<5: # block title which has too little words and too many arabic numerals
                # print "%d %s \n filename: %s" %(k,input1.getDocumentInfo().title,fileName)
                tmp = input1.getDocumentInfo().title + '\n'
                f.write(tmp) # write title to the file
                pass
            else:
                # print "%d None \n filename: %s" %(k,fileName)
                h += 1
            k += 1
        except:
            # print "%d None \n filename: %s" %(k,fileName)
            k += 1
            h += 1
    # print "%d articles have no title" %(h)
    f.close()
