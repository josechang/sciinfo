from pyPdf import PdfFileReader
f = open('file_1.pdf', 'rb')
p = PdfFileReader(f)
o = p.getOutlines()
outline = o[1][2][0]
test = len(o)
print outline
print test
#test =outline[0]
#outline = outline["/Title"]
#print outline
