# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404, render_to_response
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.contrib.postgres.search import SearchQuery, SearchRank, SearchVector

from .models import Article
from .forms import TextForm

#import vector_space_convert_cp1 as vc
#import transformation_cp1 as tf
#import similarity_cp1 as sim

# Create your views here.
def get_text(request):

    # if the search bar gets query, direct to result page, using GET method
    if 'search' in request.GET:
        # Access the database to do searching
        article_all = Article.objects.all()
        vector = SearchVector('content', weight='A')
        query = SearchQuery(str(request.GET['search']))
        uq = request.GET['search']

        # implement searching function and ranks
        #vc.vecter_space_convert(article_all)
        #tf.transformation()
        #rank_score = sim.similarity_compare(query)
        result = Article.objects.annotate(rank=SearchRank(vector, query)).filter(rank__gte=0.3).order_by('-rank')
        resultlist = []
        for i in result:
            resultlist.append(i)
        return render_to_response('SearchDB/result.html', {'uq': uq ,'resultlist': resultlist})

    else:
        return render_to_response('SearchDB/search.html')
