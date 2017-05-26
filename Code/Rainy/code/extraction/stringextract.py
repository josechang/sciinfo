import re

text = 'AAA1234ZZZuijjk'

m = re.search('1234', text)
found = m.group(0)
print found

#m = re.match('he', 'hello')
#found = m.group(0)
#print found
