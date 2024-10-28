from django.urls import path
from . import views

urlpatterns = [
    path('', views.published_posts, name='home'),
]