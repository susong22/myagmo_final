from django.urls import path
from . import views

app_name = "work"
urlpatterns = [
    path('', views.main, name='main'),
    path('add_work/', views.add_work, name='add_work'),
    path('empty/', views.main, name='empty'),
    path('add_work/save_points/',views.save_points, name='save_points'),
    path('<int:card_id>/delete', views.del_work, name='del'),
    
]