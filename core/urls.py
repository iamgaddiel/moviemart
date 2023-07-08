from django.urls import path
from .views import (
    IndexPage,
    MovieDetail,
    WatchMovie,
    ListMovie,
    MovieSuggestView,
    dowload_torrent_file,
    SearchMovies,
    post_review
)


app_name  = 'core'

urlpatterns = [
    path('', IndexPage.as_view(), name="index"),
    path('movie/watch/<uuid:pk>/', WatchMovie.as_view(), name='movie_watch'),
    path('movie/<uuid:pk>/', MovieDetail.as_view(), name='movie_detail'),
    path('movie/list/', ListMovie.as_view(), name='movie_list'),
    path('movie/suggestions/', MovieSuggestView.as_view(), name='movie_suggestion'),
    path('movie/download/torrent/<uuid:pk>/<str:resolution>', dowload_torrent_file, name='movie_download_torrent'),
    path('movie/search', SearchMovies.as_view(), name='movie_search'),
    path('reivew/', post_review, name='add_review'),
]
