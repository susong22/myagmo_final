from django.urls import path
from . import views

app_name = "farm"
urlpatterns = [
    path('', views.main, name='main'),
]