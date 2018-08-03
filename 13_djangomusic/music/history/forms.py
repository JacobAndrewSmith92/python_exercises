
from django import forms

class AlbumForm(forms.Form):
    album_name = forms.CharField(label='New Album', max_length=50)

