from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

def home_page_view(request):
    return HttpResponse("Hello, World!")

def home(request):
    template = loader.get_template('pages/maintemplate.html')
    return HttpResponse(template.render())

def react(request):
    template = loader.get_template('pages/index.html')
    return HttpResponse(template.render())
