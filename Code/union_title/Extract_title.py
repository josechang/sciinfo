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

###################
# extract title
###################

# Using metacharacters vice literal matches
p=re.compile('^(.*)([\s]){2}[A-z]+[\s]+[\s]?.+')

def titlepull(docnum):
    text = kddcorpus.raw(docnum)
    title_test=re.search('^(.*)[\s]+[\s]?(.*)?',kddcorpus.raw(docnum)).group(1).strip()+" "+re.search('^(.*)[\s]+[\s]?(.*)?',kddcorpus.raw(docnum)).group(2).strip()
    return title_test

#####################
#test
#####################

######################################
#lists
######################################
metas3=[]
# We need the top section
DATA_DIR="C:\Users\user\Desktop\KDD_corpus"
for filename in os.listdir(DATA_DIR):
    metas3.append(titlepull(filename))


print metas3[2]
