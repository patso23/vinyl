from django.conf.urls import patterns, url

from albums import views

urlpatterns = patterns('',
                       url(r'^$', views.index, name="index")
                       )
