# Generated by Django 2.2.26 on 2023-06-26 22:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_moviesuggestion_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='movie_tags',
            field=models.TextField(default='', max_length=300),
            preserve_default=False,
        ),
    ]
