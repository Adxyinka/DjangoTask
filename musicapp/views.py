from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from .serializers import ArtisteSerializer, SongSerializer, LyricSerializer
from rest_framework.decorators import api_view
from .models import Artiste, Song, Lyric
# Create your views here.

def index(request):
    return HttpResponse('Hello, this is my first djangoapp')


# @api_view(['GET'])
# def getArtistes(request):
#     return Response(Artiste)

# class ArtisteList(viewsets.ModelViewSet):
class ArtisteList(ModelViewSet):
    queryset = Artiste.objects.all()
    serializer_class = ArtisteSerializer
    
class ArtisteList(ModelViewSet):
    queryset = Artiste.objects.all()
    serializer_class = ArtisteSerializer
    

# class SongList(viewsets.ModelViewSet):
class SongList(ModelViewSet):
    queryset = Song.objects.all()
    serializer_class = SongSerializer
    
class SongDetail(ModelViewSet):
    queryset = Song.objects.all()
    serializer_class = SongSerializer

# @api_view(['GET'])
# def getLyric(request):
#     return Response(Lyric)

# class LyricViewSet(viewsets.ModelViewSet):
# class LyricList(generics.ListCreateAPIView):
#     queryset = Lyric.objects.all()
#     serializer_class = LyricSerializer