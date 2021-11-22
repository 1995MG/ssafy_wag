from django.urls import path
from . import views

app_name = 'movies'

urlpatterns = [
    # path('page/<int:page>/', views.index),
    path('', views.index),
    path('<int:movie_pk>/', views.movie_detail),
    path('<int:movie_pk>/rank/', views.rank_list_create),
    path('<int:movie_pk>/rank/<int:rank_pk>/', views.rank_delete),
    path('<int:movie_pk>/rank/<int:rank_pk>/likes/', views.rank_likes),
    # path('recommended/', views.recommended, name='recommended'),
]