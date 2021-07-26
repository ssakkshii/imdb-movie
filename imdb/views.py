"""
Views that handle requests and return responses
"""

from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, DjangoModelPermissions
from rest_framework import filters
from imdb.models import Directors, Genres, Movies
from imdb.serializers import DirectorSerializer, GenreSerializer, MovieSerializer


class DirectorsViewSet(viewsets.ModelViewSet):

    queryset = Directors.objects.all()
    serializer_class = DirectorSerializer
    permission_classes = [IsAuthenticated, DjangoModelPermissions]


class GenresViewSet(viewsets.ModelViewSet):

    queryset = Genres.objects.all()
    serializer_class = GenreSerializer
    permission_classes = [IsAuthenticated, DjangoModelPermissions]


class MoviesViewSet(viewsets.ModelViewSet):

    filter_backends = (filters.SearchFilter, DjangoFilterBackend)
    search_fields = ['name', 'director__name']
    filterset_fields = ['genre', 'director']
    queryset = Movies.objects.all()
    serializer_class = MovieSerializer
    permission_classes = [IsAuthenticated, DjangoModelPermissions]
