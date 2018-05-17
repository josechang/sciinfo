#!/bin/bash

########################################
#  shell script for transform pdf to txt and count the # of words of articles
# you can put this script anywhere, only be careful to the path
#
# Editor: Sunny Tseng

DATA_DIR=~/nordron-sciinfo/Code/Django/src/Article_pdf/
TXT_DIR=~/nordron-sciinfo/Code/Django/src/Article_txt1
PROGRAM_DIR=~/nordron-sciinfo/Code/Sunny_transient


for f in `find $DATA_DIR*.pdf`
do
    echo "Converting $(basename $f) "
    pdfx $f -t -o $TXT_DIR/$(echo $(basename $f) | cut -f 1 -d '.').txt
    #sleep 5s
    #python $PROGRAM_DIR/countWordnumber.py $TXT_DIR/$(echo $(basename $f) | cut -f 1 -d '.').txt
done


