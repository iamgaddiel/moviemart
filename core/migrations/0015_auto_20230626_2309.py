# Generated by Django 2.2.26 on 2023-06-26 23:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0014_auto_20230626_2235'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='movie_type',
            field=models.CharField(default='Movie', max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='movie',
            name='realse_data',
            field=models.DateField(null=True),
        ),
    ]
