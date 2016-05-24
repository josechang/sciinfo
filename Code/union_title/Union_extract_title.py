##############################################
# Administrative code: Import what we need
##############################################
import os
import time
from os import walk

###############################################
# Set the Path
##############################################

path = os.path.abspath(os.getcwd())

# Path to directory where KDD files are
TESTDIR = os.path.normpath(os.path.join(os.path.expanduser("~"),"Desktop","KDD_15","docs"))

# Establish an empty list to append filenames as we iterate over the directory with filenames
files = []


###############################################
# Code to iterate over files in directory
##############################################

'''Iterate over the directory of filenames and add to list.  
Inspection shows our target filenames begin with 'p' and end with 'pdf' '''

for dirName, subdirList, fileList in os.walk(TESTDIR):
    for fileName in fileList:
        if fileName.startswith('p') and fileName.endswith('.pdf'):
            files.append(fileName)
end_time = time.time()

###############################################
# Output
###############################################

print len(files) # Print the number of files

###############################################
# Importing what we need
###############################################

import string
import unicodedata
import subprocess
import nltk
import os, os.path
import re

###############################################
# Create the directory we will write the .txt files to after stripping text
###############################################

# path where KDD journal files exist on disk or cloud drive access
corpuspath = os.path.normpath(os.path.expanduser('~/Desktop/KDD_corpus/'))
if not os.path.exists(corpuspath):
    os.mkdir(corpuspath)

###############################################
# Core code to iterate over files in the directory
###############################################

# We start from the code to iterate over the files timeit

for dirName, subdirList, fileList in os.walk(TESTDIR):
    for fileName in fileList:
        if fileName.startswith('p') and fileName.endswith('.pdf'):
            if os.path.exists(os.path.normpath(os.path.join(corpuspath,fileName.split(".")[0]+".txt"))):
                pass
            else:

                try:
                    document = filter(lambda x: x in string.printable,unicodedata.normalize('NFKD', (unicode(subprocess.check_output(['pdf2txt.py',str(os.path.normpath(os.path.join(TESTDIR,fileName)))],shell=True),errors='ignore'))).encode('ascii','ignore').decode('unicode_escape').encode('ascii','ignore'))
                except UnicodeDecodeError:
                    document = unicodedata.normalize('NFKD',unicode(subprocess.check_output(['pdf2txt.py',str(os.path.normpath(os.path.join(TESTDIR,fileName)))], shell=True),errors='ignore')).encode('ascii','ignore')    

                if len(document)<300:
                    pass
                else:
                    # used this for assistance http://stackoverflow.com/questions/2967194/open-in-python-does-not-create-a-file-if-it-doesnt-exist
                    if not os.path.exists(os.path.normpath(os.path.join(corpuspath,fileName.split(".")[0]+".txt"))):
                        file = open(os.path.normpath(os.path.join(corpuspath,fileName.split(".")[0]+".txt")), 'w+')
                        file.write(document)
                    else:
                        pass

kddcorpus= nltk.corpus.PlaintextCorpusReader(corpuspath, '.*\.txt')

# Mapping, setting count to zero for start
wordcount = 0

#Iterating over list and files and counting length
for fileid in kddcorpus.fileids():
    wordcount += len(kddcorpus.words(fileid))
print wordcount

# Using metacharacters vice literal matches
p=re.compile('^(.*)([\s]){2}[A-z]+[\s]+[\s]?.+')

for fileid in kddcorpus.fileids()[:25]:
    print re.search('^(.*)[\s]+[\s]?(.*)?',kddcorpus.raw(fileid)).group(1).strip()+" "+re.search('^(.*)[\s]+[\s]?(.*)?',kddcorpus.raw(fileid)).group(2).strip()

#######################
#extract abstract
#######################

def abpull(docnum=None,section='abstract',full = False):

    ans={}
    failids = []
    section = section.lower()    
    if docnum is None and full == False:
        raise BaseException("Enter target file to extract data from")

    if docnum is None and full == True:

        text=kddcorpus.raw(docnum).lower()
        # to return output from entire corpus
        if full == True:
            for fileid in kddcorpus.fileids():
                text = kddcorpus.raw(fileid)
                if section == "abstract":
                    section1=["ABSTRACT", "Abstract "]
                    target = ""   
                    section2=["Categories and Subject Descriptors","Categories & Subject Descriptors","Keywords","INTRODUCTION"]
                    for fileid in kddcorpus.fileids():
                        text = kddcorpus.raw(fileid)


                        for sect1 in section1:
                            for sect2 in section2:
                                part1= "(?<="+str(sect1)+")(.+)"
                                part2 = "(?="+str(sect2)+")"
                                p = re.compile(part1+part2)
                                try:
                                    target=p.search(re.sub('[\s]'," ",text)).group()
                                    if len(target) > 50:
                                        ans[str(fileid)]={}
                                        ans[str(fileid)]["abstract"]=target.strip()
                                        ans[str(fileid)]["charcount"]=len(target)
                                        #print [fileid,len(target),len(text)]
                                        break
                                    else:
                                        failids.append(fileid)
                                        pass
                                except AttributeError:
                                    pass 

            return ans

        # to return output from one document
    else:
        ans = {}
        failids=[]
        text = kddcorpus.raw(docnum).lower()
        if section == "abstract":
            section1=["ABSTRACT", "Abstract "]
            target = ""   
            section2=["Categories and Subject Descriptors","Categories & Subject Descriptors","Keywords","INTRODUCTION","Author Keywords"]
            for sect1 in section1:
                for sect2 in section2:
                    part1= "(?<="+str(sect1)+")(.+?)"
                    part2 = "(?="+str(sect2)+"[\s]?)"
                    p = re.compile(part1+part2)
                    try:
                        target=p.search(re.sub('[\s]'," ",text)).group()
                        if len(target) > 50:
                            ans[str(docnum)]={}
                            ans[str(docnum)]["abstract"]=target.strip()
                            ans[str(docnum)]["charcount"]=len(target)
                            #print [docnum,len(target),len(text)]
                            break
                        else:
                            failids.append(docnum)
                            pass
                    except AttributeError:
                        pass
        return ans
        return failids

test=abpull(full=True)
import itertools
import collections

