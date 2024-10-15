from django.shortcuts import render

def home(request):
    """ view to return the home page. """
    return render(request, 'home/index.html')