from django.shortcuts import render
from .models import Fortune

def fortune(request):
    fortunes = Fortune.objects.all()
    return render(request, "fortunes/fortune.html", {"fortunes": fortunes})
