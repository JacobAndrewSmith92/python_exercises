from django.db import models
import datetime

class Artist(models.Model):
    artist_name = models.CharField(max_length=100)
    year_started = models.CharField(max_length=4, default=" ")

    def __str__(self):
        return self.artist_name

# class Genre(models.Model):
#     genre_type = models.CharField(max_length=50)

#     def __str__(self):
#         return self.genre_type


class Song(models.Model):
    artist_name = models.ForeignKey(Artist, on_delete=models.CASCADE)
    song_name = models.CharField(max_length=100)
    release_year = models.CharField(max_length=4, default="2010")
    # album = models.ManyToManyField(Album, through='Album_Song')


class Album(models.Model):
    song = models.ManyToManyField(Song, through='Album_Song')
    artist_name = models.ForeignKey(Artist, on_delete=models.CASCADE)
    album_title = models.CharField(max_length=75)
    year_released = models.IntegerField(default=None)

    def __str__(self):
        return self.album_title

class Album_Song(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    song = models.ForeignKey(Song, on_delete=models.CASCADE)

    def __str__(self):
        return self.song_name + self.release_year

