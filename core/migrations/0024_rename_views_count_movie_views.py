# Generated by Django 4.2.2 on 2023-07-03 17:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0023_alter_movie_rating'),
    ]

    operations = [
        migrations.RenameField(
            model_name='movie',
            old_name='views_count',
            new_name='views',
        ),
    ]
