from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

def home_page_view(request):
    return HttpResponse("Hello, World!")

def home(request):
    template = loader.get_template('pages/home.html')
    return HttpResponse(template.render())
