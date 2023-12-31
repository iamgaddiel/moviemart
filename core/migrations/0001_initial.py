# Generated by Django 2.2.26 on 2023-06-23 03:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('created', models.DateTimeField(auto_created=True)),
                ('id', models.UUIDField(editable=False, primary_key=True, serialize=False, unique=True)),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('x480', models.FileField(upload_to='media/movies/torrents')),
                ('x720', models.FileField(upload_to='media/movies/torrents')),
                ('x1080', models.FileField(upload_to='media/movies/torrents')),
                ('movie_link', models.URLField()),
                ('thumbnail', models.ImageField(upload_to='media/movie/thumbnails')),
                ('realse_year', models.CharField(max_length=5)),
            ],
        ),
    ]
