from space.widgets import RangeInput
from django.db import models
from django.urls import reverse
# from datetime import date
# from django.forms import widgets.RangeInput
# from django.forms import widgets


# Create your models here.
class SolarSystem(models.Model):
  DISPLAYTYPE = [('orbit', 'Orbit'), ('line', 'Line')]
  display_type = models.CharField(max_length=100, choices=DISPLAYTYPE, default='Orbit', name='Display')
  random = models.BooleanField(default=True, name='Randomize Placement?')
  border_size = models.IntegerField(default=40, name='Border Size')
  width = models.IntegerField(default=3000, name='Width of Image')
  height = models.IntegerField(default=2000, name='Heiht of Image')
  noise = models.FloatField(default=.35, name='Noise/Texture of Final Image')
  white_star = models.IntegerField( default=400, name='White Star Count in Background')
  yellow_star = models.IntegerField(default=60, name='Yellow Star Count in Background')
  blue_star = models.IntegerField(default=25, name='Blue Star Count')
#   to add: color themes, comet, asteroid?, movement?
  def __str__(self):
    return self.name

#   def get_absolute_url(self):
#     return reverse('index')
  
  
#   age = models.IntegerField()
#   toys = models.ManyToManyField(Toy)
#   user = models.ForeignKey(User, on_delete=models.CASCADE)
