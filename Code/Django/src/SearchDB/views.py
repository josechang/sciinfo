# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404, render_to_response
from django.http import Http404, HttpResponse, HttpResponseRedirect

from .models import Article
from .forms import TextForm

# Create your views here.
def get_text(request):
    if 'user_query' in request.GET:
        return HttpResponse('Your search string is: '+request.GET['user_query'])
    else:
        return render_to_response('SearchDB/search.html', locals())

def show_text(request):
    if request.method == 'POST':
        form = TextForm(request.POST)
        if form.is_valid():
            return render(request, 'SearchDB/result.html', {'form': form})
