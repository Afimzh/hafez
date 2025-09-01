from django.urls import path
from . import views

urlpatterns = [
    path('', views.poems, name='poems'),
    path("poems/", views.poems, name="poems"),
    path("poems/random/", views.random_poem, name="random_poem"),
    path("poems/<int:pk>/", views.poem_detail, name="poem_detail"),
    path("api/next/", views.next_poem_api, name="next_poem_api"),
]