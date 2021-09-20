import modulefinder
# from modules.generative_planets import space_generate

from django.shortcuts import render, redirect
from django.http import HttpResponse
# Create your views here.
def index(request): 
    return render(request, 'index.html')

def planet(request):
    # space_generate()
    return HttpResponse("""<html><script>window.location.replace('/');</script></html>""")