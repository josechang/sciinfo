Python 2.7.11 (v2.7.11:6d1b6a68f775, Dec  5 2015, 20:32:19) [MSC v.1500 32 bit (Intel)] on win32

Type "copyright", "credits" or "license()" for more information.
import pdfx   #pdfx is a package
pdf = pdfx.PDFx("filename-or-url.pdf")   #use the function  below pdfx
metadata = pdf.get_metadata()    #set variable
references_list = pdf.get_references()     #set variable
references_dict = pdf.get_references_as_dict()    #set variable
pdf.download_pdfs("target-directory")       #download and choose the path to store
  
