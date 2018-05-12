# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, render_to_response, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.postgres.search import SearchQuery, SearchRank, SearchVector
from django.conf import settings
#import article model
from .models import Article


#import modules for vector space convert, similarity, title extraction
import logging
import codecs
import os
import codecs
import re
from gensim import corpora, models, similarities
from stop_words import get_stop_words
from collections import defaultdict
from six import iteritems
from pyPdf import PdfFileWriter, PdfFileReader
from vector_space_convert_cp1 import file_read, vector_space_convert
from transformation_cp1 import transformation
from similarity_cp1 import similarity_compare
from title_extraction_cp1 import title_extractor
from doi_extract_cp1 import doi_extract

# import charts
from fusioncharts import FusionCharts
import json

# Define path and filename for gensim
PDF_PATH = getattr(settings, 'PDF_PATH', os.path.join(settings.BASE_DIR, 'Article_pdf/'))
TXT_PATH = getattr(settings, 'TXT_PATH', os.path.join(settings.BASE_DIR, 'Article_txt/'))
ABSTRACT_PATH = getattr(settings, 'ABSTRACT_PATH', os.path.join(settings.BASE_DIR, 'Article_abstract/'))
TMP_PATH = getattr(settings, 'TMP_PATH', os.path.join(settings.BASE_DIR, 'tmp/'))
tmpName = 'deerwester'

# Create your views here.
def get_text(request):
    # if the search bar gets query, redirect to the result page, using GET method
    if 'q' in request.GET:

        # Access the database to do searching
        article_all = Article.objects.all()
        vector = SearchVector('content', weight='A')
        query = SearchQuery(str(request.GET['q']))
        uq = request.GET['q']
   

        # implement searching function and ranks
        sims = similarity_compare(uq, os.listdir(TXT_PATH), TMP_PATH, TMP_PATH, TMP_PATH, tmpName)
        resultlist = []
        abstract = []
        for i in range(0,len(sims)):
		    #Get abstract from Article_abstract file and append it to abstract list. 
            result = Article.objects.get(filename = sims[i][0]) 
            '''file_open = codecs.open(ABSTRACT_PATH + result.filename.replace(".txt" , "abstract.txt") ,'r', encoding ='utf-8')
            read_file = file_open.read()
            abstract.append([(read_file)])
			 
            file_open.close()'''
	    #with open(TXT_PATH + str(result.filename), "r") as f:
    	        #for line in f: pass
    		#print line #this is the last line of the file
            resultlist.append([str(result.filename), sims[i][1]])
        fig = chart(sims)
        # return uq, resultlist to result.html
        return render_to_response('SearchDB/result.html', {'uq': uq ,'resultlist': resultlist ,'fig': fig , 'abstract' : abstract})
		

    else:
        return render_to_response('SearchDB/search.html')

def refreshDatabase(request):
    # Create a list with filenames in SQL database
    sql_filename = []
    for i in Article.objects.all():
        sql_filename.append(i.filename)

    # Create a list with filenames in local folder
    local_filename = []
    for i in os.listdir(TXT_PATH):
        local_filename.append(i)

    # Create path if it doesn't exist
    if not os.path.exists(TMP_PATH):
        os.mkdir(TMP_PATH)

    if not os.path.exists(ABSTRACT_PATH):
        os.mkdir(ABSTRACT_PATH)
		
    a = open(ABSTRACT_PATH + "test.txt" , 'w')	
    for i in os.listdir(PDF_PATH):
        if not i.replace(".pdf",".abstract.txt") in os.listdir(ABSTRACT_PATH):
            a.write("s")
    a.close()
            
    # If size changed, refresh dict and mm files
    # Using diff of list for current prototype
    # Using numpy for better performance in the future
    if len(local_filename) != len(sql_filename):
        # Dict
        vector_space_convert(TXT_PATH, TMP_PATH, TMP_PATH, tmpName)
        transformation(TMP_PATH, TMP_PATH, TMP_PATH, tmpName)

        # SQL
        diff_filename = [i for i in local_filename if i not in sql_filename]
        for fname in diff_filename:
            # Load txt file, for content
            f = open(TXT_PATH + fname, 'r')

            # Load pdf file, for title
            pdf_filename = fname.replace(".txt", ".pdf")
            t = title_extractor(PDF_PATH, pdf_filename)
            d = doi_extract(PDF_PATH, pdf_filename)
            Article.objects.create(filename=fname, content=f.read(), title=t, doi=d)
            f.close()
    return redirect('/')

# Chart function
def chart(article_info):

# Initialize list for counting articles of different percentage
    tmp = [0, 0, 0, 0, 0]
    for element in article_info:
        if element[1] >= 0.9:
            tmp[0] += 1
        if element[1] >= 0.8 and element[1] <= 0.9:
            tmp[1] += 1
        if element[1] >= 0.7 and element[1] <= 0.8:
            tmp[2] += 1
        if element[1] >= 0.6 and element[1] <= 0.7:
            tmp[3] += 1
        if element[1] >= 0.5 and element[1] <= 0.6:
            tmp[4] += 1

# Create an object for the column2d chart using the FusionCharts class constructor
    column2d = FusionCharts("column2d", "ex1" , "600", "400", "chart-1", "json",
    # The data is passed as a string in the `dataSource` as parameter.
    {
        "chart":{
            "caption":"Similarity Score distribution",
            "xAxisname": "percentage (%)",
            "yAxisName": "no. of article",
            "theme":"carbon"
        },
        "data": [
                {
                    "label": "90-100",
                    "value": tmp[0]
                },
                {
                    "label": "80-90",
                    "value": tmp[1]
                },
                {
                    "label": "70-80",
                    "value": tmp[2]
                },
                {
                    "label": "60-70",
                    "value": tmp[3]
                },
                {
                    "label": "50-60",
                    "value": tmp[4]
                }
        ]
    })

        # returning complete JavaScript and HTML code, which is used to generate chart in the browsers.
    return column2d.render()
