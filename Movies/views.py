from django.shortcuts import render
from .models import Movie
# Create your views here.

def movie_list(request):
    movies = Movie.objects.all()
    context = {
        'movies': movies
    }
    return render(request, 'Movie/Movie.html', context)

def movie_detail(request, movie_id):
    movie = Movie.objects.get(id=movie_id)
    context = {
        'movie': movie
    }
    return render(request, 'Movie/movie_detail.html', context)