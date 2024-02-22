from django.urls import path
from . import views

app_name = "workdiary"
urlpatterns = [
    path('', views.main, name='workdiary_main'),
    path('workinfo', views.work_info_view, name='work_info'),
    path('update/', views.update_view, name='update'),
    path('alert_map/', views.alert_map, name='alert_map'),
]