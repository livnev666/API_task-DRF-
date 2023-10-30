from django.shortcuts import render
from .serializers import *
from rest_framework import generics
from rest_framework.pagination import PageNumberPagination
from .permissions import IsAdminHasObjectPermissions, IsAdminHasPermissions
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAdminUser, IsAuthenticated

# Create your views here.


class Pagination(PageNumberPagination):

    page_size = 5
    page_size_query_param = 'page_size'
    max_page_size = 1000


class ArtistListView(generics.ListCreateAPIView):

    """Вывод всех артистов"""

    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer
    # permission_classes = (IsAdminHasObjectPermissions, )


class ArtistDetailView(generics.RetrieveAPIView):

    queryset = Artist.objects.all()
    serializer_class = ArtistDetailSerializer
    pagination_class = Pagination
    # permission_classes = (IsAuthenticatedOrReadOnly, )


class AlbumListView(generics.ListCreateAPIView):
    """Вывод всех артистов"""

    queryset = Album.objects.all()
    serializer_class = AlbumSerialiser
    pagination_class = Pagination


class AlbumDetailView(generics.RetrieveAPIView):

    queryset = Album.objects.all()
    serializer_class = AlbumDetailSerializer


class SongListView(generics.ListCreateAPIView):
    """Вывод всех артистов"""

    queryset = Song.objects.all()
    serializer_class = SongSerializer
    pagination_class = Pagination
    # permission_classes = (IsAuthenticatedOrReadOnly, )


class SongDetailView(generics.RetrieveAPIView):

    queryset = Song.objects.all()
    serializer_class = SongDetailSerializer


