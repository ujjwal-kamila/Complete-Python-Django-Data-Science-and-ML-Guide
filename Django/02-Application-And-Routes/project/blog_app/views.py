from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse('<h1>Blog Home</h1>')

def about(request):
    return HttpResponse('<h1>Blog About</h1>')

def name(request):
    return HttpResponse('<h1>Hiii <br> I am Ujjwal Kamila <br> Python Developer</h1>')
