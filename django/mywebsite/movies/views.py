
from django.shortcuts import render,get_object_or_404
from  .models import Movies, Songs

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
        return  render(request, 'movies/error.html')
    return render(request, 'movies/details.html', data)

def favourite(request,movie_id):
    movie=get_object_or_404(Movies,pk=movie_id)
    try:
      selected_song=movie.songs_set.get(pk=request.POST['song'])
    except(KeyError,Songs.DoesNotExist):
        return  render(request, 'movies/details.html', {'movies':movie, 'error_message': "You Didn't Select a song"})
    else:
        selected_song.is_favourite= True
        selected_song.save()
        return render(request, 'movies/details.html', {'movies': movie})
