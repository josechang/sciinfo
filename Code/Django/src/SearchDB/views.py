# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404, render_to_response, redirect
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.contrib.postgres.search import SearchQuery, SearchRank, SearchVector
from django.conf import settings
#import article model
from .models import Article


#import modules for vector space convert and similarity
import logging
import os
import codecs
import re
from gensim import corpora, models, similarities
from stop_words import get_stop_words
from collections import defaultdict
from six import iteritems
from vector_space_convert_cp1 import file_read, vector_space_convert
from transformation_cp1 import transformation
from similarity_cp1 import similarity_compare

# Define path and filename for gensim
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
            resultlist.append(result)
            
        # return uq, resultlist to result.html
        return render_to_response('SearchDB/result.html', {'uq': uq ,'resultlist': resultlist})

    else:
        return render_to_response('SearchDB/search.html')

def refreshDatabase(request):
    #Create path if it doesn't exist
    if not os.path.exists(TMP_PATH):
        os.mkdirs(TMP_PATH)

    # If size changed, refresh dict and mm files
    if len(Article.objects.all()) is not len(os.listdir(TXT_PATH)):
        vector_space_convert(TXT_PATH, TMP_PATH, TMP_PATH, tmpName)
        transformation(TMP_PATH, TMP_PATH, TMP_PATH, tmpName)

    return redirect('/sciinfo/')