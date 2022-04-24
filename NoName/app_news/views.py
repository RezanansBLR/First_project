from datetime import datetime
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.shortcuts import render
from .models import News, Category

class HomeListView(ListView):
    model = News
    context_object_name = 'news'
    template_name = 'app_news/index.html'

    def get_context_data(self):
        context = super().get_context_data()
        context['last_adds'] = News.objects.order_by('datetime')[:3]
        context['cats'] = Category.objects.all()
        return context

class NewDetailView(DetailView):
    model = News
    context_object_name = 'new'
    template_name = 'app_news/new.html'
    

class NewsCatListView(ListView):
    model = News
    context_object_name = 'newscat'
    template_name = 'app_news/category.html'

    def get_queryset(self, **kwargs):
        qs = News.objects.filter(category__slug=self.kwargs['slug'])
        return qs
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cat'] = Category.objects.get(slug=self.kwargs['slug'])
        context['date'] = datetime.today()
        return context

def about(request):
    return render(request, 'app_news/about-us.html', context={})

def contact(request):
    return render(request, 'app_news/contact.html', context={})
    
def post(request):
    return render(request, 'app_news/single-post.html', context={})