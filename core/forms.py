from django.forms import ModelForm
from .models import MovieSuggestion


class SuggestionCrateForm(ModelForm):
    class Meta:
        model = MovieSuggestion
        fields = '__all__'
