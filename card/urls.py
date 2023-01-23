from django.urls import include, path
from .views import visa,master

urlpatterns = [
    path('/visa', visa, name='visa'),
    path('/master',master,name='master')
]