the folder contains the extraction method of an article of information retrieval course 2017

######## set up pdftitle_pyPDF_PDFMiner  ####
This code can extract title from PDF by extracting the metadata. If the metadata of title doesn't exit it will extract first line in pdf as a title

step1 install pdfMiner 20110515:
  use pip to install: pip install pdfMiner==20110115
step2 install pyPdf:
  pip install pyPdf
step3 run the code:
  python pdftitle_pyPDF_PDFMiner.py "file.pdf"  #file is the name of PDF

######## dot_extractor.py #########
specify the pat of the pdf folder, The program will extract the orginal source of every pdf file in that folder and return a txt file.
