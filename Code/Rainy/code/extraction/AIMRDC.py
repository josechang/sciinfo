import textract
#article1 = textract.process('file_1.pdf', method='pdfminer')
article1 = textract.process('file_1.pdf', m='pdfminer')
#text2 = textract.process('file_2.pdf', m='pdfminer')
#text3 = textract.process('file_3.pdf', m='pdfminer')

###########################################
#define the start and the end of the abstract part
###########################################
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
###########################################
#define the start and the end of the introduction part
###########################################
def introduction_start(a):
    arr=['1.INTRODUCTION','I.INTRODUCTION','INTRODUCTION','1. INTRODUCTION']

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
###########################################
#define the start and the end of the theory part
###########################################def theoretical_start(a):
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
###########################################
#define the start and the end of the method part
###########################################

def method_start(a):
    arr=["II.METHODS","METHODS","2.METHODS","MATERIAL","EXPERIME"]

    if(a.strip().upper() in arr):
        return 1
    else:
        return 0

def method_end(a):
    arr=["III.RESULTS","RESULTS","3.RESULTS"]

    if(a.strip().upper() in arr):
        return 1
    else:
        return 0
###########################################
#define the start and the end of the result part
###########################################

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

###########################################
#define the start and the end of the discussion part
###########################################
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
###########################################
#define the start and the end of the conclusion part
###########################################

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


#-------------------------------------------------------------
###########################################
#build a txt file which contains all in article1
###########################################
xml1=open('pdf_1.txt','w')

for i in xrange(len(article1)):
    xml1.write(article1[i])

xml1.close()

# xml2=open('pdf_2.txt','w')
#
# for i in xrange(len(text2)):
#     xml2.write(text2[i])
#
# xml2.close()


# xml3=open('pdf_3.txt','w')
#
# for i in xrange(len(text3)):
#     xml3.write(text3[i])
#
# xml3.close()


myfile1 = open("pdf_1.txt")
# myfile2 = open("pdf_2.txt")
# myfile3 = open("pdf_3.txt")

a1=[]
a2=[]
a3=[]
a4=[]
a5=[]
a6=[]

c1=0
for i in myfile1.readlines():

  if(abstract_start(i)):
     c1+=1
  elif(abstract_end(i) or abstract_end(i.strip()[0:8])):
     c1=0

  if c1 > 0 :
     a1.append(i)

c2=0
for i in myfile1.readlines():

  if(introduction_start(i)):
     c2+=1
  elif(introduction_end(i) or introduction_end(i.strip()[0:8])):
     c2=0

  if c2 > 0 :
     a2.append(i)
#
# c3=0
# for i in myfile3.readlines():
#
#   if(abstract_start(i)):
#      c3+=1
#   elif(abstract_end(i) or abstract_end(i.strip()[0:8])):
#      c3=0
#
#   if c3 > 0 :
#      a3.append(i)



ab=open('abstract1.txt','w')

ab.write("file-1"+"\n")
for i in xrange(len(a1)):
   ab.write(a1[i])

ab.write("\n"+"\n")


intr= open('introduction1.txt','w')
ab.write("file-2"+"\n")
for i in xrange(len(a2)):
   ab.write(a2[i])

# ab.write("\n"+"\n")
#
# ab.write("file-3"+"\n")
# for i in xrange(len(a3)):
#    ab.write(a3[i])
#
# ab.write("\n"+"\n")

ab.close()
