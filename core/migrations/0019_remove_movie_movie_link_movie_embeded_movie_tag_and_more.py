# Generated by Django 4.2.2 on 2023-07-02 22:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0018_auto_20230627_0028'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movie',
            name='movie_link',
        ),
        migrations.AddField(
            model_name='movie',
            name='embeded_movie_tag',
            field=models.CharField(default='', max_length=500, unique=True),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='Reviews',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
