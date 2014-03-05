from django.db import models

# Create your models here.


class Album(models.Model):
    artist = models.CharField(max_length=50)
    album_title = models.CharField(max_length=50)
    label = models.CharField(max_length=50)
    release_year = models.DateField(False, False)
    upc = models.CharField(max_length=13)
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


class Track(models.Model):
    track_listing = models.ForeignKey(TrackListing)
    title = models.CharField(max_length=150)


class Label(models.Model):
    album = models.OneToOneField(Album, primary_key=True,
                                 related_name='album_name')
    name = models.CharField(max_length=100)
    address_1 = models.CharField(max_length=100)
    address_2 = models.CharField(max_length=100)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=2)
    zip = models.CharField(max_length=5)
    email = models.EmailField(max_length=254)
    phone = models.CharField(max_length=20)
    url = models.CharField(max_length=765)

    def __unicode__(self):
        return self.name
