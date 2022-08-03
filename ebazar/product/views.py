from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def product_home(request):
    # context = {"page_title": "This is Product Page"}
    # return render(request, 'Owner_Book/home.html', context)
    return HttpResponse("<html><body><h1>This is Product Page.</h1></body></html>")