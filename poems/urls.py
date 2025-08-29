from django.urls import path
from . import views

urlpatterns = [
    path('', views.poems, name='poems'),
]