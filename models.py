from django.db import models

# Choices for a transaction:
Genres = [('Rock', 'Rock'), ('Blues', 'Blues'), ('Classical', 'Classical'), ('R&B', 'R&B')]

class Track(models.Model):
    artist_name = models.CharField(max_length=100, default="", blank=True, null=False)
    product_name = models.CharField(max_length=100, default="", blank=True, null=False)
    track_name = models.CharField(max_length=100, default="", blank=True, null=False)
    genre_name = models.CharField(choices=Genres, max_length=100)

    objects = models.Manager()

    def __str__(self):
        return self.track_name


class FavTrack(models.Model):
    track_name = models.CharField(max_length=100, default="", blank=True, null=False)
    price = models.CharField(max_length=20, default="", blank=True, null=False)

    objects = models.Manager()

    def __str__(self):
        return self.track_name

