from django.urls import path, include
from rest_framework import routers
from . import views


router = routers.DefaultRouter()
router.register(r'artiste', views.ArtisteList)
router.register(r'song', views.SongList)
# router.register(r'lyrics', views.LyricViewSet)
urlpatterns = [
    path('', views.index, name = 'index'),
    # path('', include(router.urls)),
    path('api/', include(router.urls))
    # path('api-auth/', include('rest_framework.urls'))
]