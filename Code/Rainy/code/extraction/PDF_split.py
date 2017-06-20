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

#split txt file into small part
myfile = open("pdf_1.txt")
part = []
line = myfile.readlines()
c = 0

for i in range(0,len(subheading)):
    for j in line:
        try:
            if j.find(subheading[i])>0 and len(j)-len(subheading[i])<10:
                c = 1
            if c == 1:
                part.append(j)
            if j.find(subheading[i+1])>0 and len(j)-len(subheading[i+1])<10:
                intr = open(subheading[i],'w')
                for i in xrange(len(part)-1):
                    intr.write(part[i])
                c = 0
                part = []
        except:
            print subheading[i]
