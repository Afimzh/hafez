from django.shortcuts import render
from django.http import HttpResponse , JsonResponse 

def poems(request):
    return HttpResponse("Poems Page")

