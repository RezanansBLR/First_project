from django.urls import path
from .views import NewDetailView, NewsCatListView, HomeListView, post, about, contact

urlpatterns = [
    path('', HomeListView.as_view(), name="home"),
    path('new/<slug:slug>/', NewDetailView.as_view(), name='new'),
    path('cat/<slug:slug>/', NewsCatListView.as_view(), name='category'),
    path('about/', about, name='about'),
    path('contact/', contact, name='contact'),
    path('single-post/', post, name='post'),
]