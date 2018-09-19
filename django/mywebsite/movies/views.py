from django.views import generic

from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.core.urlresolvers import reverse_lazy
from .models import Movies

class IndexView(generic.ListView):
    template_name = 'movies/index.html'
    context_object_name = 'all_movies'

    def get_queryset(self):
        return Movies.objects.all()
class DetailsView(generic.DetailView):
    model = Movies
    template_name = 'movies/details.html'
class add_Movies(CreateView):
    model = Movies
    fields = ['movie_title','movie_cast','movie_genre','movie_poster']
class Update_Movies(UpdateView):
    model = Movies
    fields = ['movie_title','movie_cast','movie_genre','movie_poster']
class Delete_Movies(DeleteView):
    model = Movies
    success_url = reverse_lazy('movie:index')
