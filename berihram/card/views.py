from django.shortcuts import render
from django.http import HttpResponse

def visa(request):
	return render(request, 'visa-page.html')

def master(request):
	return render(request, 'master-page.html')