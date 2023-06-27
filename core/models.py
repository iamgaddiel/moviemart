from django.db import models
from django.contrib.auth.models import User
from .validators import validate_file_extension
from django.urls import reverse
import uuid



class Movie(models.Model):
    id = models.UUIDField(primary_key=True, unique=True, editable=False, default=uuid.uuid4)
    title = models.CharField(max_length=100)
    description = models.TextField()
    x_720 = models.FileField(upload_to=f'torrents/%Y/%m/%d', validators=[validate_file_extension], blank=True)
    x_1080 = models.FileField(upload_to=f'torrents/%Y/%m/%d', validators=[validate_file_extension], blank=True)
    x_2160 = models.FileField(upload_to=f'torrents/%Y/%m/%d', validators=[validate_file_extension], blank=True)
    movie_link = models.URLField()
    thumbnail = models.ImageField(upload_to='thumbnails/%Y/%m/%d')
    realse_year = models.CharField(max_length=5)
    is_trending = models.BooleanField(default=False)
    views_count = models.IntegerField(default=0)
    thriller_link = models.URLField()
    movie_tags = models.CharField(max_length=300, help_text='seprate tags with a "/"')
    movie_type = models.CharField(max_length=20)
    realse_data = models.DateField(null=True)
    duration = models.CharField(max_length=30, help_text='duration of movie', default='')



    def __str__(self) -> str:
        return self.title

class MovieSuggestion(models.Model):
    id = models.UUIDField(primary_key=True, unique=True, editable=False, default=uuid.uuid4)
    email = models.EmailField()
    movie_titles = models.TextField(help_text='Enter movie title on a new line')

    def __str__(self) -> str:
        return '{email} suggested'.format(email=self.email)
    
    def get_absolute_url(self, kwargs):
        return reverse('core:movie_suggestion', kwargs={'pk': self.pk})
    

class Reviews(models.Model):
    user = models.ForeignKey(User)
    comment = models.TextField()



    def __str__(self) -> str:
        return f'{self.user}'

