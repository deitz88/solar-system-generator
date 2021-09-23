from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('generate', views.generate, name='generate'), 
    path('generate-nebula', views.generate_nebula, name='generate-nebula'),
    path('planet', views.planet, name='planet'),
    path('nebula', views.nebula, name='nebula')
]