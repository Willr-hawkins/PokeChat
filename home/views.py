from django.shortcuts import render, get_object_or_404, reverse
from .models import Post

def published_posts(request):
    """ View to return a list of all posts with a status = 1. """
    posts = Post.objects.filter(status=1).order_by('-created_on')
    
    return render(request, 'home/index.html', {'posts': posts})