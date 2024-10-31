from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.contrib.auth.decorators import login_required

#Imported models and forms
from .models import UserProfile
from .forms import UserProfileForm

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
        form =UserProfileForm()
    
    template = 'profiles/create_profile.html'
    context = {
        'form': form,
    }

    return render (request, template, context)