from pyPdf import PdfFileReader

def dimension(arr, list):
    for i in arr:
        for j in i:
            if(j == []):
                list.append(j)
            else:
                dimension(j, list)

f = open('y.pdf', 'rb')
p = PdfFileReader(f)
o = p.getOutlines()

list = []
dimension(o, list)

'''
list = []
list.append(1)
if(list == []):
    print "hello"
'''

'''
dimension(o, list)
for i in list:
    for j in i:
        print j
'''

'''

test = len(o)
print outline
print test
#test =outline[0]
#outline = outline["/Title"]
#print outline
'''

