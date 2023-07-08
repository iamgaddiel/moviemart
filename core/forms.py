from django.forms import ModelForm
from .models import MovieSuggestion, Review


class SuggestionCrateForm(ModelForm):
    class Meta:
        model = MovieSuggestion
        fields = '__all__'


class CrateReviewForm(ModelForm):
    class Meta:
        model = Review
        fields = ['comment', ]
