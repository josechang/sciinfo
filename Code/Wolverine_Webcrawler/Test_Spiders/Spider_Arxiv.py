import urlparse
import urllib
import urllib2
import subprocess
import re
from bs4 import BeautifulSoup

url = "http://eric.ed.gov/?q=a&ft=on"
urls = []
pdfs = []

def geturllist(url, offset, numpage):
	for i in range(0, numpage):
		offsetstring = str(offset*i)
		curl = url.replace('__', offsetstring) 
		urls.append(curl)


def getpdflist():
	while len(urls) > 0:
        	try:
                	htmltext = urllib.urlopen(urls[0]).read()
        	except:
                	print "done loading pdf links!!"

        	soup = BeautifulSoup(htmltext, 'html.parser')
        	urls.pop(0)
        	print len(urls)

        for tag in soup.find_all('a', string=re.compile('.pdf'), href = True, limit=50):
                pdfs.append(tag['href'])


def getpdffiles():
	while len(pdfs) > 0:
		try:
			wpdf = wget+pdfs[0]
		except:
			print "done downloading files!!"

		subprocess.call(wpdf, shell=True)
		pdfs.pop(0)
		print len(pdfs)


htmltext = urllib.urlopen(url).read()
with open("test.html", 'w') as f:
	f.write(htmltext)


	#for tag in soup.findAll('a', href=True):
	#	tag['href'] = urlparse.urljoin(url, tag['href'])
	#	if url in tag['href'] and tag['href'] not in visited:
	#		urls.append(tag['href'])
	#		visited.append(tag['href'])

#print visited
