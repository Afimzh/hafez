from django.shortcuts import render
from django.http import HttpResponse , JsonResponse

def fortune(request):
    return HttpResponse("Fortune Page")


# Create your views here.
