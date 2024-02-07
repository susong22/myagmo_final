from django.urls import path
from . import views

app_name = "work"
urlpatterns = [
    path('work/', views.main, name='main'),
    path('work/add_work/', views.add_work, name='add_work'),
]