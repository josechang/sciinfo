#!/bin/bash
DATA_DIR=~/nordron-sciinfo/Code/Django/src/Article_pdf/
TXT_DIR=~/nordron-sciinfo/Code/Django/src/Article_txt
PROGRAM_DIR=~/nordron-sciinfo/Code/Django/src/


for f in `find $DATA_DIR*.pdf`
do
    echo "Converting $(basename $f) "
    pdfx $f -t -o $TXT_DIR/$(echo $(basename $f) | cut -f 1 -d '.').txt
    #sleep 5s
    python $PROGRAM_DIR/countWordnumber.py $TXT_DIR/$(echo $(basename $f) | cut -f 1 -d '.').txt
done


