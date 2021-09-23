from django.db import models
from django.forms import ModelForm, widgets, CharField, IntegerField, FloatField
from .models import SolarSystem, Nebula


# display_type = models.CharField(max_length=100, choices=DISPLAYTYPE, default='Orbit', name='Display')
#   random = models.CharField(max_length=100, choices=RANDOMIZE, default=True, name='Randomize Placement?')
#   rings = models.CharField(max_length=100, choices=RINGS, default=True, name='Rings')
#   nebula = models.CharField(max_length=100, choices=NEBULA, default=True, name='Nebula Background')
#   border_size = models.IntegerField(default=40, name='Border Size')
# #   maybe take out height and width
#   width = models.IntegerField(default=3000, name='Width of Image')
#   height = models.IntegerField(default=2000, name='Height of Image')
# #   enum to less than 1, 1.5?
#   noise = models.FloatField(validators=[MinValueValidator(0.0), MaxValueValidator(1.0)], default=.35, name='Noise/Texture of Final Image')
# #   background Stars
#   white_star = models.IntegerField(default=400, name='White Star Count in Background')
#   yellow_star = models.IntegerField(default=60, name='Yellow Star Count in Background')
#   blue_star = models.IntegerF

class PlanetForm(ModelForm):
  class Meta:
    model = SolarSystem
    fields = '__all__'

class NebulaForm(ModelForm):
  class Meta:
    model = Nebula
    fields = '__all__'