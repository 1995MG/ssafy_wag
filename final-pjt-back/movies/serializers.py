from rest_framework import serializers
# from rest_framework.exceptions import MethodNotAllowed
from .models import Movie, Rank

class MovieListSerializers(serializers.ModelSerializer):

    class Meta:
        model = Movie
        fields = '__all__'

class MovieSerializers(serializers.ModelSerializer):

    class Meta:
        model = Movie
        fields = '__all__'

class RankListSerializers(serializers.ModelSerializer):
    created_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M", read_only=True)
    class Meta:
        model = Rank
        fields = '__all__'

class RankSerializers(serializers.ModelSerializer):
    created_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M", read_only=True)
    class Meta:
        model = Rank
        fields = ('score', 'content', 'user', 'movie', 'username', 'id')
