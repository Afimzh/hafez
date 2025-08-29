from django.contrib import admin
from poems.models import Poems
# Register your m
# odels here.


@admin.register(Poems)
class PoemsAdmin(admin.ModelAdmin):
    list_display = ("id" , "title")
    