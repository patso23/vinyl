from django.db import models

# Create your models here.


class Artist(models.Model):
    name = models.CharField(max_length=50)

    def __unicode__(self):
        return self.name


class Label(models.Model):
    name = models.CharField(max_length=100)
    address_1 = models.CharField(max_length=100)
    address_2 = models.CharField(max_length=100, blank=True)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=2)
    zip = models.CharField(max_length=5)
    email = models.EmailField(max_length=254)
    phone = models.CharField(max_length=20)
    url = models.CharField(max_length=765)

    def __unicode__(self):
        return self.name


class Album(models.Model):
    artist = models.OneToOneField(Artist, related_name="album_artist")
    album_title = models.CharField(max_length=50)
    label = models.ForeignKey(Label)
    release_year = models.DateField()
    upc = models.CharField(max_length=13, blank=True)
    country = models.CharField(max_length=50)
    url = models.CharField(max_length=765)
    FORMATS = (
        ('45_7', '45rpm 7"'),
        ('33_7', '33rpm 7"'),
        ('33LP', '33rpm LP'),
        ('45EP', '45rpm EP'),
        ('33_10', '33rpm 10"'),
        ('45_10', '45rpm 10"'),
    )

    format = models.CharField(max_length=5,
                              choices=FORMATS,
                              )

    def __unicode__(self):
        return self.album_title


class TrackListing(models.Model):
    album = models.OneToOneField(Album, primary_key=True)

    def __unicode__(self):
        return '%s' % (self.album.album_title)


class Track(models.Model):
    track_listing = models.ForeignKey(TrackListing)
    title = models.CharField(max_length=150)
    track_number = models.IntegerField()
    number_of_tracks = models.IntegerField()

    def __unicode__(self):
        return self.title
