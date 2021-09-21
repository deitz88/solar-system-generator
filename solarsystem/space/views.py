import asyncio
from modules.generate import generate_planets
from django.shortcuts import render
from .forms import PlanetForm

def index(request): 
    return render(request, 'index.html')

def generate(request):
    generate_form = PlanetForm()
    return render(request, 'planet_generate.html', {'generate_form': generate_form})

def planet(request):
    x = request.POST.get    
    display_type = x('Display')
    randomize = x('Randomize Placement?')
    rings = x('Rings')
    nebula = x('Nebula Background')
    border = x('Border Size')
    width = x('Width of Image')
    height = x('Height of Image')
    noise = x('Noise/Texture of Final Image')
    white_star = x('White Star Count in Background')
    yellow_star = x('Yellow Star Count in Background')
    blue_star = x('Blue Star Count')
    
    generate_planets(display_type, randomize, rings, nebula, border, width, height, noise, white_star, yellow_star, blue_star)
    return render(request, 'rendering.html')