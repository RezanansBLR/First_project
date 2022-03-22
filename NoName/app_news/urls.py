from django.urls import path
from .views import about, contact, test_view, category, post, new

urlpatterns = [
    path('',test_view, name="home"),
    path('new/', new, name='new'),
    path('cat/', category, name='category'),
    path('about/', about, name='about'),
    path('contact/', contact, name='contact'),
    path('single-post/', post, name='post'),
]