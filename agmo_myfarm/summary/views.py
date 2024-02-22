from django.shortcuts import render
from django.utils import timezone
from farm.models import FarmField
import requests
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404, redirect
from farm.models import FarmField
import json


def main(request):
    today_day = timezone.now().day
    farm_list = FarmField.objects.all()
    content={
        'today_day': today_day,
        'farm_list':farm_list,
    }

    return render(request, 'summary/summary_main.html', content)


def field_select(request, farmId):     
    response_body = {"result": ""}

    if request.method == 'POST':
        farm = get_object_or_404(FarmField, pk=farmId)
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

def search_change(request):
    response_body = {"result": ""}
    if request.method == 'POST':
        data = json.loads(request.body.decode('utf-8'))
        name = data.get('result', [])
        farmfields = FarmField.objects.all()
        farm = get_object_or_404(FarmField, field_name = name)
        for item in farmfields:
            item.is_selected = False
            item.save()
        farm.is_selected = True
        farm.save()
        response_body["result"] = "change"

    return JsonResponse(status=200, data=response_body)



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
    farm_selected=FarmField.objects.filter(is_selected=True)[0]
    price_data=""
    nongjin_link=""
    crop_name = farm_selected.crop
    if crop_name:

        first_letter=crop_name[0]
        if crop_name and crop_name[0] == '쌀':
            price_data = "https://www.kamis.or.kr/customer/price/wholesale/item.do?action=priceinfo&productclscode=02&regday=2024-02-21&graderank=&itemcategorycode=100&itemcode=111&kindcode=EE&countycode=&convert_kg_yn=N"
            nongjin_link="https://www.nongsaro.go.kr/portal/search/nongsaroSearch.ps?categoryName=SCH01&menuId=PS00007&option=0&sortOrdr=01&searchWord=%EC%8C%80"
        elif crop_name and crop_name[0] == '콩':
            price_data = "https://www.kamis.or.kr/customer/price/wholesale/item.do?action=priceinfo&regday=2024-02-21&itemcategorycode=100&itemcode=141&kindcode=&productrankcode=&convert_kg_yn=N"
            nongjin_link="https://www.nongsaro.go.kr/portal/search/nongsaroSearch.ps?menuId=PS00007&categoryName=SCH01&sortOrdr=01&pageIndex=1&pageSize=10&pageUnit=10&includeWord=&exEqWord=&ikEqWork=&excludeWord=&Hflag=&qura=&reCountingYn=Y&field=SCH01&searchWord=%EC%BD%A9"
        elif crop_name and crop_name[0] == '팥':
            price_data = "https://www.kamis.or.kr/customer/price/wholesale/item.do?action=priceinfo&regday=2024-02-21&itemcategorycode=100&itemcode=142&kindcode=&productrankcode=&convert_kg_yn=N"
            nongjin_link="https://www.nongsaro.go.kr/portal/search/nongsaroSearch.ps?menuId=PS00007&categoryName=SCH01&sortOrdr=01&pageIndex=1&pageSize=10&pageUnit=10&includeWord=&exEqWord=&ikEqWork=&excludeWord=&Hflag=&qura=&reCountingYn=Y&field=SCH01&searchWord=%ED%8C%A5"
        elif crop_name and crop_name[0] == '녹두':
            price_data= "https://www.kamis.or.kr/customer/price/wholesale/item.do?action=priceinfo&regday=2024-02-21&itemcategorycode=100&itemcode=143&kindcode=&productrankcode=&convert_kg_yn=N"
            nongjin_link="https://www.nongsaro.go.kr/portal/search/nongsaroSearch.ps?menuId=PS00007&categoryName=SCH01&sortOrdr=01&pageIndex=1&pageSize=10&pageUnit=10&includeWord=&exEqWord=&ikEqWork=&excludeWord=&Hflag=&qura=&reCountingYn=Y&field=SCH01&searchWord=%EB%85%B9%EB%91%90"


    content={
        'nongjin_link':nongjin_link,
        'first_letter':first_letter,
        'price_data':price_data,
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
    for farm in farm_list:
        field= farm.field_name


    content={
        'field':field,
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