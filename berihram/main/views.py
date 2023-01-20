from django.shortcuts import render
from django.http import HttpResponse

def index(request):
	return render(request, 'home-page.html')

def syarat(request):
	return render(request, 'syarat-page.html')

def rekan(request):
	return render(request, 'rekan-page.html')
