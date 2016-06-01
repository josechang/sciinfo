import os
import textract

def abstract_start(a):
    arr=['ABSTRACT']
    
    if(a.strip().upper() in arr):     
        return 1
    else:
        return 0

def abstract_end(a):
    arr=['1.INTRODUCTION',"I.INTRODUCTION","INTRODUCTION","INDEXTER","1INTRODUCTION"]
    
    if(a.strip().upper() in arr):     
        return 1
    else:
        return 0


DATA_DIR = "/home/z7724581/public_html/nordling/python/PDF"
pdf_name=[]
for filename in os.listdir(DATA_DIR):
    
  if(filename[-4:len(filename)] ==".pdf") :
      
    pdf_name.append(filename.replace(".pdf",""))
    
    text = textract.process('/home/z7724581/public_html/nordling/python/PDF/'+filename, method='pdfminer')

    file_txt = '/home/z7724581/public_html/nordling/python/TXT/abstract_all_'+filename.replace(".pdf",".txt")

    xml=open(file_txt,'w')
    for i in xrange(len(text)):
       xml.write(text[i])
    xml.close()

for i in xrange(len(pdf_name)):
    
  myfile = open('/home/z7724581/public_html/nordling/python/TXT/abstract_all_'+pdf_name[i]+".txt")

  c=0
  c1=0
  a1=[]
  a2=[]
  for j in myfile.readlines():
      
    #abstract-----------------------------------------
    if(abstract_start(j.strip().replace(" ","")) or abstract_start(j.strip().replace(" ","")[0:8])):

     c+=1
    elif(abstract_end(j.strip().replace(" ","")) or abstract_end(j.strip().replace(" ","")[0:8])):
        
     c=0   
    if c > 0 :
      a1.append(j)


  b1=open('/home/z7724581/public_html/nordling/python/TXT/'+pdf_name[i]+'_abstract.txt','w')
  for i in xrange(len(a1)):
     b1.write(a1[i])
  b1.close()