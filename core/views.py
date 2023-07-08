from typing import Any, Dict
import mimetypes
from os import path



from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.urls import reverse
from django.shortcuts import render, redirect
from django.views.generic import ListView, TemplateView, DetailView, CreateView
from django.conf import settings
from django.contrib.auth.decorators import login_required


from .models import Movie, MovieSuggestion, Review
from .forms import SuggestionCrateForm, CrateReviewForm



class IndexPage(TemplateView):
    template_name = "core/index.html"

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['new_movies'] = Movie.objects.all().reverse().filter()[0: 4]
        context['active_link'] = 'home'
        return context


class MovieDetail(DetailView):
    template_name = 'core/movie_detail.html'
    model = Movie
    context_object_name = 'movie'

    def get(self, *args, **kwargs):
        queryset = Movie.objects.get(id=kwargs.get('pk'))
        queryset.views += 1
        queryset.save()
        return super().get(*args, **kwargs)
    
    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        viewed_movie = Movie.objects.get(id=self.kwargs.get('pk'))
        selected_movie_tag = viewed_movie.movie_tags
        recommended_movies = Movie.objects.filter(
            movie_tags__icontains=selected_movie_tag
        )
        movie_reviews = Review.objects.filter(movie=viewed_movie)


        print(movie_reviews[0].comment, '<---------------')

        context['host'] = self.request.get_host()
        context['recommended_movies'] = recommended_movies
        context['reviews'] = movie_reviews
        return context


class ListMovie(ListView):
    model = Movie
    context_object_name = 'movies'
    template_name = 'core/movie_list.html'
    paginate_by = 30

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['active_link'] = 'browse'
        return context


class WatchMovie(DetailView):
    template_name = 'core/movie_watch.html'
    model = Movie
    context_object_name = 'movie'

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        queryset = Movie.objects.get(id=kwargs.get('pk'))
        context['movie'] = queryset
        return context


class MovieSuggestView(CreateView):
    template_name = 'core/suggest.html'
    model = MovieSuggestion
    form_class = SuggestionCrateForm

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['active_link'] = 'suggestions'
        return context


def dowload_torrent_file(request, *args, **kwargs) -> HttpResponse:
    """
    Returns the requested torrent file for download

    Args:
        request (_type_): _description_

    Returns:
        HttpResponse: 
    """

    movie_resolution = kwargs.get('resolution')

    if movie_resolution == '720':
        torrent_file_path = Movie.objects.get(id=kwargs.get('pk')).x_720.url

    if movie_resolution == '1080':
        torrent_file_path = Movie.objects.get(id=kwargs.get('pk')).x_1080.url

    if movie_resolution == '2160':
        torrent_file_path = Movie.objects.get(id=kwargs.get('pk')).x_2160.url

    filename = torrent_file_path.split('/')[-1]

    full_torrent_filepath = settings.BASE_DIR / torrent_file_path

    mime_type, _ = mimetypes.guess_type(torrent_file_path)

    response = HttpResponse(full_torrent_filepath, content_type=mime_type)

    response['Content-Disposition'] = f'attachment; filename={filename}'

    return response


class SearchMovies(ListView):
    template_name = 'core/search_result.html'
    paginate_by = 16
    context_object_name = 'movies'

    def get_queryset(self, *args, **kwargs):
        query_string = self.request.GET.get('q')
        queryset = Movie.objects.filter(title__icontains=query_string)
        return queryset

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['search_parameter'] =  self.request.GET.get('q')
        context['active_link'] = 'browse'
        return context


@login_required(login_url='auth/login')
def post_review(request):
    template_name = 'core/movie_detail.html'

    if request.method == 'POST':
        post_request = request.POST

        movie = Movie.objects.get(pk=post_request.get('movie'))

        Review.objects.create(
            user = request.user, 
            movie = movie,
            comment = post_request.get('comment')
        ).save()

        return redirect('core:movie_detail', movie.pk)
    
    context = {
        'form': CrateReviewForm()
    }
    return render(request, template_name, context)