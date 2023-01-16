from django.shortcuts import render
from django.http import HttpResponse

from .models import Video

def index(request):
    videos = Video.objects.all()
    return render(request, 'page-riyal.html',context={'videos':videos})