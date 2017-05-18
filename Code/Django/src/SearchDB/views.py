# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404, render_to_response
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.contrib.postgres.search import SearchQuery, SearchRank, SearchVector

from .models import Article
from .forms import TextForm

import imp

vc = imp.load_source('vector_space_convert', '../nordron-sciinfo/Code/Rainy/code/vector_space_convert.py')
vc.MyClass()
sim = imp.load_source('similarity', '../nordron-sciinfo/Code/Rainy/code/similarity.py')
sim.MyClass()
tf = imp.load_source('transformation', '../nordron-sciinfo/Code/Rainy/code/transformation.py')
tf.MyClass()

# Create your views here.
def get_text(request):

    # if the search bar gets query
    if 'user_query' in request.GET:
        # Access the database to do searching
        article_all = Article.objects.all()
        vector = SearchVector('content')
        query = SearchQuery(request.GET['user_query'])

        # implement searching function and ranks
        vc.vecter_space_convert(article_all)
        tf.transformation()
        rank_score = sim.similarity_compare(query)

        return HttpResponse('Your search string is: '+request.GET['user_query'])

    else:
        return render_to_response('SearchDB/search.html', locals())
