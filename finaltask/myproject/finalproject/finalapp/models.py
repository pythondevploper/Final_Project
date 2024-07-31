from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Movie(models.Model):
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  movie_title = models.CharField(max_length=255)
  poster = models.ImageField(upload_to='image/')
  description=models.CharField(max_length=1000)
  release_date=models.DateField()
  cast=models.CharField(max_length=1000)
  category=models.CharField(max_length=200)
  youtube_trailer_link=models.URLField(max_length=200)
  def __str__(self):
      return self.movie_title
class Review(models.Model):
      movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='reviews')
      user = models.ForeignKey(User, on_delete=models.CASCADE)
      rating = models.IntegerField()
      comment = models.TextField()
      created_at = models.DateTimeField(auto_now_add=True)        
      def __str__(self):
        return f'{self.user.username} - {self.movie.movie_title}'