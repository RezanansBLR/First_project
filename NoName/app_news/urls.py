from django.urls import path
from .views import NewDetailView, about, contact, HomeListView, category, post

urlpatterns = [
    path('', HomeListView.as_view(), name="home"),
    path('new/<slug:slug>/', NewDetailView.as_view(), name='new'),
    path('cat/', category, name='category'),
    path('about/', about, name='about'),
    path('contact/', contact, name='contact'),
    path('single-post/', post, name='post'),
]