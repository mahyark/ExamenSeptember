# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Movie(models.Model):
    movieName = models.CharField(max_length=50)
    actors = models.CharField(max_length=200)