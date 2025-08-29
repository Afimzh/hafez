from django.shortcuts import render
from django.http import HttpResponse , JsonResponse

def users(request):
    return HttpResponse("Users Page")

# Create your views here.
