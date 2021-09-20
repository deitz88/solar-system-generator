from django.forms import ModelForm
from .models import SolarSystem


class PlanetForm(ModelForm):
  class Meta:
    model = SolarSystem
    fields = '__all__'

# from django import forms
# from django.forms.widgets import RadioSelect, Select

# class PlanetForm(forms.Form):
#     # CHOICES = [('orbit', 'Orbit'), ('line', 'Line')]
#     planet_display = forms.RadioSelect(
#     widget=RadioSelect(
#         choices=[
#             ('', 'Unknown'),
#             (True, 'Yes'),
#             (False, 'No'),
#         ]
#     )
# )
   
    # random_display = forms.BooleanField(initial=True, required=True, label='Randomized Planet Placement?')
    
    
    
#     >>> from django import forms
# >>> CHOICES = [('1', 'First'), ('2', 'Second')]
# >>> choice_field = forms.ChoiceField(widget=forms.RadioSelect, choices=CHOICES)
# >>> choice_field.choices
# [('1', 'First'), ('2', 'Second')]
# >>> choice_field.widget.choices
# [('1', 'First'), ('2', 'Second')]
# >>> choice_field.widget.choices = []
# >>> choice_field.choices = [('1', 'First and only')]
# >>> choice_field.widget.choices
# [('1', 'First and only')]