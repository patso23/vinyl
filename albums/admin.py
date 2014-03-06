from django.contrib import admin
from albums.models import Album, Artist, Label, Track, TrackListing

# Register your models here.


admin.site.register(Artist)
admin.site.register(Album)
admin.site.register(Label)
admin.site.register(Track)
admin.site.register(TrackListing)
