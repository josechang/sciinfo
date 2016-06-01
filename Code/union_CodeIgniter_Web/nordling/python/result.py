import os
import textract
def result_start(a):
    arr=["III.RESULTS","RESULTS","3.RESULTS"]
    
    if(a.strip().upper() in arr):     
        return 1
    else:
        return 0

def result_end(a):
    
    arr=["IV.DISCUSSION","DISCUSSION","4.DISCUSSION"]
    if(a.strip().upper() in arr):     
        return 1
    else:
        return 0

DATA_DIR = "/home/z7724581/public_html/nordling/python/PDF"
pdf_name=[]
for filename in os.listdir(DATA_DIR):
    
  if(filename[-4:len(filename)] ==".pdf") :
      
    pdf_name.append(filename.replace(".pdf",""))
    
    text = textract.process('/home/z7724581/public_html/nordling/python/PDF/'+filename, result='pdfminer')

    file_txt = '/home/z7724581/public_html/nordling/python/TXT/result_all_'+filename.replace(".pdf",".txt")

    xml=open(file_txt,'w')
    for i in xrange(len(text)):
       xml.write(text[i])
    xml.close()

for i in xrange(len(pdf_name)):
    
  myfile = open('/home/z7724581/public_html/nordling/python/TXT/result_all_'+pdf_name[i]+".txt")

  c1=0
  a2=[]
  for j in myfile.readlines():
      
    if(result_start(j.strip().replace(" ","")) or result_start(j.strip().replace(" ","")[0:7])):

      c1+=1
    elif(result_end(j.strip().replace(" ","")) or result_end(j.strip().replace(" ","")[0:8])):

     c1=0
     
    if c1 > 0 :

     a2.append(j)

  b2=open('/home/z7724581/public_html/nordling/python/TXT/'+pdf_name[i]+'_result.txt','w')
  for i in xrange(len(a2)):
     b2.write(a2[i])
  b2.close()
