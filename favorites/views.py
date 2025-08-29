from django.shortcuts import render
from django.http import HttpResponse , JsonResponse

def favorites(request):
    return HttpResponse("Favorites Page")

# Create your views here.
