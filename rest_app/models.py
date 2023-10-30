from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Album(models.Model):

    """Альбом"""

    name = models.CharField()
    year_of_release = models.PositiveSmallIntegerField(verbose_name='Год выхода')
    artist_name = models.ForeignKey('Artist', on_delete=models.CASCADE,
                                    null=True, verbose_name='Имя исполнителя', related_name='albums')
    name_song = models.ForeignKey('Song', on_delete=models.CASCADE, null=True, blank=True,
                                  verbose_name='Название песни', related_name='num')

    def __str__(self):
        return f'{self.name} {self.year_of_release}'


class Song(models.Model):

    """Песня"""

    name = models.CharField(max_length=100, verbose_name='Название песни')
    number_of_albums = models.ForeignKey(Album, on_delete=models.CASCADE,
                                         null=True, verbose_name='Из альбома', related_name='song')
    number_song_album = models.PositiveIntegerField(null=True, default=0,
                                                    verbose_name='Порядковый номер в альбоме')
    name_artist = models.ForeignKey('Artist', on_delete=models.CASCADE, null=True, blank=True,
                                    verbose_name='Имя артиста')

    def __str__(self):
        return f'{self.name}'


class Artist(models.Model):

    """Исполнитель"""

    name = models.CharField(max_length=100, verbose_name='Название исполнителя')
    name_album = models.ForeignKey(Album, on_delete=models.CASCADE,
                                   null=True, blank=True, verbose_name='Название альбома')
    name_song = models.ForeignKey(Song, on_delete=models.CASCADE, null=True, blank=True,
                                  verbose_name='Название песни')
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, verbose_name='Пользователь')

    def __str__(self):
        return f'{self.name}'
