# Generated by Django 4.2.2 on 2023-07-02 22:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0019_remove_movie_movie_link_movie_embeded_movie_tag_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movie',
            name='embeded_movie_tag',
        ),
        migrations.AddField(
            model_name='movie',
            name='movie_link',
            field=models.URLField(default=''),
            preserve_default=False,
        ),
    ]
