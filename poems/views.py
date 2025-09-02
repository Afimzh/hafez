import random
from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from .models import Poems

def poems(request):
    """نمایش یک شعر رندوم در صفحه اشعار"""
    all_poems = Poems.objects.all()
    poem = random.choice(all_poems) if all_poems else None
    return render(request, "poems/poems.html", {"poem": poem})

def next_poem_api(request):
    """API شعر بعدی (رندوم)"""
    qs = Poems.objects.all()
    if not qs.exists():
        return JsonResponse({"error": "هیچ شعری موجود نیست."}, status=404)
    p = random.choice(list(qs))
    return JsonResponse({"id": p.id, "title": p.title, "text": p.poem_text})

def poem_detail(request, pk):
    """نمایش جزئیات کامل یک شعر"""
    poem = get_object_or_404(Poems, pk=pk)

    # فقط همون شعر نمایش داده بشه
    return render(request, "poems/poem_detail.html", {
        "poem": poem,
    })


def random_poem(request):
    """(اختیاری) API رندوم؛ اگر در جاهای دیگر استفاده می‌کنی"""
    qs = Poems.objects.all()
    if not qs.exists():
        return JsonResponse({"error": "هیچ شعری پیدا نشد."}, status=404)
    p = random.choice(list(qs))
    return JsonResponse({"id": p.id, "title": p.title, "text": p.poem_text})
