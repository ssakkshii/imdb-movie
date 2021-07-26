"""
imdb-movie Serializers
"""

from rest_framework import serializers
from imdb.models import Directors, Genres, Movies


class DirectorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Directors
        fields = '__all__'


class GenreSerializer(serializers.ModelSerializer):

    class Meta:
        model = Genres
        fields = '__all__'


class MovieSerializer(serializers.ModelSerializer):

    class Meta:
        model = Movies
        fields = '__all__'
