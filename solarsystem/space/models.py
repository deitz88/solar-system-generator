from space.widgets import RangeInput
from django.db import models
from datetime import date
# from django.forms import widgets.RangeInput
# from django.forms import widgets


# Create your models here.
class SolarSystem(models.Model):
  DISPLAYTYPE = [('orbit', 'Orbit'), ('line', 'Line')]
  display_type = models.CharField(max_length=100, choices=DISPLAYTYPE, default='Orbit')
  random = models.BooleanField(default=True)
  border_size = models.IntegerField(default=40)
  width = models.IntegerField(default=3000)
  height = models.IntegerField(default=2000)
  noise = models.FloatField(default=.35)
  white_star = models.IntegerField(RangeInput, default=400)
  yellow_star = models.IntegerField(default=60)
  blue_star = models.IntegerField(default=25)
#   to add: color themes, comet, asteroid?, movement?

  
  
  
#   age = models.IntegerField()
#   toys = models.ManyToManyField(Toy)
#   user = models.ForeignKey(User, on_delete=models.CASCADE)

  def __str__(self):
    return self.name