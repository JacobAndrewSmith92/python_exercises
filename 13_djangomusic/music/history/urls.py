from django.urls import path

from . import views


app_name = 'history'

urlpatterns = [
    path('', views.ArtistsView.as_view(), name='artists'),
    path('artists/<int:pk>/', views.ArtistDetailView.as_view(), name='detail'),
    # path('artist/new', views.new_artist, name='new_artist'),
]