###########################################
#
#  Delete the final line of txt file
#  Editor: Sunny Tseng
#
#
########################################
from sys import argv
import os

script, filename = argv


os.system('sed -i "$ d" {0}'.format(filename))
 
#with open(filename, 'r+') as f:
#    lines = f.readlines()
#    lines = lines[:-1]
#    f.close()
