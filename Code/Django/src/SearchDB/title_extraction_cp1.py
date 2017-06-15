# pyPdf available at http://pybrary.net/pyPdf/
from pyPdf import PdfFileWriter, PdfFileReader
import os
import re


def title_extractor(pdf_path, pdf_filename):
    abs_path = pdf_path + pdf_filename
    try:
        input1 = PdfFileReader(file(abs_path, "rb"))

        ############ get arabic numerals in title #############
        z = re.findall(r'\d+', input1.getDocumentInfo().title)
        z = str(z)
        z = z.replace('u','').replace(',','').replace('[','').replace(']','').replace(' ','').replace("'",'')
        #######################################################

        # block title which has too little words and too many arabic numerals
        if len(input1.getDocumentInfo().title)>7 and len(z)<5:         
            return input1.getDocumentInfo().title
        else:
            return "No title"
    except:
        print "Load pdf error."