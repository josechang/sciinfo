import textract
import os
DATA_DIR = 'C:/Users/Wei/Desktop/mm'
for filename in os.listdir(DATA_DIR):
 if(filename[-4:len(filename)] ==".pdf") :
  
   text = textract.process('C:/Users/Wei/Desktop/mm/'+filename, method='pdfminer')
   file_txt = 'C:/Users/Wei/Desktop/mm/'+filename.replace(".pdf",".txt")
   xml=open(file_txt,'w')
   for i in xrange(len(text)):
        xml.write(text[i])
   xml.close()
