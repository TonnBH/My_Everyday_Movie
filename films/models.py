from django.db import models
from django.conf import settings # add this line to the bottom of the imports.

class Films(models.Model):
    title = models.CharField(max_length=250)
    released = models.DateField(auto_now=False, auto_now_add=False)
    certificate = models.CharField(max_length=3)
    duration = models.DurationField()
    genre = models.CharField(max_length=100)
    direction = models.CharField(max_length=250)
    star1 = models.CharField(max_length=250)
    star2 = models.CharField(max_length=250)
    star3 = models.CharField(max_length=250)
    star4 = models.CharField(max_length=250)
    overvew = models.TextField(max_length=1000)
    poster = models.URLField(max_length=200)

    def __str__(self):
        return self.title
    
class Ratting (models.Model):
    film = models.ForeignKey(Films, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    rating = models.IntegerField()

    def __str__(self) -> str:
        return f"{self.film} - {self.user}"
