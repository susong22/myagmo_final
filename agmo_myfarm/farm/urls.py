from django.urls import path
from . import views

app_name = "farm"
urlpatterns = [
    path('', views.add_farmfield, name='add_farmfield'),
    path('delete_field/', views.delete_farmfield, name='delete_farmfield'),
    path('<int:farmId>/select', views.field_select, name='field_select'),
    path('save_markers/',views.save_markers, name='save_markers'),
    path('autocomplete/',views.autocomplete, name='autocomplete'),
    path('search_change/',views.search_change, name='search_change'),
]