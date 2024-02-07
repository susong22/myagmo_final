from django.shortcuts import render
from .models import Works
from farm.models import FarmField

def main(request):
    pass

def add_work(request):
    # wea = request.session.get('wea')
    work_obj = Works()
    farm1 = FarmField()
    farm2 = FarmField()
    if request.method == 'POST':
        pass

    return render(request, 'work/add_work.html')
