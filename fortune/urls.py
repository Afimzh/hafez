from django.urls import path
from . import views

urlpatterns = [
    path('', views.fortune, name='fortune'),
    path("random-fortune/", views.random_fortune, name="random_fortune"),
]