# analytics/urls.py
from django.urls import path
from .views import create_post, get_analysis

urlpatterns = [
    path('api/v1/posts/', create_post, name='create_post'),
    path('api/v1/posts/<str:post_id>/analysis/', get_analysis, name='get_analysis'),
]
