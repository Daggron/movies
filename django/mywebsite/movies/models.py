from django.db import models
from django.core.urlresolvers import reverse
class Movies(models.Model):
    movie_title = models.CharField(max_length=250)
    movie_cast = models.CharField(max_length=1000)
    movie_genre = models.CharField(max_length=1000)
    movie_poster = models.FileField()

    def get_absolute_url(self):
        return reverse('movie:detail', kwargs={'pk': self.pk})
    def __str__(self):
        return self.movie_title+'----'+self.movie_cast

class Songs(models.Model):
    song = models.ForeignKey(Movies,  on_delete=models.CASCADE)
    song_title = models.CharField(max_length=250)
    file_type = models.CharField(max_length=250)
    def __str__(self):
        return self.song_title+'---'+self.file_type