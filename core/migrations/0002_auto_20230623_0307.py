# Generated by Django 2.2.26 on 2023-06-23 03:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='created',
            field=models.DateTimeField(auto_created=True, editable=False),
        ),
    ]