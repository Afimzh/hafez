from django.shortcuts import render
from django.http import HttpResponse , JsonResponse , HttpResponseRedirect
from users.forms import CustomerForm

def users(request):
    if request.method == "POST":
        form = CustomerForm(request.POST)
        if form.is_valid():
            return HttpResponseRedirect("/users/")
    else:
        form = CustomerForm()
    
    return render(request, "users/users.html", {"form": form})    
        
