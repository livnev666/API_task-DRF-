# Generated by Django 4.2.6 on 2023-10-29 13:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rest_app', '0002_song_number_song_album_alter_song_number_of_albums'),
    ]

    operations = [
        migrations.AddField(
            model_name='artist',
            name='name_album',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='rest_app.album', verbose_name='Название альбома'),
        ),
        migrations.AddField(
            model_name='artist',
            name='name_song',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='rest_app.song', verbose_name='Название песни'),
        ),
        migrations.AlterField(
            model_name='album',
            name='artist_name',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='art', to='rest_app.artist', verbose_name='Имя исполнителя'),
        ),
    ]
