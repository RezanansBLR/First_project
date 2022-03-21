from django.shortcuts import render

def test_view(request):
    return render(request, 'index.html', context={})