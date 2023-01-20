from django.urls import include, path
from .views import index,syarat

urlpatterns = [
    path('', index, name='index'),
    path('syarat-haji', syarat, name='syarat'),
]
