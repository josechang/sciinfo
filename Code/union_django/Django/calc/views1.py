from django.shortcuts import render
from django.http import HttpResponse
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
def add(request):
   if 'abstract' in request.GET:

      DATA_DIR = '/root/Django/file'
      pdf_name=[]
      for filename in os.listdir(DATA_DIR):
    
       if(filename[-4:len(filename)] ==".pdf") :
      
        pdf_name.append(filename.replace(".pdf",""))
    
        text = textract.process('/root/Django/file/'+filename, method='pdfminer')

        file_txt = '/root/Django/file/abstract_all_'+filename.replace(".pdf",".txt")

        xml=open(file_txt,'w')
        for i in xrange(len(text)):
          xml.write(text[i])
        xml.close()
      
        for i in xrange(len(pdf_name)):
	  myfile_x = open('/root/Django/file/abstract_all_'+pdf_name[i]+".txt")
	  kk=0
	  a1=[]
	  for j in myfile_x.readlines():
	    k=str(j.strip().replace(" ",""))
	    if(abstract_start(k) or abstract_start(k[0:8])):
	      kk=1
	    elif(abstract_end(k) or abstract_end(k[0:8])):
	      kk=0
	    if kk == 1 :	   
	      a1.append(str(j))
	  b1=open('/root/Django/file/'+pdf_name[i]+'_abstract.txt','w')
	  for i in xrange(len(a1)):
	    b1.write(a1[i])
	  b1.close()
      return HttpResponse('Success')
   elif 'introduction' in request.GET:
      return HttpResponse('Welcome!~'+request.GET['introduction'])
   elif 'method' in request.GET:
      return HttpResponse('Welcome!~'+request.GET['method'])
