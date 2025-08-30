from django.contrib import admin
from .models import Fortune

admin.site.register(Fortune)

class FortuneAdmin(admin.ModelAdmin):
    list_display = ["id"]

