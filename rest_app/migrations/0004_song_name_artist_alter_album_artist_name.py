# Generated by Django 4.2.6 on 2023-10-29 13:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rest_app', '0003_artist_name_album_artist_name_song_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='song',
            name='name_artist',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='rest_app.artist', verbose_name='Имя артиста'),
        ),
        migrations.AlterField(
            model_name='album',
            name='artist_name',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='albums', to='rest_app.artist', verbose_name='Имя исполнителя'),
        ),
    ]
