from django.urls import path
from . import views
from home.views import post_comment

urlpatterns = [
    path('first_login_redirect/', views.first_login_redirect, name='first_login_redirect'),
    path('create_profile', views.create_profile, name='create_profile'),
    path('profile/', views.profile_view, name='profile'),
    path('comment/<int:post_id>/', post_comment, name='post_comment'),
]