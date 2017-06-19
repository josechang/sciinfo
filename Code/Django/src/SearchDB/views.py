# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404, render_to_response, redirect
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.contrib.postgres.search import SearchQuery, SearchRank, SearchVector
from django.conf import settings
#import article model
from .models import Article


#import modules for vector space convert, similarity, title extraction
import logging
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

# Define path and filename for gensim
PDF_PATH = getattr(settings, 'PDF_PATH', os.path.join(settings.BASE_DIR, 'Article_pdf/'))
TXT_PATH = getattr(settings, 'TXT_PATH', os.path.join(settings.BASE_DIR, 'Article_txt/'))
TMP_PATH = getattr(settings, 'TMP_PATH', os.path.join(settings.BASE_DIR, 'tmp/'))
tmpName = 'deerwester'

# Create your views here.
def get_text(request):
    # if the search bar gets query, redirect to the result page, using GET method
    if 'search' in request.GET:

        # Access the database to do searching
        article_all = Article.objects.all()
        vector = SearchVector('content', weight='A')
        query = SearchQuery(str(request.GET['search']))
        uq = request.GET['search']

        # implement searching function and ranks
        sims = similarity_compare(uq, os.listdir(TXT_PATH), TMP_PATH, TMP_PATH, TMP_PATH, tmpName)
        resultlist = []
        for i in range(0,len(sims)):
            result = Article.objects.get(filename = sims[i][0])
            resultlist.append(result.filename, sims[i][1])
            
        # return uq, resultlist to result.html
        return render_to_response('SearchDB/result.html', {'uq': uq ,'resultlist': resultlist})

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

    # If size changed, refresh dict and mm files
    # Using diff of list for current prototype
    # Using numpy for better performance in the future
    if len(sql_filename) is not len(local_filename):
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
    return redirect('/sciinfo/')