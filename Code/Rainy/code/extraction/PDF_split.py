from pyPdf import PdfFileReader
import textract

def dimension(arr, list):    #transfer pdf outlines into a single list
    for i in arr:
        if type(i) != type(list):
            list.append(i)
        else:
            dimension(i, list)

def split(arr,list): #split all parts baded on subheading
    pass

f = open('y.pdf', 'rb')
p = PdfFileReader(f)
o = p.getOutlines()  #read outlines in pdf

list = []
dimension(o, list)

subheading = []
for j in range(0,len(list)):
    sub = list[j]["/Title"]
    subheading.append(sub) #build a list of subtitle
article = textract.process('y.pdf', m='pdfminer') #read line
split(article,subheading) 
