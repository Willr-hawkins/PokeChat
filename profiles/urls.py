from django.urls import path
from . import views

urlpatterns = [
    path('first_login_redirect/', views.first_login_redirect, name='first_login_redirect'),
    path('create_profile', views.create_profile, name='create_profile'),
    path('profile/', views.profile_view, name='profile'),
]