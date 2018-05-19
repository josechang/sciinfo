# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from vocabulary.vocabulary import Vocabulary as vb
from django.shortcuts import render, render_to_response, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.postgres.search import SearchQuery, SearchRank, SearchVector
from django.conf import settings
# import article model
from .models import Article


# import modules for vector space convert, similarity, title extraction
import logging
import codecs
import io
import os
import codecs
import re
from gensim import corpora, models, similarities
# 匯入斷字、斷字處理等等手續都在vector_space_convert_cp1、transformation_cp1
#Use "vector_space_convert_cp1" & "transformation_cp1" to tokenize
from stop_words import get_stop_words
from collections import defaultdict
from six import iteritems
from pyPdf import PdfFileWriter, PdfFileReader
from vector_space_convert_cp1 import file_read, vector_space_convert
from transformation_cp1 import transformation
from similarity_cp1 import similarity_compare
from result_of_year import year_similarity_compare
from title_extraction_cp1 import title_extractor
from doi_extract_cp1 import doi_extract
from Synonym_finder import get_syn
# from synonym_finder_wordnet_v1 import get_syn


# import charts
from fusioncharts import FusionCharts
import json

# Define path and filename for gensim
PDF_PATH = getattr(settings, 'PDF_PATH', os.path.join(
    settings.BASE_DIR, 'Article_pdf/'))
TXT_PATH = getattr(settings, 'TXT_PATH', os.path.join(
    settings.BASE_DIR, 'Article_txt/'))
ABSTRACT_PATH = getattr(settings, 'ABSTRACT_PATH', os.path.join(
    settings.BASE_DIR, 'Article_abstract/'))
TMP_PATH = getattr(settings, 'TMP_PATH',
                   os.path.join(settings.BASE_DIR, 'tmp/'))
tmpName = 'deerwester'

# Create your views here.


def get_text(request):
    # if the search bar gets query, redirect to the result page,
    # using GET method
    if 'q' in request.GET and 'check' in request.GET:

        # Access the database to do searching
        article_all = Article.objects.all()
        vector = SearchVector('content', weight='A')
        query = SearchQuery(str(request.GET['q']))
        uq = request.GET['q']

        synonym = get_syn(uq)
        teststr = "Got the message"

        sims = similarity_compare(uq, os.listdir(
            TXT_PATH), TMP_PATH, TMP_PATH, TMP_PATH, tmpName)
        # implement searching function and ranks
        yearsort = year_similarity_compare(uq, os.listdir(
            TXT_PATH), TMP_PATH, TMP_PATH, TMP_PATH, tmpName)

        year_all = []
        year_simus = []
        # create list and sorting similarity for each year
        for i in range(len(yearsort)):
            year_all.append(yearsort[i][2])
        
        year_max = max(year_all)
        year_min = min(year_all)
        
        for i in range(year_max, year_min, -1):
            tmp = []
            for j in range(0, len(yearsort)):
                if i == yearsort[j][2]:
                    tmp.append(
                        [yearsort[j][0], yearsort[j][1], yearsort[j][2]])
            tmp = sorted(tmp, key=lambda item: -item[1])
            for k in range(0, len(tmp)):
                result = Article.objects.get(filename=tmp[k][0])
                year_simus.append([result.filename, tmp[k][1], tmp[k][2]])

        resultlist = []
        abstract = []
        for i in range(0, len(year_simus)):
            result = Article.objects.get(filename=year_simus[i][0])
            file_open = codecs.open(
                ABSTRACT_PATH + result.filename.replace(".txt", "abstract.txt"), 'r', encoding='utf-8')
            read_file = file_open.read()
            abstract.append([(read_file)])

            file_open.close()
            with open(TXT_PATH + str(result.filename), "r") as f:
                for line in f:
                    pass
                print line  # this is the last line of the file
            resultlist.append([str(result.filename), year_simus[i][1]])
        fig_year = year_chart(year_simus)
        fig = chart(sims)
        # return uq, resultlist to result.html
        return render_to_response('SearchDB/result.html', {'uq': uq, 'resultlist': resultlist, 'fig': fig, 'fig_year': fig_year, 'abstract': abstract, 'synonym': synonym})

    elif 'q' in request.GET:

        # Access the database to do searching
        article_all = Article.objects.all()
        vector = SearchVector('content', weight='A')
        query = SearchQuery(str(request.GET['q']))
        uq = request.GET['q']

        synonym = get_syn(uq)
        teststr = "Got the message"

        # implement searching function and ranks
        sims = similarity_compare(uq, os.listdir(
            TXT_PATH), TMP_PATH, TMP_PATH, TMP_PATH, tmpName)
        resultlist = []
        abstract = []
        for i in range(0, len(sims)):
                    # Get abstract from Article_abstract file and append it
                    # to abstract list.
            result = Article.objects.get(filename=sims[i][0])
            file_open = codecs.open(
                ABSTRACT_PATH + result.filename.replace(".txt", "abstract.txt"), 'r', encoding='utf-8')
            read_file = file_open.read()
            abstract.append([(read_file)])

            file_open.close()
            with open(TXT_PATH + str(result.filename), "r") as f:
                for line in f:
                    pass
                print line  # this is the last line of the file
            resultlist.append([str(result.filename), sims[i][1], line])
        fig = chart(sims)
        fig_year = chart(sims)
        # return uq, resultlist to result.html
        return render_to_response('SearchDB/result.html', {'uq': uq, 'resultlist': resultlist, 'fig': fig, 'fig_year': fig_year, 'abstract': abstract, 'synonym': synonym})

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
            # y = year_extractor(PDF_PATH, pdf_filename)
            d = doi_extract(PDF_PATH, pdf_filename)
            Article.objects.create(
                filename=fname, content=f.read(), title=t, doi=d)
            f.close()
    return redirect('/')

# Year chart function


def year_chart(article_info):

    # Initialize list for counting articles of different
    # percentage   #0517 add
    year = [0, 0, 0, 0, 0]
    d = []  # 0517 add
    for i in range(len(article_info)):
        d.append(article_info[i][2])
    big = max(d)
    small = min(d)
    interval = (big-small+1)/5
    for i in range(len(article_info)):
        if article_info[i][2] >= big-interval+1:
            year[0] += 1
        if article_info[i][2] <= big-interval and article_info[i][2] >= big-2*interval+1:
            year[1] += 1
        if article_info[i][2] <= big-2*interval and article_info[i][2] >= big-3*interval+1:
            year[2] += 1
        if article_info[i][2] <= big-3*interval and article_info[i][2] >= big-4*interval+1:
            year[3] += 1
        if article_info[i][2] <= big-4*interval:
            year[4] += 1

# Create an object for the column2d chart using the FusionCharts
# class constructor #0517 add
    I1 = str(eval('big'))
    I2 = str(eval('big-interval'))
    I3 = str(eval('big-2*interval'))
    I4 = str(eval('big-3*interval'))
    I5 = str(eval('big-4*interval'))
    I6 = str(eval('small'))
    I21 = I1+'-'+str(eval('big-interval+1'))
    I32 = I2+'-'+str(eval('big-2*interval+1'))
    I43 = I3+'-'+str(eval('big-3*interval+1'))
    I54 = I4+'-'+str(eval('big-4*interval+1'))
    I65 = I5+'-'+I6
    column2d = FusionCharts("column2d", "ex2", "600", "400", "chart-2", "json",
                            # The data is passed as a string in the
                            # `dataSource` as parameter.
                            {
                                "chart": {
                                    "caption": "Publication year distribution",
                                    "subCaption": "Numbers within each time period",
                                    "xAxisname": "year",
                                    "yAxisName": "No. of articles",
                                    "theme": "zune"
                                },
                                "data": [
                                    {
                                        "label": I21,
                                        "value": year[0]
                                    },
                                    {
                                        "label": I32,
                                        "value": year[1]
                                    },
                                    {
                                        "label": I43,
                                        "value": year[2]
                                    },
                                    {
                                        "label": I54,
                                        "value": year[3]
                                    },
                                    {
                                        "label": I65,
                                        "value": year[4]
                                    },
                                ]
                            })

    # returning complete JavaScript and HTML code, which is used to
    # generate chart in the browsers.
    return column2d.render()

# Chart function


def chart(article_info):

    # Initialize list for counting articles of different percentage
    tmp = [0, 0, 0, 0, 0]
    for element in article_info:
        if element[1] > 0.9:
            tmp[0] += 1
        if element[1] > 0.8 and element[1] <= 0.9:
            tmp[1] += 1
        if element[1] > 0.7 and element[1] <= 0.8:
            tmp[2] += 1
        if element[1] > 0.6 and element[1] <= 0.7:
            tmp[3] += 1
        if element[1] > 0.5 and element[1] <= 0.6:
            tmp[4] += 1

# Create an object for the column2d chart using the
# FusionCharts class constructor
    column2d = FusionCharts("column2d", "ex1", "600", "400", "chart-1", "json",
                            # The data is passed as a
                            # string in the `dataSource` as parameter.
                            {
                                "chart": {
                                    "caption": "Similarity Score distribution",
                                    "xAxisname": "percentage (%)",
                                    "yAxisName": "No. of articles",
                                    "theme": "carbon"
                                },
                                "data": [
                                    {
                                        "label": "91-100",
                                        "value": tmp[0]
                                    },
                                    {
                                        "label": "81-90",
                                        "value": tmp[1]
                                    },
                                    {
                                        "label": "71-80",
                                        "value": tmp[2]
                                    },
                                    {
                                        "label": "61-70",
                                        "value": tmp[3]
                                    },
                                    {
                                        "label": "51-60",
                                        "value": tmp[4]
                                    }
                                ]
                            })

    # returning complete JavaScript and HTML code, which is used to
    # generate chart in the browsers.
    return column2d.render()
