from django.forms import ModelForm
from .models import SolarSystem

class Generate(ModelForm):
  class Meta:
    model = SolarSystem
    fields = 'all'