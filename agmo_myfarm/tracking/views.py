from django.shortcuts import render
from .models import Tracking, Progress
from work.models import Works
from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from django.views.generic import DetailView, RedirectView, UpdateView
from django.http import JsonResponse
from django.contrib.gis.geos import Point
from .models import Tracking
import json
import requests
import urllib.request
from django.views.decorators.csrf import csrf_exempt
from django.contrib.gis.geos import GEOSGeometry
from django.contrib.gis.geos import MultiPoint

def main(request):
    # tracking.html 템플릿을 렌더링하여 HTTP 응답으로 반환합니다.
    return render(request, 'tracking/tracking.html')

def save_points(request):
    if request.method == 'POST':
        #start_lat = float(request.POST.get('start_lat'))
        #start_lng = float(request.POST.get('start_lng'))

        #end_lat = float(request.POST.get('end_lat'))
        #end_lng = float(request.POST.get('end_lng'))

        # 받은 좌표를 Point 객체로 변환하여 start_point 필드에 저장합니다.
        #start_point = Point(start_lng, start_lat)
        #end_point = Point(end_lat, end_lng)  
        data = json.loads(request.body.decode('utf-8'))
        points_coordinates = data.get('points', [])


        start_point_co = points_coordinates[0]
        end_point_co = points_coordinates[1]

        start_point = GEOSGeometry(f"POINT({start_point_co['lng']} {start_point_co['lat']})")
        end_point = GEOSGeometry(f"POINT({end_point_co['lng']} {end_point_co['lat']})")
        print(start_point,end_point)
        my_model_instance = Tracking()
        my_model_instance.start_point_t = start_point
        my_model_instance.end_point_t = end_point
        my_model_instance.save()


        # Point 객체의 인자는 (경도, 위도) 순서입니다.

        #tracking_data = Tracking.objects.create(start_point_t=start_point, end_point_t=end_point)

        #tracking_data.save()

        # JSON 형태로 응답합니다.
        return JsonResponse({'message': 'Start point saved successfully.'})
    else:
        # POST 요청이 아닌 경우 에러 메시지를 반환합니다.
        return JsonResponse({'error': 'POST method required.'}, status=400)
    

def save_markers(request):
    if request.method == 'POST':
        data = json.loads(request.body.decode('utf-8'))
        marker_coordinates = data.get('markers', [])
        print(marker_coordinates)

        # Point 객체로 변환하여 리스트에 저장
        markers = [GEOSGeometry(f"POINT({coordinate['lng']} {coordinate['lat']})") for coordinate in marker_coordinates]
        print(markers)
        # MyModel에 저장하기
        my_model_instance = Tracking()
        my_model_instance.markers = MultiPoint(markers)
        my_model_instance.save()

        return JsonResponse({'success': True})
    else:
        return JsonResponse({'success': False})