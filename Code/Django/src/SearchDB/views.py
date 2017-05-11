# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404
from django.http import Http404, HttpResponse, HttpResponseRedirect

from .models import Article
from .forms import TextForm

# Create your views here.
def get_text(request):
    if request.method == 'POST':
        form = TextForm(request.POST)

        if form.is_valid():
            return HttpResponseRedirect('/thanks/')
    else:
        form = TextForm()
    return render(request, 'SearchDB/search.html', {'form': form})

def show_text(request):
    if request.method == 'POST':
        form = TextForm(request.POST)
        if form.is_valid():
            return render(request, 'SearchDB/result.html', {'form': form})
