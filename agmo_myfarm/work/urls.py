from django.urls import path
from . import views

app_name = "work"
urlpatterns = [
    path('add_work/', views.add_work, name='add_work'),
]