
#!/bin/bash

#####################################################
# 
#  I put the file in ~/django/src means to count the # of words of articles and add a line at the bottom of that article.
# Editor: Sunny Tseng
#
TXT_DIR=~/django_image/src/Article_txt/
PROGaRAM_DIR=~/nordron-sciinfo/Code/Sunny_transient
for f in `find $TXT_DIR*.txt`
do
    echo "Converting $(basename $f) "
    python $PROGRAM_DIR/countWordnumber.py $f
done



