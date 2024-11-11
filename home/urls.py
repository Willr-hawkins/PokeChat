from django.urls import path
from . import views

urlpatterns = [
    path('', views.published_posts, name='home'),
    path('add_post/', views.add_post, name='add_post'),
    path('delete/<int:post_id>/', views.delete_post, name='delete_post'),
    path('edit_status/<int:post_id>/', views.change_post_status, name='edit_status'),
]