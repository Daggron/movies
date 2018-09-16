from django.db import models

class Movies(models.Model):
    movie_title = models.CharField(max_length=250)
    movie_cast = models.CharField(max_length=1000)
    movie_genre = models.CharField(max_length=1000)
    movie_poster = models.CharField(max_length=1000)

    def __str__(self):
        return self.movie_title+'----'+self.movie_cast

class Songs(models.Model):
    song = models.ForeignKey(Movies,  on_delete=models.CASCADE)
    song_title = models.CharField(max_length=250)
    file_type = models.CharField(max_length=250)
    is_favourite= models.BooleanField(default=False)
    def __str__(self):
        return self.song_title+'---'+self.file_type