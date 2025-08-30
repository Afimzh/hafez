from django.shortcuts import render

def favorites(request):
    return render(request, "favorites/favorites.html")
