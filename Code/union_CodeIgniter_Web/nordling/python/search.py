import os
import textract
import sys

# search="Predicting"
def delect_special(a):
    b=a.replace(".","").replace("!","").replace("@","").replace("#","").replace("~","").replace(",","")
    return b

search=delect_special(sys.argv[2].replace("__"," ")).split(" ")
name=sys.argv[1].replace("__"," ")

text = textract.process('/home/z7724581/public_html/nordling/python/PDF/'+name+".pdf", method='pdfminer')

file_txt = '/home/z7724581/public_html/nordling/python/TXT/'+name+".txt"
xml=open(file_txt,'w')
for i in xrange(len(text)):
    xml.write(text[i])
xml.close()
#------------------------------------------------------------------------------------------------------------------------------

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
############################################################
    
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
############################################################
    
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
############################################################
    
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
############################################################
    
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
############################################################
    
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
############################################################
    
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
############################################################
def reference_start(a):
    arr=["REFERENCES"]
    
    if(a.strip().upper() in arr):     
        return 1
    else:
        return 0    
#------------------------------------------------------------------------------------------------------------------------------
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


myfile=open('/home/z7724581/public_html/nordling/python/TXT/'+name+".txt",'r')
for i in myfile.readlines():
    
  if(abstract_start(i.strip().replace(" ","")) or abstract_start(i.strip().replace(" ","")[0:8])):

     c+=1
  elif(abstract_end(i.strip().replace(" ","")) or abstract_end(i.strip().replace(" ","")[0:8])):
     c=0
     
  if c > 0 :
     a1.append(i)
  #########################################################################################################

  if(introduction_start(i.strip().replace(" ","")) or introduction_start(i.strip().replace(" ","")[0:8])):
     c1+=1
  elif(introduction_end(i.strip().replace(" ","")) or introduction_end(i.strip().replace(" ","")[0:8])):
     c1=0
     
  if c1 > 0 :
     introduction1.append(i)

  #########################################################################################################

  if(theoretical_start(i.strip().replace(" ","")) or theoretical_start(i.strip().replace(" ","")[0:8])):
     c2_1+=1
  elif(theoretical_end(i.strip().replace(" ","")) or theoretical_end(i.strip().replace(" ","")[0:8])):
     c2_1=0
     
  if c2_1 > 0 :
     theoretical1.append(i)

  #########################################################################################################

  if(method_start(i.strip().replace(" ","")) or method_start(i.strip().replace(" ","")[0:8])):
     c2+=1
  elif(method_end(i.strip().replace(" ","")) or method_end(i.strip().replace(" ","")[0:7])):
     c2=0
     
  if c2 > 0 :
     method1.append(i)
  #########################################################################################################

  if(result_start(i.strip().replace(" ","")) or result_start(i.strip().replace(" ","")[0:7])):
     c3+=1
  elif(result_end(i.strip().replace(" ","")) or result_end(i.strip().replace(" ","")[0:8])):
     c3=0
     
  if c3 > 0 :
     result1.append(i)
  #########################################################################################################

  if(discussion_start(i.strip().replace(" ","")) or discussion_start(i.strip().replace(" ","")[0:8])):
     c3+=1
  elif(discussion_end(i.strip().replace(" ","")) or discussion_end(i.strip().replace(" ","")[0:8])):
     c3=0
     
  if c3 > 0 :
     discussion1.append(i)

  #########################################################################################################

  if(conclusion_start(i.strip().replace(" ","")) or conclusion_start(i.strip().replace(" ","")[0:8])):
     c3_1+=1
  elif(conclusion_end(i.strip().replace(" ","")) or conclusion_end(i.strip().replace(" ","")[0:8])):
     c3_1=0
     
  if c3_1 > 0 :
     conclusion1.append(i)

  if(reference_start(i.strip().replace(" ","")) or reference_start(i.strip().replace(" ","")[0:8])):
      c4+=1

  if c4>0:
     reference1.append(i)

     
# # #------------------------------------------------------------------------------------------------------------------------------

a2=''.join(a1).split('.')
a3=[]
for i in xrange(len(a2)):
    a4=0
    for j in xrange(len(search)):
        
       if search[j].upper() in a2[i].upper():
           a4+=1
    if a4 == len(search) :
       a3.append(a2[i])
#####################################################

introduction2=''.join(introduction1).split('.')
introduction3=[]
for i in xrange(len(introduction2)):
    introduction4=0
    for j in xrange(len(search)):
        
       if search[j].upper() in introduction2[i].upper():
           introduction4+=1
    if introduction4 == len(search) :
       introduction3.append(introduction2[i])
####################################################

theoretical2=''.join(theoretical1).split('.')
theoretical3=[]
for i in xrange(len(theoretical2)):
    theoretical4=0
    for j in xrange(len(search)):
        
       if search[j].upper() in theoretical2[i].upper():
           theoretical4+=1
    if theoretical4 == len(search) :
       theoretical3.append(theoretical2[i])
####################################################

method2=''.join(method1).split('.')
method3=[]
for i in xrange(len(method2)):
    method4=0
    for j in xrange(len(search)):
        
       if search[j].upper() in method2[i].upper():
           method4+=1
    if method4 == len(search) :
       method3.append(method2[i])

####################################################  

result2=''.join(result1).split('.')
result3=[]
for i in xrange(len(result2)):
    result4=0
    for j in xrange(len(search)):
        
       if search[j].upper() in result2[i].upper():
           result4+=1
    if result4 == len(search) :
       result3.append(result2[i])
####################################################

discussion2=''.join(discussion1).split('.')
discussion3=[]
for i in xrange(len(discussion2)):
    discussion4=0
    for j in xrange(len(search)):
        
       if search[j].upper() in discussion2[i].upper():
           discussion4+=1
    if discussion4 == len(search) :
       discussion3.append(discussion2[i])
####################################################

conclusion2=''.join(conclusion1).split('.')
conclusion3=[]
for i in xrange(len(conclusion2)):
    conclusion4=0
    for j in xrange(len(search)):
        
       if search[j].upper() in conclusion2[i].upper():
           conclusion4+=1
    if conclusion4 == len(search) :
       conclusion3.append(conclusion2[i])
#####################################################
reference2=''.join(reference1).split('.')
reference3=[]
for i in xrange(len(reference2)):
    reference4=0
    for j in xrange(len(search)):
        
       if search[j].upper() in reference2[i].upper():
           reference4+=1
    if reference4 == len(search) :
       reference3.append(reference2[i])

#----------------------------------------------------------------------------------------      
ab=open('/home/z7724581/public_html/nordling/python/TXT/'+name+'_result.txt','w')

if len(a3) > 0:
   st_str="start_abstract" +"\n"
   st_len=str(len(a3))+"\n"
   st_end="end_abstract" +"\n"
   ab.write(st_str)
   ab.write(st_len)
   for i in xrange(len(a3)):
      j=i+1   
      ab.write(str(j) +"."+ a3[i].replace("\n","") +"\n")
      
   ab.write(st_end)
   
###################################################
if len(introduction3) > 0:
   st_str="start_introduction" +"\n"
   st_len=str(len(introduction3))+"\n"
   st_end="end_introduction" +"\n"
   ab.write(st_str)
   ab.write(st_len)
   for i in xrange(len(introduction3)):
      j=i+1

      ab.write(str(j) +"."+ introduction3[i].replace("\n","") +"\n")
   ab.write(st_end)
# ####################################################
if len(theoretical3) > 0:
   st_str="start_theoretical" +"\n"
   st_len=str(len(theoretical3))+"\n"
   st_end="end_theoretical" +"\n"
   ab.write(st_str)
   ab.write(st_len)
   for i in xrange(len(theoretical3)):
      j=i+1

      ab.write(str(j) +"."+ theoretical3[i].replace("\n","") +"\n")
   ab.write(st_end)
# ####################################################
if len(method3) > 0:
   st_str="start_method" +"\n"
   st_len=str(len(method3))+"\n"
   st_end="end_method" +"\n"
   ab.write(st_str)
   ab.write(st_len)
   for i in xrange(len(method3)):
      j=i+1

      ab.write(str(j) +"."+ method3[i].replace("\n","") +"\n")
   ab.write(st_end)
# ####################################################
if len(result3) > 0:
   st_str="start_result" +"\n"
   st_len=str(len(result3))+"\n"
   st_end="end_result" +"\n"
   ab.write(st_str)
   ab.write(st_len)
   for i in xrange(len(result3)):
      j=i+1

      ab.write(str(j) +"."+ result3[i].replace("\n","") +"\n")
   ab.write(st_end)
# ####################################################
if len(discussion3) > 0:
   st_str="start_discussion" +"\n"
   st_len=str(len(discussion3))+"\n"
   st_end="end_discussion" +"\n"
   ab.write(st_str)
   ab.write(st_len)
   for i in xrange(len(discussion3)):
      j=i+1

      ab.write(str(j) +"."+ discussion3[i].replace("\n","") +"\n")
   ab.write(st_end)
# ####################################################
if len(conclusion3) > 0:
   st_str="start_conclusion" +"\n"
   st_len=str(len(conclusion3))+"\n"
   st_end="end_conclusion" +"\n"
   ab.write(st_str)
   ab.write(st_len)
   for i in xrange(len(conclusion3)):
      j=i+1

      ab.write(str(j) +"."+ conclusion3[i].replace("\n","") +"\n")
   ab.write(st_end)
# ####################################################
if len(reference3) > 0:
   st_str="start_reference" +"\n"
   st_len=str(len(reference3))+"\n"
   st_end="end_reference" +"\n"
   ab.write(st_str)
   ab.write(st_len)
   for i in xrange(len(reference3)):
      j=i+1

      ab.write(str(j) +"."+ reference3[i].replace("\n","") +"\n")

   ab.write(st_end)
ab.close()