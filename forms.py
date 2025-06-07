from django.forms import ModelForm

from MusicApp.models import Track, FavTrack


class TrackForm(ModelForm):
    class Meta:
        model = Track
        fields = '__all__'


class FavTrackForm(ModelForm):
    class Meta:
        model = FavTrack
        fields = '__all__'