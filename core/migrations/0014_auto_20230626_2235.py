# Generated by Django 2.2.26 on 2023-06-26 22:35

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0013_auto_20230626_2228'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='movie',
            name='thumbnail',
            field=models.ImageField(upload_to='thumbnails/%Y/%m/%d'),
        ),
        migrations.AlterField(
            model_name='moviesuggestion',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True),
        ),
    ]