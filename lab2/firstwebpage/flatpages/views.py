from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, 'templates/static_handler.html')


def hello(request):
    return HttpResponse("Привет, Мир!")
