from django.contrib import admin
from .models import *

# Register your models here.


@admin.register(Artist)
class ArtistAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    list_display_links = ['name']
    ordering = ['id']


@admin.register(Album)
class AlbumAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'year_of_release']
    list_display_links = ['name']
    ordering = ['id']


@admin.register(Song)
class SongAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'number_of_albums', 'number_song_album']
    list_display_links = ['name']
    ordering = ['id']
