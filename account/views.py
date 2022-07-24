from django.http import HttpResponse
from django.shortcuts import render

def profile(request):
    return HttpResponse('Profile')
