#!/bin/bash

for f in *.pdf
do
	echo "Converting $f"
	pdfx $f -t -o ../txt/$(echo $f | cut -f 1 -d '.').txt
done
