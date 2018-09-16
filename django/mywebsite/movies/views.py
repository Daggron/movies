
from django.shortcuts import render
from  .models import Movies

def index(request):
    movies=Movies.objects.all()
    context={'movies':movies}

    return render(request,'movies/index.html',context)

def details(request,movie_id):
    try:
        movies = Movies.objects.get(pk=movie_id)
        data = {
            'movies':movies
        }
    except Movies.DoesNotExist:
        return  render(request,'movies/error.html')
    return render(request,'movies/details.html', data)

