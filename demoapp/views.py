from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def homeapp(request):
    return HttpResponse("This is first app")