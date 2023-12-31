# Generated by Django 4.2.6 on 2023-10-29 12:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rest_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='song',
            name='number_song_album',
            field=models.PositiveIntegerField(default=0, null=True, verbose_name='Порядковый номер в альбоме'),
        ),
        migrations.AlterField(
            model_name='song',
            name='number_of_albums',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='rest_app.album', verbose_name='Из альбома'),
        ),
    ]
