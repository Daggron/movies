from django.views import generic
from django.core.urlresolvers import reverse
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from .models import Movies

class IndexView(generic.ListView):
    template_name = 'movies/index.html'
    context_object_name = 'all_movies'
    def get_absolute_url(self):
        return  reverse('movie:detail',kwargs={'pk':self.pk})
    def get_queryset(self):
        return Movies.objects.all()
class DetailsView(generic.DetailView):
    model = Movies
    template_name = 'movies/details.html'
class add_Movies(CreateView):
    model = Movies
    fields = ['movie_title','movie_cast','movie_genre','movie_poster']
