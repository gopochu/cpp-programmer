from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, "index.html")


def info(request):
    return render(request, "info.html")


def about(request):
    return render(request, "about.html")


def contact(request):
    return HttpResponse('Контакты')