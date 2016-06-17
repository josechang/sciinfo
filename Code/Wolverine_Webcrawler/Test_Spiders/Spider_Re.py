import re

def find(pattern, string):
	match = re.search(pattern,string)
	if match: print match.group()
	else: print "not find"

pat = '\w*\.\pdf'
str = 'https://example.com/book/title/abcd.pdf'
find(pat, str)
