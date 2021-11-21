from django.shortcuts import get_list_or_404, get_object_or_404, render
from rest_framework.response import Response
from .models import Movie
from .serializers import MovieListSerializers, MovieSerializers
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
# Create your views here.

@api_view(['GET'])
@permission_classes([AllowAny])
def index(request, page):
    # movies = get_list_or_404(Movie.objects.order_by(''))
    # https://wayhome25.github.io/django/2017/03/01/django-99-my-first-project-5/ 참조
    movies = get_list_or_404(Movie)
    serializers = MovieListSerializers(movies, many=True)
    return Response(serializers.data[(page-1)*5:page*5])


@api_view(['GET'])
@permission_classes([AllowAny])
def movie_detail(request, movie_pk):
     movie = get_object_or_404(Movie, pk=movie_pk)
     serializer = MovieSerializers(movie)
     return Response(serializer.data)

