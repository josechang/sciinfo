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
        N = re.findall(r'\d+', input1.getDocumentInfo().title)
        N = str(N)
        N = N.replace('[','').replace(']','').replace(' ','').replace("'",'')
		# str.replace(old, new[, max])
		year = int(N[0:4])
        #######################################################
		author = input1.getDocumentInfo().author
		
        # block title which has too little words and too many arabic numerals
        if len(input1.getDocumentInfo().title)>7 and len(N)<5:         
            return int(year)
        else:
            return "No title or wrong published year"
    except:
        print "Load pdf error."