# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404, render_to_response, redirect
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.contrib.postgres.search import SearchQuery, SearchRank, SearchVector

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
from pprint import pprint
from six import iteritems

from vector_space_convert_cp1 import file_read, vector_space_convert
from transformation_cp1 import transformation
from similarity_cp1 import similarity_compare

# Create your views here.

#Define path and filename
ArticlePath = '../Article_txt/'
tmpPath = '../tmp'
tmpName = 'deerwester'

def get_text(request):

    # if the search bar gets query, redirect to the result page, using GET method
    if 'search' in request.GET:
        # Access the database to do searching
        article_all = Article.objects.all()
        vector = SearchVector('content', weight='A')
        query = SearchQuery(str(request.GET['search']))
        uq = request.GET['search']

        # implement searching function and ranks
        sims = similarity_compare(uq, tmpPath, tmpPath, tmpPath, tmpName)
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
    if not os.path.exists(tmpPath):
        os.mkdirs(tmpPath)

    # If size changed, refresh dict and mm files
    if len(Article.objects.all()) is not len(os.listdir(ArticlePath)):
        vector_space_convert(ArticlePath, tmpPath, tmpPath, tmpName)
        transformation(tmpPath, tmpPath, tmpPath, tmpName)

    return redirect('/sciinfo/')