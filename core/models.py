from django.db import models
from django.contrib.auth.models import User
from .validators import validate_file_extension
from django.urls import reverse
import uuid



class Movie(models.Model):
    id = models.UUIDField(primary_key=True, unique=True, editable=False, default=uuid.uuid4)
    title = models.CharField(max_length=100, unique=True)
    description = models.TextField()
    x_720 = models.FileField(upload_to=f'torrents/%Y/%m/%d', validators=[validate_file_extension], blank=True)
    x_1080 = models.FileField(upload_to=f'torrents/%Y/%m/%d', validators=[validate_file_extension], blank=True)
    x_2160 = models.FileField(upload_to=f'torrents/%Y/%m/%d', validators=[validate_file_extension], blank=True)
    movie_link = models.URLField()
    locked_movie_link = models.URLField(blank=True)
    locked_x_720_link = models.URLField(blank=True)
    locked_x_1080_link = models.URLField(blank=True)
    locked_x_2160_link = models.URLField(blank=True)
    thumbnail = models.ImageField(upload_to='thumbnails/%Y/%m/%d')
    realse_year = models.CharField(max_length=5)
    is_trending = models.BooleanField(default=False)
    views = models.IntegerField(default=0)
    thriller_link = models.URLField()
    movie_tags = models.CharField(max_length=300, help_text='seprate tags with a "/"')
    movie_type = models.CharField(max_length=20)
    realse_data = models.DateField(null=True)
    rating = models.CharField(max_length=20, default="1/10", help_text="1/10")
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
    

class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.TextField()
    movie = models.ForeignKey(to=Movie, on_delete=models.CASCADE)
    created = models.DateField(auto_created=True)


    def __str__(self) -> str:
        return f'{self.user}'

