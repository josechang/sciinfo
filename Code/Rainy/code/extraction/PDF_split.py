##############################
#extract PDF subheading,
#PDF to txt
#split txt based on subheading
##############################
from pyPdf import PdfFileReader
import textract
import os
import sys

# encoding=utf8
reload(sys)
sys.setdefaultencoding('utf8')

#transfer pdf outlines into a single list
def dimension(arr, list):
    for i in arr:
        if type(i) != type(list):
            list.append(i)
        else:
            dimension(i, list)

#transfer PDF to txt file
def pdftotxt(article):
    xml1=open('pdf_1.txt','w') #open a txt file named pdf_1
    for i in xrange(len(article)):
        xml1.write(article[i])
    xml1.close()

#split txt into small part based on subheading
def split(line,subheading,path):
    part = []
    c = 1
    newpath = path + "/new"
    if not os.path.exists(newpath):
        os.makedirs(newpath)
    os.chdir(newpath)
    for i in range(0,len(subheading)):
        for j in line:
            if j.find(subheading[i])>=0 and len(j)-len(subheading[i])<10:
                c = 1
            if c == 1:
                part.append(j)
            if i+1<len(subheading):
                if j.find(subheading[i+1])>0 and len(j)-len(subheading[i+1])<10:
                    intr = open(subheading[i],'w')
                    for k in xrange(len(part)-1):
                        intr.write(part[k])
                    c=0
                    part=[]
            elif i+1==len(subheading):
                intr = open(subheading[i],'w')
                for k in xrange(len(part)-1):
                    intr.write(part[k])


path = "C:\Users\Wu/nordron-sciinfo\Code\Rainy\code\extraction" #please change path
article = textract.process('y.pdf', m='pdfminer') #please chang the file name
f = open('y.pdf', 'rb') #import PDF file
p = PdfFileReader(f)
o = p.getOutlines()  #read outlines in pdf


list = []
dimension(o, list)
pdftotxt(article)

#build a list of subtitle
subheading = []
for j in range(0,len(list)):
    sub = list[j]["/Title"]
    subheading.append(sub)
#title=title_extractor(path, filename)
myfile = open("pdf_1.txt")
line = myfile.readlines() # read txt file line by line
split(line,subheading,path)
