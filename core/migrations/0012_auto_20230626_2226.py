# Generated by Django 2.2.26 on 2023-06-26 22:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0011_auto_20230626_2223'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='movie_tags',
            field=models.CharField(help_text='seprate tags with a "/"', max_length=300),
        ),
    ]
