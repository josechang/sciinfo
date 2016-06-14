import textract
text = textract.process('file_1.pdf', method='pdfminer')


def abstract_start(a):

    arr=['ABSTRACT']
    
    if(a.strip().upper() in arr):     
        return 1
    else:
        return 0

def abstract_end(a):
    arr=['INTRODUCTION','KEYWORDS','CATEGORI']
    
    if(a.strip().upper() in arr):     
        return 1
    else:
        return 0
    

xml=open('pdf_1.txt','w')

for i in xrange(len(text)):
    xml.write(text[i])
xml.close()


myfile = open("pdf_1.txt")
a1=[]

c=0

for i in myfile.readlines():
    
  if(abstract_start(i)):
     c+=1
  elif(abstract_end(i) or abstract_end(i.strip()[0:8])):
     c=0
     
  if c > 0 :
     a1.append(i)


ab=open('abstract_1.txt','w')

for i in xrange(len(a1)):
    ab.write(a1[i])
ab.close()


      
     
