import urlparse
import urllib
import subprocess
import re
from bs4 import BeautifulSoup

url = "http://eric.ed.gov/?q=a&ft=on&pg=__"
wget = "wget -nc -P ./pdfs "
urls = []
pdfs = []

def geturllist(url, offset, numpage):
	for i in range(1, numpage):
		offsetstring = str(offset*i)
		curl = url.replace('__', offsetstring) 
		urls.append(curl)
	print urls


def getpdflist():
	i = 1
	while len(urls) > 0:
        	try:
                	htmltext = urllib.urlopen(urls[0]).read()
        	except:
                	print "done loading pdf links!!"

		#Output htmls
		#with open("test%s.html" % i, 'w') as f:
			#f.write(htmltext)
		#i += 1

        	soup = BeautifulSoup(htmltext, 'html.parser')
        	urls.pop(0)
        	print len(urls)

		repdf = re.compile('.*pdf')
		#for tag in soup.find_all('a', string=re.compile(".pdf"),  href=True):
		for tag in soup.find_all('a',  href=True):
			if repdf.match(tag['href']):
               			pdfs.append(tag['href'])
	for item in pdfs:
		with open("pdfs.txt", 'w') as p:
			p.write("%s\n" % item)
	#print pdfs
	print len(pdfs)

def getpdffiles():
	while len(pdfs) > 0:
		try:
			wpdf = wget+pdfs[0]
		except:
			print "done downloading files!!"

		subprocess.call(wpdf, shell=True)
		print len(pdfs)
		pdfs.pop(0)


geturllist(url, offset = 1, numpage = 670)
getpdflist()
#getpdffiles()




	#for tag in soup.findAll('a', href=True):
	#	tag['href'] = urlparse.urljoin(url, tag['href'])
	#	if url in tag['href'] and tag['href'] not in visited:
	#		urls.append(tag['href'])
	#		visited.append(tag['href'])

#print visited
