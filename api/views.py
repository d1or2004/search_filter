from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Artist, Album, Song
from .serializers import ArtistSerializer, AlbumSerializer, SongSerializer
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework import filters


class LandingAPIView(APIView):
    def get(self, request):
        return Response(data={"Landing Page get request": "Landing Page"})

    def post(self, request):
        return Response(data={"Landing Page post request": "Landing Page"})


# ________________________________________________________________________
class ArtistAPIView(APIView):
    def get(self, request):
        artists = Artist.objects.all()
        serializer = ArtistSerializer(artists, many=True)
        return Response(serializer.data)


class ArtistCreateAPIView(generics.CreateAPIView):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer


class ArtistUpdateAPIView(generics.UpdateAPIView):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer


class ArtistDeleteAPIView(generics.DestroyAPIView):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer


# _____________________________________________________________________________________

class AlbumAPIView(APIView):
    def get(self, request):
        albums = Album.objects.all()
        serializer = AlbumSerializer(albums, many=True)
        return Response(serializer.data)


class AlbumDetailAPIView(APIView):
    def get(self, request, pk):
        album = Album.objects.get(id=pk)
        try:
            serializer = AlbumSerializer(album)
            return Response(data={"Album": serializer.data})
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def patch(self, request, pk):
        album = Album.objects.get(id=pk)
        serializer = AlbumSerializer(instance=album, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(data={"Album": serializer.data}, status=status.HTTP_200_OK)

        return Response(data={"Album": serializer.data}, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        album = Album.objects.get(id=pk)
        serializer = AlbumSerializer(instance=album, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data={"Album": serializer.data}, status=status.HTTP_200_OK)

        return Response(data={"Album": serializer.data}, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        album = Album.objects.get(id=pk)
        album.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# _________________________________________________________

class SongAPIView(APIView):
    def get(self, request):
        songs = Song.objects.all()
        serializer = SongSerializer(songs, many=True)
        return Response(serializer.data)


#
# class SongDetailAPIView(ModelViewSet):
#     queryset = Song.objects.all()
#     serializer_class = SongSerializer


class SongSetAPIView(ModelViewSet):
    queryset = Song.objects.all()
    serializer_class = SongSerializer
    permission_classes = (IsAuthenticated,)
    # authentication_classes = (TokenAuthentication,)
    # filter_backends = (filters.SearchFilter,)
    # search_fields = ('name',)
    # search_fields = ('^name')
    # search_fields = ('=name',)
    search_fields = ('$name',)


class AlbumSetAPIView(ModelViewSet):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer
    # permission_classes = (IsAuthenticated,)
    # authentication_classes = (TokenAuthentication,)
    filter_backends = (filters.SearchFilter,)
    # search_fields = ('title',)
    # search_fields = ('^title')
    # search_fields = ('=title',)
    search_fields = ('title',)


class ArtistSetAPIView(ModelViewSet):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer
    # permission_classes = (IsAuthenticated,)
    # authentication_classes = (TokenAuthentication,)
    # search_fields = ('title',)
    # search_fields = ('^title')
    # search_fields = ('=title',)
    search_fields = ('title',)
