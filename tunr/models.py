from django.db import models
from django.urls import reverse


# Create your models here.

class Artist(models.Model):
    name = models.CharField(max_length=100)
    nationality = models.CharField(max_length=100)
    photo_url = models.TextField()

    def __str__(self):
        return self.name


class Song(models.Model):
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE, related_name='songs')
    title = models.CharField(max_length=100, null = True , default = None, blank = True)
    album = models.CharField(max_length=100, null = True , default = None, blank = True)
    preview = models.TextField(null = True , default = None, blank = True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('song_detail', kwargs={'pk': self.pk})    