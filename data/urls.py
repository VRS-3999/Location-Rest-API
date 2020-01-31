from django.urls import path, include
from . import views
from django.conf.urls import url

app_name = 'data'

urlpatterns = [
    url(r'^users/$', views.GsmView.as_view(), name='LocationTrack'),
    url(r'^users/(?P<pk>[0-9]+)/$', views.GsmDetail.as_view(), name='DetailTrack'),
    url(r'^location/$', views.cordinates.as_view(), name='cordinates'),
    ]
