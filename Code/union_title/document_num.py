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
