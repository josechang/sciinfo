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
        if fileName.startswith('p') and fileName.endswith('.pdf'):   #can be set by our own rule
            files.append(fileName)


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
"""""
p=re.compile('^(.*)([\s]){2}[A-z]+[\s]+[\s]?.+')

for fileid in kddcorpus.fileids()[:25]:
    print re.search('^(.*)[\s]+[\s]?(.*)?',kddcorpus.raw(fileid)).group(1).strip()+" "+re.search('^(.*)[\s]+[\s]?(.*)?',kddcorpus.raw(fileid)).group(2).strip()
"""""

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


#####################################
#top pull
#####################################
def toppull(docnum=None,section='top',full = False):

 
    ans={}
    failids = []
    section = section.lower()    
    if docnum is None and full == False:
        raise BaseException("Enter target file to extract data from")

    if docnum is None and full == True:

        text=kddcorpus.raw(docnum).lower()
        # to return output from entire corpus

        if full == True:
            if section == 'top':
                section = ["ABSTRACT","Abstract","Bio","Panel Summary"]
                for fileid in kddcorpus.fileids():
                    text = kddcorpus.raw(fileid)
                    for sect in section:
                        try:
                            part1="(.+)(?="+sect+")"
                            #print "re.compile"+"("+part1+")"
                            p=re.compile(part1)
                            target = p.search(re.sub('[\s]'," ", text)).group()
                            #print docnum,len(target),len(text)

                            ans[str(fileid)]={}
                            ans[str(fileid)]["top"]=target.strip()
                            ans[str(fileid)]["charcount"]=len(target)
                            #print [fileid,len(target),len(text)]
                            break
                        except AttributeError:
                            failids.append(fileid)
                            pass
        return ans
        return failids

        # to return output from one document
    else:
        ans = {}
        failids=[]
        text = kddcorpus.raw(docnum)

        if section == "top":
            section = ["ABSTRACT","Abstract","Bio","Panel Summary"]
            text = kddcorpus.raw(docnum)
            for sect in section:
                try:
                    part1="(.+)(?="+sect+")"
                    #print "re.compile"+"("+part1+")"
                    p=re.compile(part1)
                    target = p.search(re.sub('[\s]'," ", text)).group()
                    #print docnum,len(target),len(text)

                    ans[str(docnum)]={}
                    ans[str(docnum)]["top"]=target.strip()
                    ans[str(docnum)]["charcount"]=len(target)
                    #print [fileid,len(target),len(text)]
                    break

                except AttributeError:
                    failids.append(docnum)
                    pass

        return ans
        return failids
    
################################
#polyglot
################################
def extraction(corpus):
    import itertools
    import unicodedata
    import polyglot
    from polyglot.text import Text, Word
    

    corpus=corpus
    # extract entities from a single string; remove whitespace characters
    try:
        e=Text(corpus).entities
    except:
        pass
        #e = Text(re.sub("(r'(x0)'," ","(re.sub('[\s]'," ",corpus)))).entities

    current_person =[]
    persons =[]
    current_org=[]
    organizations=[]
    current_loc=[]
    locations=[]

    for l in e:
        if l.tag == 'I-PER':
            for m in l:
                current_person.append(unicodedata.normalize('NFKD', m).encode('ascii','ignore'))
            else:
                if current_person: # if the current chunk is not empty
                    persons.append(" ".join(current_person))
                    current_person = []
        elif l.tag == 'I-ORG':
            for m in l:
                current_org.append(unicodedata.normalize('NFKD', m).encode('ascii','ignore'))
            else:
                if current_org: # if the current chunk is not empty
                    organizations.append(" ".join(current_org))
                    current_org = []
        elif l.tag == 'I-LOC':
            for m in l:
                current_loc.append(unicodedata.normalize('NFKD', m).encode('ascii','ignore'))
            else:
                if current_loc: # if the current chunk is not empty
                    locations.append(" ".join(current_loc))
                    current_loc = []
    results = {}
    results['persons']=persons
    results['organizations']=organizations
    results['locations']=locations

    return results

###########################################
#nltk
###########################################
def nltktreelist(text):
    from operator import itemgetter

    text = text


    persons = []
    organizations = []
    locations =[]
    genpurp = []

    for l in nltk.ne_chunk(nltk.pos_tag(nltk.word_tokenize(text))):
        if isinstance(l,nltk.tree.Tree):
            if l.label() == 'PERSON':
                if len(l)== 1:
                    if l[0][0] in persons:
                        pass
                    else:
                        persons.append(l[0][0])
                else:
                    if " ".join(map(itemgetter(0), l)) in persons:
                        pass
                    else:
                        persons.append(" ".join(map(itemgetter(0), l)).strip("*"))


    for o in nltk.ne_chunk(nltk.pos_tag(nltk.word_tokenize(text))):
        if isinstance(o,nltk.tree.Tree):
            if o.label() == 'ORGANIZATION':
                if len(o)== 1:
                    if o[0][0] in organizations:
                        pass
                    else:
                        organizations.append(o[0][0])
                else:
                    if " ".join(map(itemgetter(0), o)) in organizations:
                        pass
                    else:
                        organizations.append(" ".join(map(itemgetter(0), o)).strip("*"))


    for o in nltk.ne_chunk(nltk.pos_tag(nltk.word_tokenize(text))):
        if isinstance(o,nltk.tree.Tree):
            if o.label() == 'LOCATION':
                if len(o)== 1:
                    if o[0][0] in locations:
                        pass
                    else:
                        locations.append(o[0][0])
                else:
                    if " ".join(map(itemgetter(0), o)) in locations:
                        pass
                    else:
                        locations.append(" ".join(map(itemgetter(0), o)).strip("*"))

    for e in nltk.ne_chunk(nltk.pos_tag(nltk.word_tokenize(text))):
        if isinstance(o,nltk.tree.Tree):
            if o.label() == 'GPE':
                if len(o)== 1:
                    if o[0][0] in genpurp:
                        pass
                    else:
                        genpurp.append(o[0][0])
                else:
                    if " ".join(map(itemgetter(0), o)) in genpurp:
                        pass
                    else:
                        genpurp.append(" ".join(map(itemgetter(0), o)).strip("*"))




    results = {}
    results['persons']=persons
    results['organizations']=organizations
    results['locations']=locations
    results['genpurp'] = genpurp

    return results


###############################################
#Stanford NER
###############################################
"""
def get_continuous_chunks(string):
    string = string
    continuous_chunk = []
    current_chunk = []

    for token, tag in stner.tag(string.split()):
        if tag != "O":
            current_chunk.append((token, tag))
        else:
            if current_chunk: # if the current chunk is not empty
                continuous_chunk.append(current_chunk)
                current_chunk = []
    # Flush the final current_chunk into the continuous_chunk, if any.
    if current_chunk:
        continuous_chunk.append(current_chunk)
    named_entities = continuous_chunk
    named_entities_str = [" ".join([token for token, tag in ne]) for ne in named_entities]
    named_entities_str_tag = [(" ".join([token for token, tag in ne]), ne[0][1]) for ne in named_entities]
    persons = []
    for l in [l.split(",") for l,m in named_entities_str_tag if m == "PERSON"]:
        for m in l:
            for n in m.strip().split(","):
                if len(n)>0:
                    persons.append(n.strip("*"))
    organizations = []
    for l in [l.split(",") for l,m in named_entities_str_tag if m == "ORGANIZATION"]:
        for m in l:
            for n in m.strip().split(","):
                n.strip("*")
                if len(n)>0:
                    organizations.append(n.strip("*"))
    locations = []
    for l in [l.split(",") for l,m in named_entities_str_tag if m == "LOCATION"]:
        for m in l:
            for n in m.strip().split(","):
                if len(n)>0:
                    locations.append(n.strip("*"))
    dates = []
    for l in [l.split(",") for l,m in named_entities_str_tag if m == "DATE"]:
        for m in l:
            for n in m.strip().split(","):
                if len(n)>0:
                    dates.append(n.strip("*"))
    money = []
    for l in [l.split(",") for l,m in named_entities_str_tag if m == "MONEY"]:
        for m in l:
            for n in m.strip().split(","):
                if len(n)>0:
                    money.append(n.strip("*"))
    time = []
    for l in [l.split(",") for l,m in named_entities_str_tag if m == "TIME"]:
        for m in l:
            for n in m.strip().split(","):
                if len(n)>0:
                    money.append(n.strip("*"))

    percent = []
    for l in [l.split(",") for l,m in named_entities_str_tag if m == "PERCENT"]:
        for m in l:
            for n in m.strip().split(","):
                if len(n)>0:
                    money.append(n.strip("*"))

    entities={}
    entities['persons']= persons
    entities['organizations']= organizations
    entities['locations']= locations
    #entities['dates']= dates
    #entities['money']= money
    #entities['time']= time
    #entities['percent']= percent

    return entities
"""
num=len(files)
texts = []
metas1=[]
metas2=[]
# We need the top section
"""
DATA_DIR="C:\Users\user\Desktop\KDD_corpus"
for filename in os.listdir(DATA_DIR):
    texts.append(filename)
    metas1.append(toppull(filename)[filename]['top'])
    metas2.append(abpull(filename)[filename]['abstract'])
"""
print abpull('p6pdf.txt')['p6pdf.txt']['abstract']

###############################################
#  NLTK Standard Chunker
###############################################

#nltkstandard_p4ents = nltktreelist(metas1[3])
#print(nltkstandard_p4ents['persons'])
#print metas2[3]

###############################################
# Polyglot NERC Tool
###############################################


#poly_p4ents = {'top': extraction(p4['top'])}
#print(poly_p4ents['top']['persons'])

###############################################
# Stanford NERC Tool
################################################
"""
import os
java_path = "C:/Program Files/Java/jdk1.8.0_20/bin/java.exe"
os.environ['JAVAHOME'] = java_path

from nltk.tag import StanfordNERTagger, StanfordPOSTagger
stner = StanfordNERTagger('/Users/user/stanford-corenlp-full/classifiers/english.muc.7class.distsim.crf.ser.gz','/Users/user/stanford-corenlp-full/stanford-corenlp-3.6.0.jar',encoding='utf-8')
stpos = StanfordPOSTagger('/Users/user/stanford-postagger-full/models/english-bidirectional-distsim.tagger','/Users/user/stanford-postagger-full/stanford-postagger-3.6.0.jar') 

stan_p4ents = get_continuous_chunks(p4['top'])
print(nltkstandard_p4ents['persons'])
"""     
end_time = time.time()
