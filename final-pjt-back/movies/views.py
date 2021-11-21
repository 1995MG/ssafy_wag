from django.shortcuts import get_list_or_404, get_object_or_404, render
from rest_framework import serializers
from rest_framework.response import Response
from .models import Movie
# from .serializers import MovieListSerializers, MovieSerializers
# Create your views here.

def index(request):
    # movies = get_list_or_404(Movie.objects.order_by(''))
    # https://wayhome25.github.io/django/2017/03/01/django-99-my-first-project-5/ 참조
    # movies = get_list_or_404(Movie)
    # serializers = MovieListSerializers(movies, many=True)
    # return Response(serializers.data)
    pass


def movie_detail(request, movie_pk):
    #  movie = get_object_or_404(Movie, pk=movie_pk)
    #  serializer = MovieSerializers(movie)
    #  return Response(serializer.data)
    pass