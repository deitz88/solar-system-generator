import random
from django.db import models
from django.urls import reverse
from django.core.validators import MaxValueValidator, MinValueValidator


# Create your models here.
class SolarSystem(models.Model):
  DISPLAYTYPE = [('orbit', 'Orbit'), ('line', 'Line')]
  RANDOMIZE = [('True', True), ('False', False)]
  RINGS = [('True', True), ('False', False)]
  NEBULA = [('True', True), ('False', False)]
  display_type = models.CharField(max_length=100, choices=DISPLAYTYPE, default='Orbit', name='Display')
  random = models.CharField(max_length=100, choices=RANDOMIZE, default=True, name='Randomize Placement?')
  rings = models.CharField(max_length=100, choices=RINGS, default=True, name='Rings')
  # nebula = models.CharField(max_length=100, choices=NEBULA, default=True, name='Nebula Background')
  border_size = models.IntegerField(default=40, name='Border Size')
#   maybe take out height and width
  width = models.IntegerField(default=3000, name='Width of Image')
  height = models.IntegerField(default=2000, name='Height of Image')
#   enum to less than 1, 1.5?
  noise = models.FloatField(validators=[MinValueValidator(0.0), MaxValueValidator(1.0)], default=.35, name='Noise/Texture of Final Image')
#   background Stars
  white_star = models.IntegerField(default=400, name='White Star Count in Background')
  yellow_star = models.IntegerField(default=60, name='Yellow Star Count in Background')
  blue_star = models.IntegerField(default=25, name='Blue Star Count')
  
#   to add: color themes, comet, asteroid?, movement?
  def __str__(self):
    return self.name
  
class Nebula(models.Model):
  def randomName(): 
    letters = ['P', 'Z', 'B', 'X', 'C', 'L']
    return 'System '+ random.choice(letters) + random.choice(letters)+ str(random.randint(1, 97))
  # shapes = models.IntegerField(default=15, name="Min")
  # max_shapes = models.IntegerField(default=20, name="Max")
  name = models.CharField(max_length=100, name='Name your Nebula', default=randomName())

  def __str__(self):
    return self.name
  
