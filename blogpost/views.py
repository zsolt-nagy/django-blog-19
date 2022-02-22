from django.shortcuts import render
from .models import Blogpost

# Create your views here.
def blogposts(request):
    blogposts = Blogpost.objects.all()
    context = { 
        'blogposts': blogposts,
        'page_title': 'JavaScript Blog Home',
    }    
    return render(request, 'blogposts.html', context)

def base(request):
    context = {
        'page_title': 'JavaScript blog with every word capitalized'
    }
    return render(request, 'base.html', context)

