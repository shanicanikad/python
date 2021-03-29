# from django.urls import path
# from . import views
# from rest_framework.routers import DefaultRouter

# urlpatterns = [
#     path('artists/', views.ArtistList.as_view(), name='artist_list'),
#     path('songs/', views.SongList.as_view(), name='song_list'),
#     path('artists/<int:pk>', views.ArtistDetail.as_view(), name='artist_detail'),
#     path('songs/<int:pk>', views.SongDetail.as_view(), name='song_detail'),
#     path('artists/new', views.ArtistCreate.as_view(), name='artist_create'),
#     path('songs/new', views.song_create, name='song_create'),
#     path('artists/<int:pk>/edit', views.artist_edit, name='artist_edit'),
#     path('songs/<int:pk>/edit', views.SongEdit.as_view(), name='song_edit'),
#     path('artists/<int:pk>/delete', views.artist_delete, name='artist_delete'),
#     path('songs/<int:pk>/delete', views.SongDelete.as_view(), name='song_delete'),

# ]
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.artist_list, name='artist_list'),
    url(r'^artists/(?P<pk>\d+)$', views.artist_detail, name='artist_detail'),
    url(r'^artists/new$', views.artist_create, name='artist_create'),
    url(r'^artists/(?P<pk>\d+)/edit$', views.artist_edit, name='artist_edit'),
    url(r'^artists/(?P<pk>\d+)/delete$', views.artist_delete, name='artist_delete'),


    url(r'^songs$', views.song_list, name='song_list'),
    url(r'^songs/(?P<pk>\d+)$', views.song_detail, name='song_detail'),
    url(r'^songs/new$', views.song_create, name='song_create'),
    url(r'^songs/(?P<pk>\d+)/edit$', views.song_edit, name='song_edit'),
    url(r'^songs/(?P<pk>\d+)/delete$', views.song_delete, name='song_delete'),
]