from django.urls import path
from . import views

app_name = "tracking"
urlpatterns = [
    path('', views.main, name='main'),
    path('save_points/',views.save_points, name='save_points'),
    path('save_markers/',views.save_markers, name='save_markers'),
]