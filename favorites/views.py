from django.shortcuts import redirect, render, get_object_or_404
from poems.models import Poems

def favorites(request):
    """نمایش لیست علاقه‌مندی‌ها از روی session"""
    favorite_ids = request.session.get("favorites", [])
    favorites = Poems.objects.filter(id__in=favorite_ids)
    return render(request, "favorites/favorites.html", {"favorites": favorites})


def add_to_favorites(request, poem_id):
    """افزودن شعر به علاقه‌مندی‌ها"""
    poem = get_object_or_404(Poems, id=poem_id)
    
    favorites = request.session.get("favorites", [])
    if poem.id not in favorites:
        favorites.append(poem.id)
        request.session["favorites"] = favorites
    
    return redirect("favorites")


def remove_from_favorites(request, poem_id):
    """حذف شعر از علاقه‌مندی‌ها"""
    favorites = request.session.get("favorites", [])
    if poem_id in favorites:
        favorites.remove(poem_id)
        request.session["favorites"] = favorites
    
    return redirect("favorites")
