import urlparse
import urllib
import subprocess
import re
from bs4 import BeautifulSoup

url = "http://eric.ed.gov/?q=a&ft=on&pg=__"
directory = "./pdfs"
wget = "wget -nc -P " + directory + " "
urls = []
dirs = []
pdfs = []

def geturllist(url, offset, numpage):
	for i in range(1, numpage):
		offsetstring = str(offset*i)
		curl = url.replace('__', offsetstring) 
		urls.append(curl)
	#print urls


def getpdflist():
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
        	print "%s urls remaning..." % len(urls)

		repdf = re.compile("^http.*\.pdf$")
		#for tag in soup.find_all('a', string=re.compile(".pdf"),  href=True):
		for tag in soup.find_all('a',  href=True):
			if repdf.match(tag['href']):
				name = re.search('[^\/]*?\.pdf', tag['href'])
				dirs.append(directory+"/"+name.group())
               			pdfs.append(tag['href'])

	with open("pdfs.txt", 'w') as p:
		for i in range(0, len(pdfs)-1):
			p.write("%s\t%s\n" % (dirs[i], pdfs[i]))
	#print pdfs
	print "Length of dirs: %s" % len(dirs)
	print "Length of pdfs: %s" % len(pdfs)

def getpdffiles():
	while len(pdfs) > 0:
		try:
			wpdf = wget+pdfs[0]
		except:
			print "done downloading files!!"

		subprocess.call(wpdf, shell=True)
		pdfs.pop(0)
		print "%s more pdfs to download" % len(pdfs)


geturllist(url, offset = 1, numpage = 2)
getpdflist()
getpdffiles()




	#for tag in soup.findAll('a', href=True):
	#	tag['href'] = urlparse.urljoin(url, tag['href'])
	#	if url in tag['href'] and tag['href'] not in visited:
	#		urls.append(tag['href'])
	#		visited.append(tag['href'])

#print visited
