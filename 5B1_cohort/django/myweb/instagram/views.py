from django.shortcuts import render
from django.http.response import HttpResponse

# Create your views here.


def welcome(request):
    return HttpResponse("<h1>Simple view<h1>")
    

def post(request):
    return HttpResponse("<h1>individual post<h1>")

def contact(request):
    return HttpResponse("<h1>contact us<h1>")

def about(request):
    return HttpResponse("<h1>about us<h1>")

def blog(request):
    return HttpResponse("<h1>blog post<h1>")
