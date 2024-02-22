from django.urls import path
from . import views

app_name = 'home'
urlpatterns = [
    path('', views.index, name='index'),
    path('path2/', views.path2, name='path2'),
    path('path3/', views.path3, name='path3'),
    path('path4/', views.path4, name='path4'),
]