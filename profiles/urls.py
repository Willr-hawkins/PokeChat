from django.urls import path
from . import views
from home.views import post_comment

urlpatterns = [
    path('first_login_redirect/', views.first_login_redirect, name='first_login_redirect'),
    path('create_profile', views.create_profile, name='create_profile'),
    path('profile/', views.profile_view, name='profile'),
    path('comment/<int:post_id>/', post_comment, name='post_comment'),
    path('search/', views.search_profiles, name='search_profiles'),
    path('profile/<str:username>/', views.profile_detail, name='profile_detail'),
]