from django.contrib import admin
from .models import Movie, MovieSuggestion, Review



admin.site.register(Movie)
admin.site.register(MovieSuggestion)
admin.site.register(Review)
