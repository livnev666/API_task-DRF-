from rest_framework import serializers
from .models import *


class AlbumSerialiser(serializers.ModelSerializer):

    """Список альбомов"""

    class Meta:
        model = Album
        fields = ['name', 'year_of_release']


class SongSerializer(serializers.ModelSerializer):

    """Список песен"""

    class Meta:
        model = Song
        fields = ['name', 'number_song_album']


class ArtistSerializer(serializers.ModelSerializer):

    """Список артистов"""

    class Meta:
        model = Artist
        fields = ['name']


class AlbumDetailSerializer(serializers.ModelSerializer):

    song = SongSerializer(many=True)

    class Meta:
        model = Album
        fields = ['name', 'year_of_release', 'song']


class ArtistDetailSerializer(serializers.ModelSerializer):

    albums = AlbumDetailSerializer(many=True)

    class Meta:
        model = Artist
        fields = ['name', 'albums']


class SongDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = Song
        fields = '__all__'
