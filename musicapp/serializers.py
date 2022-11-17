from rest_framework import serializers
from .models import Artiste, Song, Lyric

class ArtisteSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Artiste
        fields = ('id', 'first_name', 'last_name', 'age')
        
class SongSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Song
        fields = '__all__'
        
class LyricSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Lyric
        fields = '__all__'