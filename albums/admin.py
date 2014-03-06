from django.contrib import admin
from albums.models import Album, Artist, Label, Track


class TrackInline(admin.TabularInline):
    model = Track
    extra = 3


class AlbumAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['artist', 'album_title', 'label', 'release_year',
                           'upc', 'country', 'url', 'format']}),
    ]
    inlines = [TrackInline]


# Register your models here.

admin.site.register(Artist)
admin.site.register(Album, AlbumAdmin)
admin.site.register(Label)
