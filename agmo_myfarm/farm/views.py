import requests
import urllib.request
from django.shortcuts import render, redirect, get_object_or_404
from django.utils.translation import gettext_lazy as _
from .forms import FarmForm
from farm.models import FarmField
from work.models import Works
from . import models
from django.http import JsonResponse
import json
from tracking.models import Tracking
from django.contrib.gis.geos import GEOSGeometry
from django.contrib.gis.geos import MultiPoint
from django.views.decorators.http import require_POST
from django.core.serializers import serialize
from django.db import IntegrityError




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
                session_data = request.session.get('field_point', None)
                if session_data is not None and session_data[1] > 0 and session_data[3] > 0:
                    try:
                        point = {
                            'lat': session_data[2]/session_data[3],
                            'lng': session_data[0]/session_data[1],
                        }
                        # y,x 꼴 (lat, lng)

                        for item in FarmField.objects.all():
                            item.is_selected = False
                            item.save()

                        new_farm = formset.save()
                        new_farm.is_selected = True
                        new_farm.location = point
                        new_farm.crop = []
                        new_farm.save()
                        print('add_farmfield 폼이 저장되었습니다!')  
                        print(new_farm.location) 
                        return redirect('work:main')
                    except IntegrityError:
                        print('경작지 이름이 중복됩니다.')
                        return redirect('farm:add_farmfield')
                else:
                    print('위치를 정확하게 입력해주십시오.')
                    return redirect('farm:add_farmfield')
                    
            else:
                print(formset.errors)
                print(request.POST)
                formset = FarmForm() 

def delete_farmfield(request):
    
        Works.objects.all().delete()
        FarmField.objects.all().delete()

        return redirect('work:main')

def field_select(request, farmId):     
    response_body = {"result": ""}

    if request.method == 'POST':
        farm = get_object_or_404(models.FarmField, pk=farmId)
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

def save_markers(request):
    if request.method == 'POST':
        data = json.loads(request.body.decode('utf-8'))
        x_sum = 0
        x_count = 0
        y_sum = 0
        y_count = 0
        marker_coordinates = data.get('markers', [])
        print(marker_coordinates)
        for coordinate in marker_coordinates:
            x_sum += coordinate['lng']
            x_count += 1
            y_sum += coordinate['lat']
            y_count += 1

        session_data = (x_sum, x_count, y_sum, y_count)

        request.session['field_point'] = session_data
        response_data = {'data': session_data}

        return JsonResponse(response_data)
    else:
        return JsonResponse({'success': False})
    

@require_POST
def autocomplete(request):
    search_term = request.POST.get('search_term', '')
    # 여기에서 적절한 방식으로 검색을 수행하고 결과를 생성합니다.
    field_list = FarmField.objects.filter(field_name__icontains=search_term)
    if len(field_list) != 0: 
        results = serialize('json', field_list)
        return JsonResponse({'results': results})
    else:
        results = serialize('json', {})
        print('흠')
        return JsonResponse({'results': results})

def search_change(request):
    response_body = {"result": ""}
    if request.method == 'POST':
        data = json.loads(request.body.decode('utf-8'))
        name = data.get('result', [])
        farmfields = FarmField.objects.all()
        farm = get_object_or_404(models.FarmField, field_name = name)
        for item in farmfields:
            item.is_selected = False
            item.save()
        farm.is_selected = True
        farm.save()
        response_body["result"] = "change"

    return JsonResponse(status=200, data=response_body)