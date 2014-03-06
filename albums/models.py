from django.db import models

# Create your models here.


class Artist(models.Model):
    name = models.CharField(max_length=50)

    def __unicode__(self):
        return self.name


class Label(models.Model):
    name = models.CharField(max_length=100)
    address_1 = models.CharField(max_length=100, blank=True)
    address_2 = models.CharField(max_length=100, blank=True)
    city = models.CharField(max_length=50, blank=True)
    state = models.CharField(max_length=2, blank=True)
    zip = models.CharField(max_length=5, blank=True)
    email = models.EmailField(max_length=254, blank=True)
    phone = models.CharField(max_length=20, blank=True)
    url = models.CharField(max_length=765, blank=True)

    def __unicode__(self):
        return self.name


class Album(models.Model):
    artist = models.ForeignKey(Artist)
    album_title = models.CharField(max_length=50)
    label = models.ForeignKey(Label)
    release_year = models.DateField(blank=True)
    upc = models.CharField(max_length=13, blank=True)
    country = models.CharField(max_length=50, blank=True)
    url = models.CharField(max_length=765, blank=True)
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


class Track(models.Model):
    album = models.ForeignKey(Album)
    title = models.CharField(max_length=150)
    track_number = models.IntegerField(unique=True)
    number_of_tracks = models.IntegerField()

    def __unicode__(self):
        return self.title
