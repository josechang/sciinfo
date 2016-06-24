import textract
import os
DATA_DIR = '/home/dd/nordron-sciinfo/Code/Wolverine_Webcrawler/pdfs'
for filename in os.listdir(DATA_DIR):
 if(filename[-4:len(filename)] ==".pdf") :
  
   text = textract.process('/home/dd/nordron-sciinfo/Code/Wolverine_Webcrawler/pdfs'+filename, method='pdfminer')
   file_txt = '/home/dd/nordron-sciinfo/Code/Wolverine_Webcrawler/txt'+filename.replace(".pdf",".txt")
   xml=open(file_txt,'w')
   for i in xrange(len(text)):
        xml.write(text[i])
   xml.close()
