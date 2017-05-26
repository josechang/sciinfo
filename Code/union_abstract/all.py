import textract
#text1 = textract.process('file_1.pdf', method='pdfminer')
text1 = textract.process('file_1.pdf', m='pdfminer')
text2 = textract.process('file_2.pdf', m='pdfminer')
text3 = textract.process('file_3.pdf', m='pdfminer')

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

xml1=open('pdf_1.txt','w')

for i in xrange(len(text1)):
    xml1.write(text1[i])

xml1.close()

xml2=open('pdf_2.txt','w')

for i in xrange(len(text2)):
    xml2.write(text2[i])

xml2.close()


xml3=open('pdf_3.txt','w')

for i in xrange(len(text3)):
    xml3.write(text3[i])

xml3.close()


myfile1 = open("pdf_1.txt")
myfile2 = open("pdf_2.txt")
myfile3 = open("pdf_3.txt")

a1=[]
a2=[]
a3=[]

c1=0
for i in myfile1.readlines():

  if(abstract_start(i)):
     c1+=1
  elif(abstract_end(i) or abstract_end(i.strip()[0:8])):
     c1=0

  if c1 > 0 :
     a1.append(i)

c2=0
for i in myfile2.readlines():

  if(abstract_start(i)):
     c2+=1
  elif(abstract_end(i) or abstract_end(i.strip()[0:8])):
     c2=0

  if c2 > 0 :
     a2.append(i)

c3=0
for i in myfile3.readlines():

  if(abstract_start(i)):
     c3+=1
  elif(abstract_end(i) or abstract_end(i.strip()[0:8])):
     c3=0

  if c3 > 0 :
     a3.append(i)



ab=open('abstract_all.txt','w')

ab.write("file-1"+"\n")
for i in xrange(len(a1)):
   ab.write(a1[i])

ab.write("\n"+"\n")


ab.write("file-2"+"\n")
for i in xrange(len(a2)):
   ab.write(a2[i])

ab.write("\n"+"\n")

ab.write("file-3"+"\n")
for i in xrange(len(a3)):
   ab.write(a3[i])

ab.write("\n"+"\n")

ab.close()
