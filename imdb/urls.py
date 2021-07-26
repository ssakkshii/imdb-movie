"""
Application specific URL Configuration
"""
from django.urls import path, include
from imdb import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register(r'directors', views.DirectorsViewSet)
router.register(r'genres', views.GenresViewSet)
router.register(r'movies', views.MoviesViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
