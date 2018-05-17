#!/bin/bash

for f in *.pdf
do
    echo "Converting $f"
    pdfx $f -t -o ../Article_txt/$(echo $f | cut -f 1 -d '.').txt
    sleep 5s
    python countWordnumber.py ../Article_txt/$(echo $f | cut -f 1 -d '.').txt
done
