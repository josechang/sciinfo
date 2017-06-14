from pyPdf import PdfFileReader
import os, sys

# doi extractor using pyPdf, return doi of each article in the given path
def doi_extract(pdf_path):
    # must be pdf file in the path, otherwise it won't work!!
    os.chdir(pdf_path)
    doi = []

    for PDFs in os.listdir('.'):
        pdf_info = PdfFileReader(open(PDFs, 'rb')).getDocumentInfo() # extract pdf information
        doi.append('http://doi.org/'+pdf_info['/doi']) # get doi information from pdf_info

    return doi

path = '/Users/dickson/tmp/pdf'
doi_extract(path)
