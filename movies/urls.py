from django.conf.urls import url

from movies.views import MovieListView

urlpatterns = [
    url('/', MovieListView.as_view(), name='movie-list'),
]