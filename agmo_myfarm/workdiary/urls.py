from django.urls import path
from . import views
from .views import work_info_view

app_name = "workdiary"
urlpatterns = [
    path('', views.main, name='workdiary_main'),
    path('workinfo', views.work_info_view, name='work_info'),
]