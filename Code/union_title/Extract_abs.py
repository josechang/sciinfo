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
# Set the Path
##############################################

path = os.path.abspath(os.getcwd())

# Path to directory where KDD files are
TESTDIR = os.path.normpath(os.path.join(os.path.expanduser("~"),"Desktop","KDD_15","docs"))      

# Establish an empty list to append filenames as we iterate over the directory with filenames
files = []

###############################################
# Create the directory we will write the .txt files to after stripping text
###############################################

# path where KDD journal files exist on disk or cloud drive access
corpuspath = os.path.normpath(os.path.expanduser('~/Desktop/KDD_corpus/'))
if not os.path.exists(corpuspath):
    os.mkdir(corpuspath)

#Set the database abou txt
kddcorpus= nltk.corpus.PlaintextCorpusReader(corpuspath, '.*\.txt')

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
            section2=["Categories and Subject Descriptors","Categories & Subject Descriptors","Keywords","INTRODUCTION"]
            text = kddcorpus.raw(docnum)
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

######################################
#lists
######################################
texts = []
metas2= []

# We need the top section

DATA_DIR="C:\Users\user\Desktop\KDD_corpus"
for filename in os.listdir(DATA_DIR):
    try:
        metas2.append(abpull(filename)[filename]['abstract'])
    except KeyError:
        pass
    
print metas2[3]
