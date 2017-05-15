# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Article(models.Model):
    filename = models.CharField(max_length = 255)
    content = models.TextField()
    title = models.CharField(max_length = 255)
    def __str__(self):
        return self.filename
