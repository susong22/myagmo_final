from django.shortcuts import render
from django.utils import timezone
from farm.models import FarmField

def main(request):
    today_day = timezone.now().day
    farm_list = FarmField.objects.all()
    content={
    'today_day': today_day,
    'farm_list':farm_list,
    }

    return render(request, 'summary/summary_main.html', content)

def machine_center(request):
    today_day = timezone.now().day
    farm_list = FarmField.objects.all()
    content={
    'today_day': today_day,
    'farm_list':farm_list,
    }
    return render(request, 'summary/machine_center.html', content)

def my_crop(request):
    today_day = timezone.now().day
    farm_list = FarmField.objects.all()
    content={
    'today_day': today_day,
    'farm_list':farm_list,
    }
    return render(request, 'summary/my_crop.html', content)

def soil_water(request):
    today_day = timezone.now().day
    farm_list = FarmField.objects.all()
    content={
    'today_day': today_day,
    'farm_list':farm_list,
    }
    return render(request,'summary/soil_water.html', content)

def soil(request):
    today_day = timezone.now().day
    farm_list = FarmField.objects.all()
    content={
    'today_day': today_day,
    'farm_list':farm_list,
    }
    return render(request,'summary/soil.html', content)

def solution(request):
    today_day = timezone.now().day
    farm_list = FarmField.objects.all()
    content={
    'today_day': today_day,
    'farm_list':farm_list,
    }
    return render(request, 'summary/solution.html', content)
