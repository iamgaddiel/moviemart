# Generated by Django 2.2.26 on 2023-06-23 05:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20230623_0512'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='trailer_link',
            field=models.URLField(default=''),
            preserve_default=False,
        ),
    ]