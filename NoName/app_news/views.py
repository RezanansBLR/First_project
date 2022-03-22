from django.shortcuts import render

def test_view(request):  
    return render(request, 'index.html', context={})

def category(request):
    return render(request, 'category.html', context={})

def about(request):
    return render(request, 'about-us.html', context={})

def contact(request):
    return render(request, 'contact.html', context={})
    
def post(request):
    return render(request, 'single-post.html', context={})