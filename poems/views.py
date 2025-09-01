import random
from django.shortcuts import render , get_object_or_404
from django.http import JsonResponse
from .models import Poems

def poems(request):
    all_poems = Poems.objects.all()
    poem = random.choice(all_poems) if all_poems else None
    context = {'poem': poem}
    return render(request, "poems/poems.html" , context)

def random_poem(request):
    all_poems = Poems.objects.all()
    poem = random.choice(all_poems) if all_poems else None
    
    if poem:
        data = {
            "title": poem.title,
            "text": poem.poem_text,
        }
    else:
        data = {"error": "هیچ شعری پیدا نشد."}

    return JsonResponse(data)

def poem_detail(request, pk):
    """نمایش جزئیات کامل یک شعر"""
    poem = get_object_or_404(Poems, pk=pk)
    return render(request, "poems/poem_detail.html", {"poem": poem})

def next_poem_api(request):
    """برگرداندن یک شعر رندوم به صورت JSON"""
    poems = Poems.objects.all()
    if not poems.exists():
        return JsonResponse({"error": "هیچ شعری موجود نیست."}, status=404)

    poem = random.choice(list(poems))
    return JsonResponse({
        "id": poem.id,
        "title": poem.title,
        "text": poem.poem_text,
    })