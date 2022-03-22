from django.shortcuts import render
from .models import News

def test_view(request):
    news = News.objects.all()
    return render(request, 'index.html', context={'news': news})

def new(request):
    news = News.objects.all()
    return render(request, 'new.html', context={'news': news[0]})

def category(request):
    return render(request, 'category.html', context={})

def about(request):
    return render(request, 'about-us.html', context={})

def contact(request):
    return render(request, 'contact.html', context={})
    
def post(request):
    return render(request, 'single-post.html', context={})