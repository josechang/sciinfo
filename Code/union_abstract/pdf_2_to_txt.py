import textract
text = textract.process('file_2.pdf', method='pdfminer')


xml=open('pdf_2.txt','w')

for i in xrange(len(text)):
    xml.write(text[i])
xml.close()


myfile = open("pdf_2.txt")
a1=[]

c=0
for i in myfile.readlines():
    
  if(i.strip().upper() == 'ABSTRACT'):
     c+=1
  elif(i.strip() == '' or i.strip()[0:8] == 'Keywords'):
     c=0

  if c > 0 :
     a1.append(i)


ab=open('abstract_2.txt','w')

for i in xrange(len(a1)):
    ab.write(a1[i])
ab.close()


      
     
