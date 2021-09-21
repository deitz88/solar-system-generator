from random import randbytes

from django.forms import widgets
from .models import SolarSystem
from modules.generate_planets_web import main
from modules.generate import generate
from django.shortcuts import render, redirect
from django.http import HttpResponse 
from .forms import PlanetForm
from django.views.generic import CreateView

# Create your views here.
def index(request): 
    return render(request, 'index.html')

def generate(request):
    generate_form = PlanetForm()
    return render(request, 'planet_generate.html', {'generate_form': generate_form})

def planet(request):
    x = request.POST.get
    display_type = x('Display')
    randomize = x('Randomize Placement?')
    border = x('Border Size')
    width = x('Width of Image')
    height = x('Height of Image')
    noise = x('Noise/Texture of Final Image')
    white_star = x('White Star Count in Background')
    yellow_star = x('Yellow Star Count in Background')
    blue_star = x('Blue Star Count')
    
    type(display_type)
    print(display_type, randomize, border, width, height, noise, white_star, yellow_star, blue_star)
    
    return render(request, 'planet.html')

    # return HttpResponse("""<html><script>window.location.replace('/');</script></html>""")
# def planet(request):
# class Generate(CreateView):
#   model = SolarSystem
#   fields = '__all__'
  
#   def form_valid(self, form):
#     return super().form_valid(form) 