from pyPdf import PdfFileReader
import os
import sys

# doi extractor using pyPdf, return doi of each article in the given path


def doi_extract(pdf_path, PDF):
    # must be pdf file in the path, otherwise it won't work!!
    # extract pdf information
    pdf_info = PdfFileReader(open(pdf_path + PDF, 'rb')
                             ).getDocumentInfo()
    # get doi information from pdf_info  
    doi = str('http://dx.doi.org/')

    # https://pythonhosted.org/PyPDF2/DocumentInformation.html#PyPDF2.pdf.DocumentInformation
    # pdf_info => The DocumentInformation Class

    return doi
