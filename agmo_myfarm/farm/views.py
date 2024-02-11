import requests
import urllib.request
from django.shortcuts import render, redirect, get_object_or_404
from django.utils.translation import gettext_lazy as _
from .forms import FarmForm
from farm.models import FarmField
from . import models
from django.http import JsonResponse


def add_farmfield(request):
    if request.method == 'GET':
        farm_list = FarmField.objects.all()
        formset = FarmForm()
        content = {
            'formset': formset,
            'farm_list': farm_list,
        }
        return render(request, 'farm/add_farmfield.html', content)
    
    if request.method == 'POST':
            formset = FarmForm(request.POST)
            if formset.is_valid():
                for item in FarmField.objects.all():
                    item.is_selected = False
                    item.save()

                new_farm = formset.save()
                new_farm.is_selected = True
                new_farm.save()
                render(request, 'work/work_main.html')
                print('add_farmfield 폼이 저장되었습니다!')   
                return redirect('work:main')
            else:
                print(formset.errors)
                print(request.POST)
                formset = FarmForm() 


def field_select(request, farm_id):     
    response_body = {"result": ""}

    if request.method == 'POST':
        farm = get_object_or_404(models.FarmField, pk=farm_id)
        # 이미 선택된 경작지 선택
        if farm.is_selected:
            pass
        # 새로운 경작지 선택
        else:
            for item in FarmField.objects.all():
                item.is_selected = False
                item.save()   
                response_body["result"] = "change"
    
            farm.is_selected = True
            farm.save()
        
        return JsonResponse(status=200, data=response_body)
    
               
