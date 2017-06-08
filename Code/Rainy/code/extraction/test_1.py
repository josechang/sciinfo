from pyPdf import PdfFileReader

def dimension(arr, list):
    for i in arr:
        if type(i) != type(list):
            list.append(i)
        else:
            dimension(i, list)



f = open('y.pdf', 'rb')
p = PdfFileReader(f)
o = p.getOutlines()

list = []
dimension(o, list)



#for j in range(0,len(list)):
#    print list[j]

doc = p.getDocumentInfo()
print doc
