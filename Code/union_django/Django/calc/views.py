from django.shortcuts import render
from django.http import HttpResponse
import os
import textract

def delect_special(a):
    b=a.replace(".","").replace("!","").replace("@","").replace("#","").replace("~","").replace(",","")
    return b
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
def theoretical_start(a):
    arr=["THEORETICAL"]
    if(a.strip().upper() in arr):     
	 return 1     
    else:
         return 0

def theoretical_end(a):
   arr=["II.METHODS","METHODS","2.METHODS","MATERIAL","EXPERIME"]
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
def conclusion_start(a):
    arr=["CONCLUSI","SUMMARYA","SUMMARY"] 
    if(a.strip().upper() in arr):     
        return 1
    else:
        return 0

def conclusion_end(a):
    arr=["REFERENCES"]
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
 
  if(len(request.GET['search'])==0):
   all_name=[]
   if 'abstract' in request.GET:

      DATA_DIR = '/root/Django/file'
      pdf_name=[]
      all_name.append("abstract")
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
      all_name.append("introduction")
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
      all_name.append("method")
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
      all_name.append("result")
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
      all_name.append("discussion")
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
      all_name.append("reference")
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
   

   DATA_DIR = '/root/Django/file'
   pdf_name_all=[]
   
   for filename in os.listdir(DATA_DIR):

     if(filename[-4:len(filename)] ==".pdf") :

       pdf_name_all.append(filename.replace(".pdf",""))

   b1=open('/root/Django/calc/templates/home3.html')
   b2=open('/root/Django/calc/templates/home4.html','w')

   for k in b1.readlines():
      kk=str(k.strip().replace(" ",""))
     	 
      if(kk=="<!--abstract-->" and 'abstract' in request.GET):
   	      for j in xrange(len(pdf_name_all)):
   	          b3=open('/root/Django/file/'+pdf_name_all[j]+'_abstract.txt')
                  for jj in b3.readlines():
                     b2.write(str(jj))
		     b2.write("<br>")
              b2.write("<br>--------------------------------------<br>")
      elif(kk=="<!--introduction-->" and 'introduction' in request.GET):
              for j in xrange(len(pdf_name_all)):
                 b3=open('/root/Django/file/'+pdf_name_all[j]+'_introduction.txt')
                 for jj in b3.readlines():
                     b2.write(str(jj))
		     b2.write("<br>")
              b2.write("<br>--------------------------------------<br>")
      elif(kk=="<!--method-->" and 'method' in request.GET):
              for j in xrange(len(pdf_name_all)):
                 b3=open('/root/Django/file/'+pdf_name_all[j]+'_method.txt')
                 for jj in b3.readlines():
                     b2.write(str(jj))
		     b2.write("<br>")
              b2.write("<br>--------------------------------------<br>")
      elif(kk=="<!--result-->" and 'result' in request.GET):
              for j in xrange(len(pdf_name_all)):
                 b3=open('/root/Django/file/'+pdf_name_all[j]+'_result.txt')
                 for jj in b3.readlines():
                     b2.write(str(jj))
		     b2.write("<br>")
              b2.write("<br>--------------------------------------<br>")
      elif(kk=="<!--discussion-->" and 'discussion' in request.GET):
              for j in xrange(len(pdf_name_all)):
                  b3=open('/root/Django/file/'+pdf_name_all[j]+'_discussion.txt')
                  for jj in b3.readlines():
                      b2.write(str(jj))
		      b2.write("<br>")
              b2.write("<br>--------------------------------------<br>")                    
      elif(kk=="<!--reference-->" and 'reference' in request.GET):
              for j in xrange(len(pdf_name_all)):
                 b3=open('/root/Django/file/'+pdf_name_all[j]+'_reference.txt')
                 for jj in b3.readlines():
                    b2.write(str(jj))
	            b2.write("<br>")
              b2.write("<br>--------------------------------------<br>")
      else:
           b2.write(k)

   return render(request, 'home4.html')
  
  else:
      search=delect_special(request.GET['search']).split(" ")

      DATA_DIR = '/root/Django/file'
      pdf_name=[]
      for filename in os.listdir(DATA_DIR):

       if(filename[-4:len(filename)] ==".pdf") :

        pdf_name.append(filename.replace(".pdf",""))

        text = textract.process('/root/Django/file/'+filename, method='pdfminer')

        file_txt = '/root/Django/file/all_'+filename.replace(".pdf",".txt")

        xml=open(file_txt,'w')
        for i in xrange(len(text)):
          xml.write(text[i])
        xml.close()

      for i in xrange(len(pdf_name)):
        myfile_w = open('/root/Django/file/all_'+pdf_name[i]+'.txt','r')

        c=0
        c1=0
        c2_1=0
        c2=0
        c3=0
        c4=0
        c3_1=0
        a1=[]
        introduction1=[]
        theoretical1=[]
        method1=[]
        result1=[]
        discussion1=[]
        conclusion1=[]
        reference1=[]
        for j in myfile_w.readlines():
    
          k=str(j.strip().replace(" ",""))
          if(abstract_start(k) or abstract_start(k[0:8])):
              c=1
          elif(abstract_end(k) or abstract_end(k[0:8])):
              c=0
          if c == 1 :
              a1.append(str(j))

          if(introduction_start(k) or introduction_start(k[0:8])):
            c1+=1
          elif(introduction_end(k) or introduction_end(k[0:8])):
            c1=0
          if c1 > 0 :
            introduction1.append(str(j))

          if(method_start(k) or method_start(k[0:8])):
             c2+=1
          elif(method_end(k) or method_end(k[0:7])):
             c2=0 
          if c2 > 0 :
             method1.append(str(j))

          if(result_start(k) or result_start(k[0:7])):
             c3+=1
          elif(result_end(k) or result_end(k[0:8])):
             c3=0 
          if c3 > 0 :
             result1.append(str(j))
     
          if(discussion_start(k) or discussion_start(k[0:8])):
             c3_1+=1
          elif(discussion_end(k) or discussion_end(k[0:8])):
             c3_1=0    
          if c3_1 > 0 :
            discussion1.append(str(j))
     
          if(reference_start(k) or reference_start(k[0:8])):
             c4+=1
          if c4>0:
             reference1.append(str(j))       

        a2=''.join(a1).split('.')
        a3=[]
	for x in xrange(len(a2)):
          a4=0
	  for xx in xrange(len(search)):
	    if str(search[xx]).upper() in str(a2[x]).upper():
             a4+=1 
          if a4 >0 :
	     a3.append(a2[x])

        introduction2=''.join(introduction1).split('.')
        introduction3=[]
        for x in xrange(len(introduction2)):
            introduction4=0
            for xx in xrange(len(search)):
              if str(search[xx].upper()) in str(introduction2[x].upper()):
                introduction4+=1
            if introduction4 >0 :
                introduction3.append(introduction2[x])
         
	method2=''.join(method1).split('.')
        method3=[]
        for x in xrange(len(method2)):
            method4=0
            for xx in xrange(len(search)):
              if str(search[xx].upper()) in str(method2[x].upper()):
                method4+=1
            if method4 >0 :
                method3.append(method2[x])

        result2=''.join(result1).split('.')
        result3=[]
        for x in xrange(len(result2)):
            result4=0
            for xx in xrange(len(search)):
              if str(search[xx].upper()) in str(result2[x].upper()):
                result4+=1
            if result4 >0 :
                result3.append(result2[x])

        discussion2=''.join(discussion1).split('.')
        discussion3=[]
        for x in xrange(len(discussion2)):
            discussion4=0
            for xx in xrange(len(search)):
              if str(search[xx].upper()) in str(discussion2[x].upper()):
                discussion4+=1
            if discussion4 >0 :
                discussion3.append(discussion2[x])

        reference2=''.join(reference1).split('.')
        reference3=[]
        for x in xrange(len(reference2)):
            reference4=0
            for xx in xrange(len(search)):
              if str(search[xx].upper()) in str(reference2[x].upper()):
                reference4+=1
            if reference4 >0 :
                reference3.append(reference2[x])


        # ab=open('/root/Django/file/'+pdf_name[i]+'_result.txt','w')

        b1=open('/root/Django/calc/templates/home3.html')
        b2=open('/root/Django/calc/templates/home4.html','w')
        for b3 in b1.readlines():

          b4=str(b3.strip().replace(" ",""))    
          if(b4=="<!--abstract-->" and len(a3)>0):
            b2.write("abstract<br><br><br><br>")
            for xxx in xrange(len(a3)):  
	           b2.write(str(a3[xxx])+"-------------------<br>")
          
          elif(b4=="<!--introduction-->" and len(introduction3)>0):
            b2.write("introduction<br><br>")
            for xxx in xrange(len(introduction3)):  
             b2.write(str(introduction3[xxx])+"-------------------<br>")
          elif(b4=="<!--method-->" and len(method3)>0):
            b2.write("method<br><br>")
            for xxx in xrange(len(method3)):  
             b2.write(str(method3[xxx])+"-------------------<br>")
          elif(b4=="<!--result-->" and len(result3)>0):
            b2.write("result<br><br>")
            for xxx in xrange(len(result3)):  
             b2.write(str(result3[xxx])+"-------------------<br>")
          elif(b4=="<!--discussion-->" and len(discussion3)>0):
            b2.write("discussion<br><br>")
            for xxx in xrange(len(discussion3)):  
             b2.write(str(discussion3[xxx])+"-------------------<br>")
          elif(b4=="<!--reference-->" and len(reference3)>0):
            b2.write("reference<br><br>")
            for xxx in xrange(len(reference3)):  
             b2.write(str(reference3[xxx])+"-------------------<br>")
          else:
             b2.write(b3)
      

  return render(request, 'home4.html')
   #return HttpResponse('Success')
