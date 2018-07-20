from django.shortcuts import render
from .models import Artist
from django.http import HttpResponse
from django.shortcuts import get_object_or_404


def artist(request):
    artist_list = Artist.objects.all()
    context = {"artists": artist_list}
    return render(request, 'history/artists.html', context)

def detail(request, artist_id):
    artist = get_object_or_404(Artist, pk=artist_id)
    song = artist.song_set.all()
    return render(request, "history/detail.html", {'songs': song})
