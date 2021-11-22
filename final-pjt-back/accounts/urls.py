from django.urls import path
from . import views
from rest_framework_jwt.views import obtain_jwt_token

app_name = 'accounts'

urlpatterns = [
    path('signup/', views.signup),
    path('<int:user_pk>/', views.get_username),
    path('<int:user_pk>/rank/', views.get_rank),
    path('<int:user_pk>/article/', views.get_article),
    path('<int:user_pk>/comment/', views.get_comment),
    path('api-token-auth/', obtain_jwt_token),
]
