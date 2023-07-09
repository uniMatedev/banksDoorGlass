from django.urls import path
from . import views

urlpatterns = [
    path('hello/', views.hello_world, name='hello_world'),
    path('convert_units/', views.convert_units, name='convert_units'),
    path('convert_volume/', views.convert_volume, name='convert_volume'),
    path('convert_area/', views.convert_area, name='convert_area'),
    path('convert_temperature/', views.convert_temperature, name='convert_temperature'),
    path('convert_time/', views.convert_time, name='convert_time'),
    path('convert_speed/', views.convert_speed, name='convert_speed'),
    path('convert_weight/', views.convert_weight, name='convert_weight'),
    path('convert_energy/', views.convert_energy, name='convert_energy'),
    path('convert_pressure/', views.convert_pressure, name='convert_pressure'),
]
