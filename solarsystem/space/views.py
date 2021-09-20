from .models import SolarSystem
from modules.generate_planets_web import main
from django.shortcuts import render, redirect
from django.http import HttpResponse 
from .forms import PlanetForm
from django.views.generic import CreateView

# Create your views here.
def index(request): 
    # planet_form = PlanetForm()
    return render(request, 'index.html')

def generate(request):
    generate_form = PlanetForm()
    return render(request, 'planet_generate.html', {'generate_form': generate_form})

# def planet(request):
#     if request.POST:
#         print(request)
#     main()
#     return HttpResponse("""<html><script>window.location.replace('/');</script></html>""")

# class Generate(CreateView):
#   model = SolarSystem
#   fields = '__all__'
  
#   def form_valid(self, form):
#     return super().form_valid(form) 