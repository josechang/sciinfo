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

def introduction_start(a):
    arr=['1.INTRODUCTION',"I.INTRODUCTION","INTRODUCTION","1INTRODUCTION"]
    
    if(a.strip().upper() in arr):     
        return 1
    else:
        return 0

def introduction_end(a):
    arr=["II.METHODS","METHODS","2.METHODS","THEORET","MATERIAL"]
    
    if(a.strip().upper() in arr):     
        return 1
    else:
        return 0

def method_start(a):
    arr=["II.METHODS","METHODS","2.METHODS","MATERIAL","EXPERIME","METHOD"]
    
    if(a.strip().upper() in arr):     
        return 1
    else:
        return 0

def method_end(a):
    arr=["III.RESULTS","RESULTS","3.RESULTS","3FEATURE"]
    
    if(a.strip().upper() in arr):     
        return 1
    else:
        return 0

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

def discussion_start(a):
    arr=["IV.DISCUSSION","DISCUSSION","4.DISCUSSION"]
    
    if(a.strip().upper() in arr):     
        return 1
    else:
        return 0

def discussion_end(a):
    
    arr=["REFERENCES","CONCLUSI","SUMMARYA","SUMMARY"]
    if(a.strip().upper() in arr):     
        return 1
    else:
        return 0

def reference_start(a):
    arr=["REFERENCES"]
    
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
   if 'introduction' in request.GET:

      DATA_DIR = '/root/Django/file'
      pdf_name=[]
      for filename in os.listdir(DATA_DIR):

       if(filename[-4:len(filename)] ==".pdf") :

        pdf_name.append(filename.replace(".pdf",""))

        text = textract.process('/root/Django/file/'+filename, method='pdfminer')

        file_txt = '/root/Django/file/introduction_all_'+filename.replace(".pdf",".txt")

        xml=open(file_txt,'w')
        for i in xrange(len(text)):
          xml.write(text[i])
        xml.close()

        for i in xrange(len(pdf_name)):
          myfile_x = open('/root/Django/file/introduction_all_'+pdf_name[i]+".txt")
          kk=0
          a1=[]
          for j in myfile_x.readlines():
            k=str(j.strip().replace(" ",""))
            if(introduction_start(k) or introduction_start(k[0:8])):
              kk=1
            elif(introduction_end(k) or introduction_end(k[0:8])):
              kk=0
            if kk == 1 :
              a1.append(str(j))
          b1=open('/root/Django/file/'+pdf_name[i]+'_introduction.txt','w')
          for i in xrange(len(a1)):
            b1.write(a1[i])
          b1.close()
   if 'method' in request.GET:

      DATA_DIR = '/root/Django/file'
      pdf_name=[]
      for filename in os.listdir(DATA_DIR):

       if(filename[-4:len(filename)] ==".pdf") :

        pdf_name.append(filename.replace(".pdf",""))

        text = textract.process('/root/Django/file/'+filename, method='pdfminer')

        file_txt = '/root/Django/file/method_all_'+filename.replace(".pdf",".txt")

        xml=open(file_txt,'w')
        for i in xrange(len(text)):
          xml.write(text[i])
        xml.close()

        for i in xrange(len(pdf_name)):
          myfile_x = open('/root/Django/file/method_all_'+pdf_name[i]+".txt")
          kk=0
          a1=[]
          for j in myfile_x.readlines():
            k=str(j.strip().replace(" ",""))
            if(method_start(k) or method_start(k[0:8])):
              kk=1
            elif(method_end(k) or method_end(k[0:7])):
              kk=0
            if kk == 1 :
              a1.append(str(j))
          b1=open('/root/Django/file/'+pdf_name[i]+'_method.txt','w')
          for i in xrange(len(a1)):
            b1.write(a1[i])
          b1.close()
   if 'result' in request.GET:

      DATA_DIR = '/root/Django/file'
      pdf_name=[]
      for filename in os.listdir(DATA_DIR):

       if(filename[-4:len(filename)] ==".pdf") :

        pdf_name.append(filename.replace(".pdf",""))

        text = textract.process('/root/Django/file/'+filename, method='pdfminer')

        file_txt = '/root/Django/file/result_all_'+filename.replace(".pdf",".txt")

        xml=open(file_txt,'w')
        for i in xrange(len(text)):
          xml.write(text[i])
        xml.close()

        for i in xrange(len(pdf_name)):
          myfile_x = open('/root/Django/file/result_all_'+pdf_name[i]+".txt")
          kk=0
          a1=[]
          for j in myfile_x.readlines():
            k=str(j.strip().replace(" ",""))
            if(result_start(k) or result_start(k[0:7])):
              kk=1
            elif(result_end(k) or result_end(k[0:8])):
              kk=0
            if kk == 1 :
              a1.append(str(j))
          b1=open('/root/Django/file/'+pdf_name[i]+'_result.txt','w')
          for i in xrange(len(a1)):
            b1.write(a1[i])
          b1.close()
   if 'discussion' in request.GET:

      DATA_DIR = '/root/Django/file'
      pdf_name=[]
      for filename in os.listdir(DATA_DIR):

       if(filename[-4:len(filename)] ==".pdf") :

        pdf_name.append(filename.replace(".pdf",""))

        text = textract.process('/root/Django/file/'+filename, method='pdfminer')

        file_txt = '/root/Django/file/discussion_all_'+filename.replace(".pdf",".txt")

        xml=open(file_txt,'w')
        for i in xrange(len(text)):
          xml.write(text[i])
        xml.close()

        for i in xrange(len(pdf_name)):
          myfile_x = open('/root/Django/file/discussion_all_'+pdf_name[i]+".txt")
          kk=0
          a1=[]
          for j in myfile_x.readlines():
            k=str(j.strip().replace(" ",""))
            if(discussion_start(k) or discussion_start(k[0:8])):
              kk=1
            elif(discussion_end(k) or discussion_end(k[0:8])):
              kk=0
            if kk == 1 :
              a1.append(str(j))
          b1=open('/root/Django/file/'+pdf_name[i]+'_discussion.txt','w')
          for i in xrange(len(a1)):
            b1.write(a1[i])
          b1.close()
   if 'reference' in request.GET:

      DATA_DIR = '/root/Django/file'
      pdf_name=[]
      for filename in os.listdir(DATA_DIR):

       if(filename[-4:len(filename)] ==".pdf") :

        pdf_name.append(filename.replace(".pdf",""))

        text = textract.process('/root/Django/file/'+filename, method='pdfminer')

        file_txt = '/root/Django/file/reference_all_'+filename.replace(".pdf",".txt")

        xml=open(file_txt,'w')
        for i in xrange(len(text)):
          xml.write(text[i])
        xml.close()

        for i in xrange(len(pdf_name)):
          myfile_x = open('/root/Django/file/reference_all_'+pdf_name[i]+".txt")
          kk=0
          a1=[]
          for j in myfile_x.readlines():
            k=str(j.strip().replace(" ",""))
            if(reference_start(k) or reference_start(k[0:8])):
              kk=1
            if kk == 1 :
              a1.append(str(j))
          b1=open('/root/Django/file/'+pdf_name[i]+'_reference.txt','w')
          for i in xrange(len(a1)):
             b1.write(a1[i])
          b1.close()
   return HttpResponse('Success')
