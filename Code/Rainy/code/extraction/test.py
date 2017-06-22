import title_extraction_cp1 as title_extractor
import os
path = "C:\Users\Wu\Desktop/100article"
os.chdir(path)
filename=os.listdir(".")
title_extractor(path, filename)
