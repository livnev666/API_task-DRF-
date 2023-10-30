from django.urls import path, include
from rest_app import views as rest_view
from rest_framework import routers

urlpatterns = [

    path('artist/', rest_view.ArtistListView.as_view()),
    path('album/', rest_view.AlbumListView.as_view()),
    path('song/', rest_view.SongListView.as_view()),

    path('artist/<int:pk>', rest_view.ArtistDetailView.as_view()),
    path('album/<int:pk>', rest_view.AlbumDetailView.as_view()),
    path('song/<int:pk>', rest_view.SongDetailView.as_view()),

]