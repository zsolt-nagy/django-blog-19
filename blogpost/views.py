from django.shortcuts import render
from .models import Blogpost

# Create your views here.
def blogposts(request):
    blogposts = Blogpost.objects.all()
    count = blogposts.count()
    context = { 
        'blogposts': blogposts,
        'count': count,
    }    
    return render(request, 'blogposts.html', context)

