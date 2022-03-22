from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.shortcuts import render
from .models import News

class HomeListView(ListView):
    model = News
    context_object_name = 'news'
    template_name = 'index.html'

class NewDetailView(DetailView):
    model = News
    context_object_name = 'new'
    template_name = 'new.html'
    

def category(request):
    return render(request, 'category.html', context={})

def about(request):
    return render(request, 'about-us.html', context={})

def contact(request):
    return render(request, 'contact.html', context={})
    
def post(request):
    return render(request, 'single-post.html', context={})