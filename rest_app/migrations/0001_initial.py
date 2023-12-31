# Generated by Django 4.2.6 on 2023-10-29 11:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField()),
                ('year_of_release', models.PositiveSmallIntegerField(verbose_name='Год выхода')),
            ],
        ),
        migrations.CreateModel(
            name='Artist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Название исполнителя')),
            ],
        ),
        migrations.CreateModel(
            name='Song',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Название песни')),
                ('number_of_albums', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='rest_app.album', verbose_name='Порядковый номер в альбоме')),
            ],
        ),
        migrations.AddField(
            model_name='album',
            name='artist_name',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='rest_app.artist', verbose_name='Имя исполнителя'),
        ),
    ]
