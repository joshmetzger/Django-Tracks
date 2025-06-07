from django.shortcuts import render, redirect, get_object_or_404
from .forms import TrackForm, FavTrackForm
from .models import Track, FavTrack
import requests
from bs4 import BeautifulSoup
def home(request):
    return render(request, 'MusicApp/home.html')

def create_track(request):
    form = TrackForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect('view_tracks')
    content = {"form": form}
    return render(request, 'MusicApp/tracks/CreateTrack.html', content)


def view_tracks(request):
    tracks = Track.objects.all()
    content = {'tracks': tracks}
    return render(request, 'MusicApp/tracks/ViewTracks.html', content)

def track_details(request, pk):
    track_id = int(pk)
    track = get_object_or_404(Track, pk=track_id)
    form = TrackForm(request.POST or None, instance=track)
    if request.method == "POST":
        if form.is_valid():
            form2 = form.save(commit=False)
            form2.save()
            return redirect('view_tracks')
        else:
            print(form.errors)
            return None
    else:
        content = {'form': form, 'track': track}
        return render(request, 'MusicApp/tracks/TrackDetails.html', content)


def delete_track(request, pk):
    track_id = int(pk)
    track = get_object_or_404(Track, pk=track_id)
    content = {'track': track}
    return render(request, 'MusicApp/tracks/ConfirmDelete.html', content)

def confirm_delete(request, pk):
    if request.method == "POST":
        track = get_object_or_404(Track, pk=pk)
        track.delete()
    return redirect('view_tracks')

# TODO: refactor this to hit the Spotify API and return something
def test_API(request):
    response = requests.get("https://catfact.ninja/fact", timeout=5)
    content = {'response': response.json()}
    return render(request, 'MusicApp/tracks/API.html', content)

def beautiful_soup(request):
    URL = "http://books.toscrape.com"
    result = requests.get(URL)

    # parse the HTML:
    soup = BeautifulSoup(result.content, 'html5lib')

    track_list = []

    # isolate main code block that contains 'track' (book) info:
    tracks = soup.find_all('article', attrs={'class': 'product_pod'})

    # extract the title and price and put it into track_list
    for track in tracks:
        track_name = track.find('a', title=True)
        price = track.find('p', attrs={'class': 'price_color'})

        if track_name and price:
            track_list.append({
                'track_name': track_name['title'],
                'price': price.text
            })

    return render(request, 'MusicApp/tracks/BeauSoup.html', {'track_list': track_list})


def add_fav_track(request):
    form = FavTrackForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect('favorites')
    content = {"form": form}
    return render(request, 'MusicApp/tracks/BeauSoup.html', content)

def favorites(request):
    fav_tracks = FavTrack.objects.all()
    print(fav_tracks)
    content = {"fav_tracks": fav_tracks}
    return render(request, 'MusicApp/tracks/FavTracks.html', content)

