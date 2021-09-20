from django.forms import ModelForm
from .models import SolarSystem


class PlanetForm(ModelForm):
  class Meta:
    model = SolarSystem
    fields = '__all__'
