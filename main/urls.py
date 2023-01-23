from django.urls import include, path
from .views import index,syarat,rekan,gallery

urlpatterns = [
    path('', index, name='index'),
    path('syarat-haji', syarat, name='syarat'),
    path('rekan', rekan, name='rekan'),
    path('galeri', gallery, name='gallery'),
]
