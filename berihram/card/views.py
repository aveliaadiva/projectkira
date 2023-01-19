from django.shortcuts import render
from django.http import HttpResponse

def visa(request):
	return render(request, 'visa-page.html')