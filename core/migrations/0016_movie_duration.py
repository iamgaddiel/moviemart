# Generated by Django 2.2.26 on 2023-06-27 00:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0015_auto_20230626_2309'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='duration',
            field=models.CharField(default='', help_text='duration of movie', max_length=30),
        ),
    ]