from rest_framework import serializers

from api.models import Artist, Album, Song


class ArtistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artist
        # fields = ('id', 'name')
        fields = '__all__'


class AlbumSerializer(serializers.ModelSerializer):
    album = ArtistSerializer(read_only=True)

    class Meta:
        model = Album
        # fields = ('id', 'artist', 'title')
        fields = '__all__'


class SongSerializer(serializers.ModelSerializer):
    # album = AlbumSerializer(read_only=True)

    class Meta:
        model = Song
        fields = ('id', 'album', 'last_updated')
        # fields = '__all__'
