# from rest_framework import serializers

# from .models import Artist, Song

# class ArtistSerializer(serializers.HyperlinkedModelSerializer):
#     songs = serializers.HyperlinkedRelatedField(
#         view_name='song_detail',
#         many=True,
#         read_only=True
#     )

#     class Meta:
#         model = Artist
#         fields = ('id', 'photo_url', 'nationality', 'name', 'songs')


# class SongSerializer(serializers.HyperlinkedModelSerializer):
#     artist=serializers.PrimaryKeyRelatedField(queryset = Artist.objects.all())
    
#     class Meta:
#         model = Song
#         fields = ('id', 'artist', 'title', 'album', 'preview',)