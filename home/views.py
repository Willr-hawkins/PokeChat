from django.shortcuts import render, get_object_or_404, reverse, redirect, HttpResponseRedirect
from django.contrib.auth.decorators import login_required

# Imported models and forms
from .models import Post, PostComment
from .forms import PostForm, UpdateStatusForm, CommentForm
from profiles.models import UserProfile

def published_posts(request):
    """
    View to return a list of all posts with a status = 1.
    """
    posts = Post.objects.filter(status=1).order_by('-created_on')
    form = CommentForm()

    context = {
        'posts': posts,
        'form': form,
    }
    
    return render(request, 'home/index.html', context)

@login_required
def add_post(request):
    """
    A view to return the PostForm so users can add thier posts.
    """
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect(reverse('home'))
    else:
        form = PostForm()

    # Get the users profile image for the post preview.
    user_profile = UserProfile.objects.get(user=request.user)
    
    template = 'home/add_post.html'
    context = {
        'form': form,
        'profile_image': user_profile.profile_image,
    }

    return render(request, template, context)

@login_required
def delete_post(request, post_id):
    """
    Delete a post is the user is post.author.
    """
    post = get_object_or_404(Post, id=post_id, author=request.user)

    if request.method == 'POST':
        post.delete()
        return redirect(reverse('profile'))

    context = {
        'post': post,
    }

    return render(request, 'home/delete_post.html', context)

@login_required
def change_post_status(request, post_id):
    """
    Change the status on a post if the user is post.author.
    """
    post = get_object_or_404(Post, id=post_id, author=request.user)

    if request.method == 'POST':
        form = UpdateStatusForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect(reverse('profile'))
    else:
        form = UpdateStatusForm(instance=post)
    
    context = {
        'post': post,
        'form': form,
    }

    return render(request, 'home/post_status.html', context)

@login_required
def post_comment(request, post_id):
    """
    A view to leave a comment on a post.
    """
    post = get_object_or_404(Post, id=post_id)

    if request.method == 'POST':
        print("POST Data:", request.POST)
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.comment_author = request.user
            comment.post = post
            comment.save()
            next_url = request.POST.get('next', reverse('home'))
            return HttpResponseRedirect(next_url)
        else:
            print("Form Errors:", form.errors)
    else:
        form = CommentForm()

    context = {
        'post': post,
        'form': form,
    }

    return render(request, 'home/index.html', context)
    