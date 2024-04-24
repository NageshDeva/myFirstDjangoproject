from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse("Hello Jango, This is my first project.")


def demo(request):
    return HttpResponse("Day 1 of starting Django.")