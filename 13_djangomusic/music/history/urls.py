from django.urls import path

from . import views


app_name = 'history'

urlpatterns = [
    path('', views.artist, name='artists'),
    path('<int:artist_id>/', views.detail, name='detail'),
    # path('artist/new', views.new_artist, name='new_artist'),
]