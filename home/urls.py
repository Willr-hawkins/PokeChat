from django.urls import path
from . import views

urlpatterns = [
    path('', views.published_posts, name='home'),
    path('add_post/', views.add_post, name='add_post'),
    path('delete_post/<int:post_id>/', views.delete_post, name='delete_post'),
    path('edit_status/<int:post_id>/', views.change_post_status, name='edit_status'),
    path('commnet/<int:post_id>/', views.post_comment, name='add_comment'),
    path('delete_comment/<int:comment_id>/', views.delete_comment, name='delete_comment'),
    path('edit_comment/<int:comment_id>/', views.edit_comment, name='edit_comment'),
]