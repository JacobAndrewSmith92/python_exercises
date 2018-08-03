from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, TemplateView, FormView, DetailView, CreateView
from .models import Artist, Song, Album, Album_Song
from django.http import HttpResponse


# class IndexView(View):
#     template_name = 'history/index.html'

#     def get(self, request):
#         return HttpResponse('At the IndexView')

class ArtistsView(ListView):
    template_name = 'history/artists.html'
    context_object_name = 'artists'

    def get_queryset(self):
        return Artist.objects.all()

# def artist(request):
    # artist_list = Artist.objects.all()
    # context = {"artists": artist_list}
    # return render(request, 'history/artists.html', context)

class ArtistDetailView(DetailView):
    model = Artist
    # template_name = 'history/detail.html'

    # context_object_name = 'artist_list'

# def detail(request, artist_id):
#     artist = get_object_or_404(Artist, pk=artist_id)
#     song = artist.song_set.all()
#     album = Album.objects.all()
#     # genre = Genre.objects.all()
#     context = {'songs': song, 'alb': album}
#     return render(request, "history/detail.html", context)

