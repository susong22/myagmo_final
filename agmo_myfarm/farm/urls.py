from django.urls import path
from . import views

app_name = "farm"
urlpatterns = [
    path('', views.add_farmfield, name='add_farmfield'),
    path('<int:farm_id>/select', views.field_select, name='field_select'),
    path('save_markers/',views.save_markers, name='save_markers'),
]