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
