from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.contrib.auth.decorators import login_required

#Imported models and forms
from .models import UserProfile
from .forms import UserProfileForm
from home.models import Post
from home.forms import CommentForm

def first_login_redirect(request):
    """
    A view that checks if it is ther users first time logging in.
    If so to redirect them to the create profile page.
    """
    if UserProfile.objects.filter(user=request.user).exists():
        return redirect(reverse('profile'))
    else:
        return redirect(reverse('create_profile'))

def create_profile(request):
    """
    A view to return the UserProfileForm so users can
    interact with the site.
    """

    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = request.user
            profile.save()
            return redirect(reverse('home'))
    else:
        form = UserProfileForm()
    
    template = 'profiles/create_profile.html'
    context = {
        'form': form,
    }

    return render (request, template, context)

@login_required
def profile_view(request):
    """
    A view to display the current logged in user's profile page.
    """
    profile = get_object_or_404(UserProfile, user=request.user)
    posts = Post.objects.filter(author=profile.user)
    form = CommentForm()

    template = 'profiles/profile.html'
    context = {
        'profile': profile,
        'posts': posts,
        'form': form,
    }

    return render(request, template, context)

def search_profiles(request):
    """
    Allow users to search for another user via thier username.
    """
    query = request.GET.get('q', '')
    profiles = UserProfile.objects.select_related('user')

    if query:
        profiles = profiles.filter(
            user__username__icontains=query
        ) | profiles.filter(
            user__first_name__icontains=query
        ) | profiles.filter(
            user__last_name__icontains=query
        )

    context = {
        'profiles': profiles,
        'query': query,
    }

    return render(request, 'profiles/search_profiles.html', context)

def profile_detail(request, username):
    """
    Show the users profile once it has been searched for.
    """

    profile = get_object_or_404(UserProfile, user__username=username)
    posts = Post.objects.filter(author=profile.user, status=1)
    form = CommentForm()

    context = {
        'profile': profile,
        'posts': posts,
        'form': form,
    }

    return render(request, 'profiles/profile.html', context)