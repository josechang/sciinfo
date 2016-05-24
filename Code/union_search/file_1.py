import textract
text = textract.process('file_1.pdf', method='pdfminer')

search="Biomedical Engineering"
def delect_special(a):
    b=a.replace(".","").replace("!","").replace("@","").replace("#","").replace("~","").replace(",","")
    return b

search1=delect_special(search).split(" ")


xml=open('pdf_1.txt','w')

for i in xrange(len(text)):
    xml.write(text[i])
xml.close()

myfile = open("pdf_1.txt")


xml=open('pdf_1.txt','w')

for i in xrange(len(text)):
    xml.write(text[i])
xml.close()


myfile = open("pdf_1.txt")

#------------------------------------------------------------------------------------------------------------------------------

def abstract_start(a):
    arr=['ABSTRACT']
    
    if(a.strip().upper() in arr):     
        return 1
    else:
        return 0

def abstract_end(a):
    arr=['KEYWORDS',"I.INTRODUCTION","INTRODUCTION"]
    
    if(a.strip().upper() in arr):     
        return 1
    else:
        return 0
############################################################
    
def introduction_start(a):
    arr=["I.INTRODUCTION","INTRODUCTION"]
    
    if(a.strip().upper() in arr):     
        return 1
    else:
        return 0

def introduction_end(a):
    arr=["II.METHODS","METHODS"]
    
    if(a.strip().upper() in arr):     
        return 1
    else:
        return 0

############################################################
    
def method_start(a):
    arr=["II.METHODS","METHODS"]
    
    if(a.strip().upper() in arr):     
        return 1
    else:
        return 0

def method_end(a):
    arr=["III.methodS ","methodS "]
    
    if(a.strip().upper() in arr):     
        return 1
    else:
        return 0
############################################################
    
def result_start(a):
    arr=["III.RESULTS","RESULTS"]
    
    if(a.strip().upper() in arr):     
        return 1
    else:
        return 0

def result_end(a):
    
    arr=["IV.DISCUSSION","DISCUSSION"]
    if(a.strip().upper() in arr):     
        return 1
    else:
        return 0
############################################################
    
def discussion_start(a):
    arr=["IV.DISCUSSION","DISCUSSION"]
    
    if(a.strip().upper() in arr):     
        return 1
    else:
        return 0

def discussion_end(a):
    
    arr=["REFERENCES"]
    if(a.strip().upper() in arr):     
        return 1
    else:
        return 0
#IV. DISCUSSION


    
#------------------------------------------------------------------------------------------------------------------------------
c=0
c1=0
c2=0
c3=0
c4=0

a1=[]
introduction1=[]
method1=[]
result1=[]
discussion1=[]


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

  if(method_start(i.strip().replace(" ","")) or method_start(i.strip().replace(" ","")[0:8])):
     c2+=1
  elif(method_end(i.strip().replace(" ","")) or method_end(i.strip().replace(" ","")[0:8])):
     c2=0
     
  if c2 > 0 :
     method1.append(i)
  #########################################################################################################

  if(result_start(i.strip().replace(" ","")) or result_start(i.strip().replace(" ","")[0:8])):
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




     
#------------------------------------------------------------------------------------------------------------------------------

a2=''.join(a1).split('.')
a3=[]
for i in xrange(len(a2)):
    a4=0
    for j in xrange(len(search1)):
        
       if search1[j].upper() in a2[i].upper():
           a4+=1
    if a4 == len(search1) :
       a3.append(a2[i])
#####################################################

introduction2=''.join(introduction1).split('.')
introduction3=[]
for i in xrange(len(introduction2)):
    introduction4=0
    for j in xrange(len(search1)):
        
       if search1[j].upper() in introduction2[i].upper():
           introduction4+=1
    if introduction4 == len(search1) :
       introduction3.append(introduction2[i])
####################################################

method2=''.join(method1).split('.')
method3=[]
for i in xrange(len(method2)):
    method4=0
    for j in xrange(len(search1)):
        
       if search1[j].upper() in method2[i].upper():
           method4+=1
    if method4 == len(search1) :
       method3.append(method2[i])

####################################################  

result2=''.join(result1).split('.')
result3=[]
for i in xrange(len(result2)):
    result4=0
    for j in xrange(len(search1)):
        
       if search1[j].upper() in result2[i].upper():
           result4+=1
    if result4 == len(search1) :
       result3.append(result2[i])
####################################################

discussion2=''.join(discussion1).split('.')
discussion3=[]
for i in xrange(len(discussion2)):
    discussion4=0
    for j in xrange(len(search1)):
        
       if search1[j].upper() in discussion2[i].upper():
           discussion4+=1
    if discussion4 == len(search1) :
       discussion3.append(discussion2[i])

#----------------------------------------------------------------------------------------      
ab=open('pdf_all.txt','w')

ab.write("Abstract"+"   "+str(search) +"-------------------------------------------------------------------------------")
ab.write(str(len(a3)) + " sentences" +"\n")
for i in xrange(len(a3)):
    ab.write(a3[i] +"\n"+"~~~~~~~~~~~"+"\n")
ab.write("\n")
####################################################

ab.write("Introduction"+"   "+str(search)+"---------------------------------------------------------------------------")
ab.write(str(len(introduction3)) + " sentences" +"\n"+"\n")

for i in xrange(len(introduction3)):
    ab.write(introduction3[i] +"\n"+"~~~~~~~~~~~"+"\n")
ab.write("\n")
####################################################

ab.write("Method"+"   "+str(search) +"---------------------------------------------------------------------------------")
ab.write(str(len(method3)) + " sentences" +"\n"+"\n")

for i in xrange(len(method3)):
    ab.write(method3[i] +"\n"+"~~~~~~~~~~~"+"\n")
ab.write("\n")
####################################################

ab.write("Result"+"   "+str(search) +"---------------------------------------------------------------------------------")
ab.write(str(len(result3)) + " sentences" +"\n"+"\n")

for i in xrange(len(result3)):
    ab.write(result3[i] +"\n"+"~~~~~~~~~~~"+"\n") 
ab.write("\n")
####################################################

ab.write("Discussion"+"   "+str(search) +"-----------------------------------------------------------------------------")
ab.write(str(len(discussion3)) + " sentences" +"\n"+"\n")

for i in xrange(len(discussion3)):
    ab.write(discussion3[i] +"\n"+"~~~~~~~~~~~"+"\n") 


ab.close()
