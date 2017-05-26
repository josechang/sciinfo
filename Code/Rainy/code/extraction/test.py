import re
a = re.findall(r'\d+', 'US20020164078.pdf.464')
b = str(a)
b = b.replace(',','').replace('[','').replace(']','').replace(' ','').replace("'",'')
print a
print b
