# pyPdf available at http://pybrary.net/pyPdf/
from pyPdf import PdfFileWriter, PdfFileReader
import os
import re


def year_extractor(pdf_path, pdf_filename):
    abs_path = pdf_path + pdf_filename
    try:
        input1 = PdfFileReader(file(abs_path, "rb"))
		# "rb" => binary reading mode
        ############ get arabic numerals in title #############
        z = re.findall(r'\d+', input1.getDocumentInfo().title)
        z = str(z)
        z = z.replace('u','').replace(',','').replace('[','').replace(']','').replace(' ','').replace("'",'')
		# str.replace(old, new[, max])
        #######################################################

        # block title which has too little words and too many arabic numerals
        if len(input1.getDocumentInfo().title)>7 and len(z)<5:         
            return int(z)
        else:
            return "No title"
    except:
        print "Load pdf error."