from django.http import HttpResponse
from django.shortcuts import render
import requests
import json

# Create your views here.

def demo(request):
    # context = {"page_title": "This is Product Page"}
    # return render(request, 'Owner_Book/home.html', context)
    html = f"<html><body><h1>This is Mobile Page Custom.</h1></body></html>"
    return HttpResponse(html)
