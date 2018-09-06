# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import os
from django.shortcuts import render
from django.conf.settings import PROJECT_ROOT

class MovieListView(request):
	"""listing the movies"""
	model = Movie
	def getAllMovies(self, arg):
		moviesFile = open(os.path.join(PROJECT_ROOT, 'movies.txt'))
		moviesList =moviesFile.readlines()
		for m in moviesList:
			print (m)
		return render(request,'movies/movie-list.html')  