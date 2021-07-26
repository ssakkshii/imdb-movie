"""
This file defines the data models tables used in the imdb application.
"""

from django.db import models
from django.db.models import DO_NOTHING


class Directors(models.Model):
    name = models.CharField(max_length=200, unique=True)
    # More director details can be added here

    def __str__(self):
        return self.name


class Genres(models.Model):
    name = models.CharField(max_length=200, unique=True)
    # Additional Genre details can be added here

    def __str__(self):
        return self.name


class Movies(models.Model):
    popularity_99 = models.DecimalField(max_digits=4, decimal_places=1)
    # Assuming that one movie is directed by a  single director
    director = models.ForeignKey(Directors, related_name='movie_director', on_delete=DO_NOTHING)
    genre = models.ManyToManyField(Genres)
    imdb_score = models.DecimalField(max_digits=3, decimal_places=1)
    name = models.CharField(max_length=300, unique=True)

    def __str__(self):
        return self.name
