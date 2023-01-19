from django.urls import include, path
from .views import visa

urlpatterns = [
    path('/visa', visa, name='visa'),
]