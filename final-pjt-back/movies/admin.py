from django.contrib import admin
from .models import Movie, Rank
# Register your models here.

class MovieAdmin(admin.ModelAdmin):
    list_display = ['id', 'title']
class RankAdmin(admin.ModelAdmin):
    list_display = ['id', 'movie', 'score', 'content', 'user', 'username']

admin.site.register(Movie, MovieAdmin)
admin.site.register(Rank, RankAdmin)