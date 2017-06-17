##############################
#extract PDF subheading,
#PDF to txt
#split txt based on subheading
##############################

from pyPdf import PdfFileReader


#transfer pdf outlines into a single list
def dimension(arr, list):
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

#build a list of subtitle
subheading = []
for j in range(0,len(list)):
    sub = list[j]["/Title"]
    subheading.append(sub)

myfile = open("pdf_1.txt")
part = []
for i in myfile.readlines():
    print o
