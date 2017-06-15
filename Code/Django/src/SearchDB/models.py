# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Article(models.Model):
    # Define number of columns for this table
    filename = models.CharField(max_length = 255)
    content = models.TextField()
    title = models.CharField(max_length = 255)
    doi = models.URLField(max_length = 128)
    def __str__(self):
        # Define the model name
        return self.filename
