from django.urls import path
from . import views


app_name = "summary"
urlpatterns = [
    path('', views.main, name='summary_main'),
    path('machine_center/', views.machine_center, name='machine_center'),
    path('my_crop/', views.my_crop, name='my_crop'),
    path('soil_water/', views.soil_water, name='soil_water'),
    path('soil/', views.soil, name='soil'),
    path('solution/', views.solution, name='solution'),
]