from django.db import models
import datetime

class Artist(models.Model):
    artist_name = models.CharField(max_length=100)
    year_started = models.CharField(max_length=4, default="2018")

    # def __str__(self):
    #     return f"{self.artist_name} : {self.year_started}"

class Song(models.Model):
    artist_name = models.ForeignKey(Artist, on_delete=models.CASCADE)
    song_name = models.CharField(max_length=100)
    release_year = models.CharField(max_length=4, default="2010")

    # def __str__(self):
    #     return f"{self.song_name} : {self.release_year}"

