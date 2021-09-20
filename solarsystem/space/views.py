import modulefinder
# from modules.generative_planets import space_generate
from modules.generate_planets_web import main
from django.shortcuts import render, redirect
from django.http import HttpResponse 
from .forms import PlanetForm
# Create your views here.
def index(request): 
    planet_form = PlanetForm()
    return render(request, 'index.html', {'planet_form': planet_form})

def planet(request):
    main()
    return HttpResponse("""<html><script>window.location.replace('/');</script></html>""")