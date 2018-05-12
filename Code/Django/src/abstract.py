import pdfx
import io
import os

if not os.path.exists('Article_abstract/'):
    os.mkdir('Article_abstract/')

DATA_DIR = "Article_pdf"
pdf_name = []
for filename in os.listdir(DATA_DIR):
  print(filename)
  if(filename[-4:len(filename)] ==".pdf") :
      
    pdf_name.append(filename)
    pdf = pdfx.PDFx("Article_pdf/" + filename)
    text = pdf.get_text()
    xml=io.open("Article_txt/" + filename.replace(".pdf",".txt"),'w' ,encoding = 'utf8')
    xml.write(text)
    xml.close()


def abstract_start(a):

    arr=["ABSTRACT", "A B S T R A C T"]
	
    c = 0
    for i in range(len(arr)):
      if(arr[i] in a.upper()):
        c = c+1
	
    '''for i in range(len(b)):
      if(b[i].upper() in arr):
        c = c+1;
		
    for i in range(len(d)):
      if(d[i].upper() in arr):
        c = c+1;'''
	
    if(c > 0):     
        return 1
    else:
        return 0

def abstract_end(a):
    arr=['INTRODUCTION','KEYWORDS','CATEGORI','INDEX']
    c = 0
    for i in range(len(arr)):
      if(arr[i] in a.upper()):
        c = c+1;
	
    if(len(a.split()) == 0):
      c = c+1
	
    if(c > 0):     
        return 1
    else:
        return 0
    



for filename in os.listdir("Article_pdf"):
  filename_txt = filename.replace(".pdf",".txt")
  myfile = io.open("Article_txt/" + filename_txt,encoding = 'utf8')
  a1=[]

  c=0

  for i in myfile.readlines():
        
    if(abstract_start(i)):
       c+=1
    elif((abstract_end(i) or abstract_end(i.strip()[0:8])) and c > 0):
       c=0
       if(len(a1) < 10 and c == 0):
         c = c+1
     
    if c > 0 :
       a1.append(i)
       


  ab=io.open("Article_abstract/" + filename_txt.replace(".txt","abstract.txt"),'w' , encoding = 'utf8')

  for i in range(len(a1)):
    ab.write(a1[i])
  ab.close()


      
     
