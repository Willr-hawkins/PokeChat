from django.urls import path
from . import views

urlpatterns = [
    path('', views.published_posts, name='home'),
    path('add_post/', views.add_post, name='add_post'),
]