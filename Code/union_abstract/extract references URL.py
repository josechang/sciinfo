Python 2.7.11 (v2.7.11:6d1b6a68f775, Dec  5 2015, 20:32:19) [MSC v.1500 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
import pdfx
pdf = pdfx.PDFx("filename-or-url.pdf")
metadata = pdf.get_metadata()
references_list = pdf.get_references()
references_dict = pdf.get_references_as_dict()
pdf.download_pdfs("target-directory")
 
