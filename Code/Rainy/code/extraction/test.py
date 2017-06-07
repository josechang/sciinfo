from pyPdf import PdfFileReader
import numpy as np
f = open('file_1.pdf', 'rb')
p = PdfFileReader(f)
o = p.getOutlines()
outline = o[1][2][0]
test = np.array(o)
#print outline
#print test
#test =outline[0]
#outline = outline["/Title"]
#print outline


get_type = type(o[1])
print get_type
if get_type == list:
    pass

'''
for i in o:
    if type(i)=='list'
        print "ok"
'''
