from .models import Works
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from django.views.generic import DetailView, RedirectView, UpdateView
import json
import requests
import urllib.request
from farm.models import FarmField
from .models import Works
from django.utils import timezone
from .forms import WorkForm
from django.contrib.gis.geos import GEOSGeometry
from django.contrib.gis.geos import MultiPoint
from django.http import JsonResponse
from datetime import datetime, timedelta
from home.path import calculate_paths
from home.path2 import calculate_paths2
from home.path3 import calculate_paths3
from home.path4 import calculate_paths4




def main(request):
    today = datetime.now().date()
    
    # 4일 후의 날짜까지 생성
    day_week = [today + timedelta(days=i) for i in range(4)]
    day_list = [(today + timedelta(days=i)).strftime("%m.%d") for i in range(4)]


    if request.method == 'GET':
        farm_list = FarmField.objects.all()
        if FarmField.objects.exists():
            if Works.objects.filter(work_fields=FarmField.objects.filter(is_selected=True)[0]):
                if FarmField.objects.filter(is_selected=True)[0].field_name == '경작지1':
                    traveled_path_data, expected_path_data, roll_data_past, roll_data_future, pitch_data_past, pitch_data_future = calculate_paths2()
                    print('a')

                elif FarmField.objects.filter(is_selected=True)[0].field_name == '경작지2':
                    traveled_path_data, expected_path_data, roll_data_past, roll_data_future, pitch_data_past, pitch_data_future = calculate_paths3() 
                    print('b')

                elif FarmField.objects.filter(is_selected=True)[0].field_name == '경작지3':
                    traveled_path_data, expected_path_data, roll_data_past, roll_data_future, pitch_data_past, pitch_data_future = calculate_paths4()
                    print('c')
                else: 
                    traveled_path_data, expected_path_data, roll_data_past, roll_data_future, pitch_data_past, pitch_data_future = calculate_paths3()
                    print('d')
            else: 
                traveled_path_data, expected_path_data, roll_data_past, roll_data_future, pitch_data_past, pitch_data_future = calculate_paths()
                print('e')
        else:
            return render(request, 'work/empty.html')    

        traveled_path_json = json.dumps(traveled_path_data.tolist())
        expected_path_json = json.dumps(expected_path_data.tolist())
        roll_data_past_json = json.dumps(roll_data_past.tolist())
        roll_data_future_json = json.dumps(roll_data_future.tolist())
        pitch_data_past_json = json.dumps(pitch_data_past.tolist())
        pitch_data_future_json = json.dumps(pitch_data_future.tolist())
                
        if FarmField.objects.exists():
            work_list = Works.objects.all()
            if Works.objects.exists():
                is_work = True
            else:
                is_work = False

            wea = weather_obj()
            
            content = {
                'wea':wea,
                'is_work':is_work,
                'work_list':work_list,
                'day_week':day_week,
                'farm_list': farm_list,
                'day_list': day_list,
                'traveled_path_json': traveled_path_json, 
                'expected_path_json': expected_path_json, 
                'roll_data_past_json': roll_data_past_json,
                'roll_data_future_json': roll_data_future_json,
                'pitch_data_past_json': pitch_data_past_json,
                'pitch_data_future_json': pitch_data_future_json
            }
            return render(request, 'work/work_main.html', content)
        else:
            return render(request, 'work/empty.html')

def add_work(request):
        day_list = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31]
        month_list = [1,2,3,4,5,6,7,8,9,10,11,12]
        year_list = [2024,2025,2026,2027,2028,2029,2030]
        farmfield_list = FarmField.objects.all()
        machine_list = ['써레', '파종기', '스프레이어']
        crop_list = ['쌀', '콩', '팥', '녹두']

        if request.method == 'GET':

            formset = WorkForm()
            content = {
            'day_list' : day_list,
            'month_list' : month_list,
            'year_list' : year_list,
            'farmfield_list' : farmfield_list,
            'machine_list' : machine_list,
            'crop_list' : crop_list,
            'formset': formset,
            }

            return render(request, 'work/add_work.html', content)
            

        if request.method == 'POST':
            formset = WorkForm(request.POST)
            
            if formset.is_valid():
                session_data = request.session.get('field_point', None)
                if session_data is not None and session_data[0] > 0 and session_data[2] > 0:
                    start = GEOSGeometry(f"POINT({session_data[0]} {session_data[1]})")
                    end = GEOSGeometry(f"POINT({session_data[2]} {session_data[3]})")
                    
                    new_work = formset.save()
                    new_work.start_point = start
                    new_work.end_point = end
                    new_work.work_fields
                    matching_farm_fields = FarmField.objects.filter(field_name=new_work.work_fields.field_name)[0]
                    if len(matching_farm_fields.crop) != 0:
                        if new_work.crop not in matching_farm_fields.crop:
                            matching_farm_fields.crop.append(new_work.crop)
                            matching_farm_fields.save()
                    else:
                        matching_farm_fields.crop.append(new_work.crop)
                        matching_farm_fields.save()
                        print(matching_farm_fields.crop)

                    render(request, 'work/work_main.html')
                    print('add_work 폼이 저장되었습니다!')
                    print(start, end)
                    return redirect('work:main')
            else:
                print(formset.errors)
                print(request.POST)
                formset = WorkForm()  
                

        content = {
            'day_list' : day_list,
            'month_list' : month_list,
            'year_list' : year_list,
            'farmfield_list' : farmfield_list,
            'machine_list' : machine_list,
            'crop_list' : crop_list,
            'formset': formset,
            'matching_farm_fields':matching_farm_fields,
            }

        return render(request, 'work/add_work.html', content)


def del_work(request, card_id):
    response_body = {"result": ""}
    if request.method == 'POST':
        card = get_object_or_404(Works, pk=card_id)
        card.delete()
        response_body["result"] = "change"
        return JsonResponse(status=200, data=response_body)

def save_points(request):
    if request.method == 'POST':
        data = json.loads(request.body.decode('utf-8'))
        points_coordinates = data.get('points', [])


        start_point_co = points_coordinates[0]
        end_point_co = points_coordinates[1]
        session_data = (start_point_co['lng'], start_point_co['lat'], end_point_co['lng'], end_point_co['lat'])

        request.session['field_point'] = session_data
        response_data = {'data': session_data}

        start_point = GEOSGeometry(f"POINT({start_point_co['lng']} {start_point_co['lat']})")
        end_point = GEOSGeometry(f"POINT({end_point_co['lng']} {end_point_co['lat']})")

        # Point 객체의 인자는 (경도, 위도) 순서입니다.

        # JSON 형태로 응답합니다.
        return JsonResponse(response_data)
    else:
        # POST 요청이 아닌 경우 에러 메시지를 반환합니다.
        return JsonResponse({'error': 'POST method required.'}, status=400)

def weather_obj():
    sky_status = {
            '1':"맑음", '3':'구름많음', '4': '흐림'
        }
    rain_status = {
        '0':"없음", '1':"비", '2':"비/눈", '3':"눈", '4':"소나기"
    }
    current_datetime = datetime.now()
    current_year = current_datetime.year
    current_month = current_datetime.month
    current_day = current_datetime.day
    current_day_of_week = current_datetime.strftime('%A')
    translated_day_of_week = _(current_day_of_week)   # 한글로 번역된 요일
    
    wea = FarmField.objects.filter(is_selected=True)[0]
    if wea.weather_date != None: # wea 정보가 있으면
        if int(wea.weather_date[10:12]) != current_day: # 날짜가 바뀌면 새롭게 정보 등록
            url = 'http://apis.data.go.kr/1360000/VilageFcstInfoService_2.0/getVilageFcst'
            key = 'SlNT2UPLHyxPS1CHGdrY+oqL9cW0Y1WqeXzYEGT8LavFpbmcM1JNhXE8GZtZkggouJQgGddzzfVAjjnI89dIiA=='
             # 20240203
            date = str(current_year) + str(current_month).zfill(2) + str(current_day-1).zfill(2)
            time = '0200'      # 0200부터 3시간 단위
            place = [55, 127]   # 위도, 경도    <- 다른 def 에서 불러와야함

            para = {
                'serviceKey':key, 'pageNo':'1', 'numOfRows':'2000', 'dataType':'json', 
                'base_date':date, 'base_time':time, 'nx':place[0], 'ny':place[1]
            }

            wea.weather_date = date[0:4] +'년 ' + date[4:6] + '월 ' + date[6:8] + '일(' + translated_day_of_week[0] + ')'
            wea.weather_time = time
            

            res = requests.get(url, params=para)
            search_request = urllib.request.Request(res.url)
            new_url = res.url
            response = urllib.request.urlopen(search_request)
            rescode = response.getcode()
            if rescode==200:
                response_body = response.read()
                result = json.loads(response_body.decode('UTF-8'))
                items = result["response"]['body']['items']['item']
                for i in items:
                    # 오늘 정보 채우기
                    if int(i['fcstDate']) == int(date): 
                        if i['category'] == 'POP':    # 강수확률
                            wea.is_rain = i['fcstValue']
                        elif i['category'] == 'PTY':    # 강수형태
                            rain_key = i['fcstValue']
                            wea.rain_sh = rain_status[rain_key]
                        elif i['category'] == 'TMP':    # 기온
                            wea.temperature = int(float(i['fcstValue']))
                        elif i['category'] == 'REH':   # 습도
                            wea.humidity = i['fcstValue']
                        elif i['category'] == 'VEC':   # 풍향
                            float_value = float(i['fcstValue'])
                            if 337.5 < float_value or float_value <= 22.5:
                                wea.wind_direction = '북풍'
                            elif 22.5 < float_value <= 67.5:
                                wea.wind_direction = '북동풍'
                            elif 67.5 < float_value <= 112.5:
                                wea.wind_direction = '동풍'
                            elif 112.5 < float_value <= 157.5:
                                wea.wind_direction = '남동풍'
                            elif 157.5 < float_value <= 202.5:
                                wea.wind_direction = '남풍'
                            elif 202.5 < float_value <= 247.5:
                                wea.wind_direction = '남서풍'
                            elif 247.5 < float_value <= 292.5:
                                wea.wind_direction = '서풍'
                            else:
                                wea.wind_direction = '북서풍'

                        elif i['category'] == 'WSD':   # 풍속
                            wea.wind_speed = i['fcstValue']
                        elif i['category'] == 'SKY':   # 하늘상태
                            sky_key = i['fcstValue']
                            wea.sky_sh = sky_status[sky_key]
                        elif i['category'] == 'TMX':    # 최고기온
                            wea.max_tem = int(float(i['fcstValue']))
                        elif i['category'] == 'TMN':    # 최저기온
                            wea.min_tem = int(float(i['fcstValue']))
                        else:
                            pass

                    # 다음날 정보 채우기    (비 형태, 최고 및 최저 기온)
                    elif int(i['fcstDate']) == int(date)+1 :
                        
                        if i['category'] == 'PTY':    # 강수형태
                            rain_key2 = i['fcstValue']
                            wea.one_after_rain_sh = rain_status[rain_key2]
                        elif i['category'] == 'SKY':   # 하늘상태
                            sky_key2 = i['fcstValue']
                            wea.one_after_sky_sh = sky_status[sky_key2]
                        elif i['category'] == 'TMX':    # 최고기온
                            wea.one_after_max = int(float(i['fcstValue']))
                        elif i['category'] == 'TMN':    # 최저기온
                            wea.one_after_min = int(float(i['fcstValue']))

                    # 그 다음날 정보 채우기
                    elif int(i['fcstDate']) == int(date)+2 :    
                        if i['category'] == 'PTY':    # 강수형태
                            rain_key3 = i['fcstValue']
                            wea.two_after_rain_sh = rain_status[rain_key3]
                        elif i['category'] == 'SKY':   # 하늘상태
                            sky_key3 = i['fcstValue']
                            wea.two_after_sky_sh = sky_status[sky_key3]
                        elif i['category'] == 'TMX':    # 최고기온
                            wea.two_after_max = int(float(i['fcstValue']))
                        elif i['category'] == 'TMN':    # 최저기온
                            wea.two_after_min = int(float(i['fcstValue']))

                    # 그그 다음날 정보 채우기
                    elif int(i['fcstDate']) == int(date)+3 :    
                        if i['category'] == 'PTY':    # 강수형태
                            rain_key4 = i['fcstValue']
                            wea.three_after_rain_sh = rain_status[rain_key4]
                        elif i['category'] == 'SKY':   # 하늘상태
                            sky_key4 = i['fcstValue']
                            wea.three_after_sky_sh = sky_status[sky_key4]
                        elif i['category'] == 'TMX':    # 최고기온
                            wea.three_after_max = int(float(i['fcstValue']))
                        elif i['category'] == 'TMN':    # 최저기온
                            wea.three_after_min = int(float(i['fcstValue']))
                
                # 실제 구현에서는 이 정보들이 모두 채워져야지만 서치를 그만두도록 알고리즘 구성
                wea.save()
                
            else:
                print("Error Code:" + rescode)


    else: # wea 정보가 없으면
        url = 'http://apis.data.go.kr/1360000/VilageFcstInfoService_2.0/getVilageFcst'
        key = 'SlNT2UPLHyxPS1CHGdrY+oqL9cW0Y1WqeXzYEGT8LavFpbmcM1JNhXE8GZtZkggouJQgGddzzfVAjjnI89dIiA=='
        #date = '20240207'      # 20240203
        date = str(current_year) + str(current_month).zfill(2) + str(current_day-1).zfill(2)
        time = '0200'      # 0200부터 3시간 단위
        place = [55, 127]   # 위도, 경도    <- 다른 def 에서 불러와야함
        para = {
            'serviceKey':key, 'pageNo':'1', 'numOfRows':'2000', 'dataType':'json', 
            'base_date':date, 'base_time':time, 'nx':place[0], 'ny':place[1]
        }

        wea.weather_date = date[0:4] +'년 ' + date[4:6] + '월 ' + date[6:8] + '일(' + translated_day_of_week[0] + ')'
        wea.weather_time = time
        

        res = requests.get(url, params=para)
        search_request = urllib.request.Request(res.url)
        new_url = res.url
        response = urllib.request.urlopen(search_request)
        rescode = response.getcode()
        if rescode==200:
            response_body = response.read()
            result = json.loads(response_body.decode('UTF-8'))
            items = result["response"]['body']['items']['item']

            for i in items:
                # 오늘 정보 채우기
                if int(i['fcstDate']) == int(date): 
                    if i['category'] == 'POP':    # 강수확률
                        wea.is_rain = i['fcstValue']
                    elif i['category'] == 'PTY':    # 강수형태
                        rain_key = i['fcstValue']
                        wea.rain_sh = rain_status[rain_key]
                    elif i['category'] == 'TMP':    # 기온
                        wea.temperature = int(float(i['fcstValue']))
                    elif i['category'] == 'REH':   # 습도
                        wea.humidity = i['fcstValue']
                    elif i['category'] == 'VEC':   # 풍향
                        float_value = float(i['fcstValue'])
                        if 337.5 < float_value or float_value <= 22.5:
                            wea.wind_direction = '북풍'
                        elif 22.5 < float_value <= 67.5:
                            wea.wind_direction = '북동풍'
                        elif 67.5 < float_value <= 112.5:
                            wea.wind_direction = '동풍'
                        elif 112.5 < float_value <= 157.5:
                            wea.wind_direction = '남동풍'
                        elif 157.5 < float_value <= 202.5:
                            wea.wind_direction = '남풍'
                        elif 202.5 < float_value <= 247.5:
                            wea.wind_direction = '남서풍'
                        elif 247.5 < float_value <= 292.5:
                            wea.wind_direction = '서풍'
                        else:
                            wea.wind_direction = '북서풍'

                    elif i['category'] == 'WSD':   # 풍속
                        wea.wind_speed = i['fcstValue']
                    elif i['category'] == 'SKY':   # 하늘상태
                        sky_key = i['fcstValue']
                        wea.sky_sh = sky_status[sky_key]
                    elif i['category'] == 'TMX':    # 최고기온
                        wea.max_tem = int(float(i['fcstValue']))
                    elif i['category'] == 'TMN':    # 최저기온
                        wea.min_tem = int(float(i['fcstValue']))
                    else:
                        pass

                # 다음날 정보 채우기    (비 형태, 최고 및 최저 기온)
                elif int(i['fcstDate']) == int(date)+1 :
                    if i['category'] == 'PTY':    # 강수형태
                        rain_key2 = i['fcstValue']
                        wea.one_after_rain_sh = rain_status[rain_key2]
                    elif i['category'] == 'SKY':   # 하늘상태
                        sky_key2 = i['fcstValue']
                        wea.one_after_sky_sh = sky_status[sky_key2]
                    elif i['category'] == 'TMX':    # 최고기온
                        wea.one_after_max = int(float(i['fcstValue']))
                    elif i['category'] == 'TMN':    # 최저기온
                        wea.one_after_min = int(float(i['fcstValue']))

                # 그 다음날 정보 채우기
                elif int(i['fcstDate']) == int(date)+2 :    
                    if i['category'] == 'PTY':    # 강수형태
                        rain_key3 = i['fcstValue']
                        wea.two_after_rain_sh = rain_status[rain_key3]
                    elif i['category'] == 'SKY':   # 하늘상태
                        sky_key3 = i['fcstValue']
                        wea.two_after_sky_sh = sky_status[sky_key3]
                    elif i['category'] == 'TMX':    # 최고기온
                        wea.two_after_max = int(float(i['fcstValue']))
                    elif i['category'] == 'TMN':    # 최저기온
                        wea.two_after_min = int(float(i['fcstValue']))

                # 그그 다음날 정보 채우기
                elif int(i['fcstDate']) == int(date)+3 :    
                    if i['category'] == 'PTY':    # 강수형태
                        rain_key4 = i['fcstValue']
                        wea.three_after_rain_sh = rain_status[rain_key4]
                    elif i['category'] == 'SKY':   # 하늘상태
                        sky_key4 = i['fcstValue']
                        wea.three_after_sky_sh = sky_status[sky_key4]
                    elif i['category'] == 'TMX':    # 최고기온
                        wea.three_after_max = int(i['fcstValue'])
                    elif i['category'] == 'TMN':    # 최저기온
                        wea.three_after_min = int(i['fcstValue'])

            # 실제 구현에서는 이 정보들이 모두 채워져야지만 서치를 그만두도록 알고리즘 구성
            wea.save()
            
        else:
            print("Error Code:" + rescode)
    return wea


