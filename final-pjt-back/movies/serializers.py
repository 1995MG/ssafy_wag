from rest_framework import serializers
# from rest_framework.exceptions import MethodNotAllowed
from .models import Movie

class MovieListSerializers(serializers.ModelSerializer):

    class Meta:
        model = Movie
        fields = '__all__'

class MovieSerializers(serializers.ModelSerializer):

    class Meta:
        model = Movie
        fields = '__all__'