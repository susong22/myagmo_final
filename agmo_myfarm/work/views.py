from .models import Works
from django.shortcuts import render
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

wea = FarmField()
work1 = Works(work_name = '작업1', machine_name = '써레', start_date_year='2024', start_date_month='02', start_date_day='08')
work2 = Works(work_name = '작업2', machine_name = '파종', start_date_year='2024', start_date_month='02', start_date_day='09')


def main(request):
    # request.session['wea'] = wea  # 이 객체를 다른 함수에서 사용하기 위해서는 Serializer 필요
    sky_status = {
            '1':"맑음", '3':'구름많음', '4': '흐림'
        }
    rain_status = {
        '0':"없음", '1':"비", '2':"비/눈", '3':"눈", '4':"소나기"
    }
    current_datetime = timezone.now()
    current_year = current_datetime.year
    current_month = current_datetime.month
    current_day = current_datetime.day

    if request.method == 'GET':
        url = 'http://apis.data.go.kr/1360000/VilageFcstInfoService_2.0/getVilageFcst'
        key = 'SlNT2UPLHyxPS1CHGdrY+oqL9cW0Y1WqeXzYEGT8LavFpbmcM1JNhXE8GZtZkggouJQgGddzzfVAjjnI89dIiA=='
        #date = '20240207'      # 20240203
        date = str(current_year) + str(current_month).zfill(2) + str(current_day).zfill(2)
        time = '0500'      # 0200부터 3시간 단위
        place = [55, 127]   # 위도, 경도    <- 다른 def 에서 불러와야함

        para = {
            'serviceKey':key, 'pageNo':'1', 'numOfRows':'20', 'dataType':'json', 
            'base_date':date, 'base_time':time, 'nx':place[0], 'ny':place[1]
        }

        wea.weather_date = date[0:4] +'년 ' + date[4:6] + '월 ' + date[6:8] + '일'
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
                if i['category'] == 'POP':    # 강수확률
                    wea.is_rain = i['fcstValue']
                elif i['category'] == 'PTY':    # 강수형태
                    rain_key = i['fcstValue']
                    wea.rain_sh = rain_status[rain_key]
                elif i['category'] == 'TMP':    # 기온
                    wea.temperature = i['fcstValue']
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
                else:
                    pass

            # 실제 구현에서는 이 정보들이 모두 채워져야지만 서치를 그만두도록 알고리즘 구성
            
            
        else:
            print("Error Code:" + rescode)
        return render(request, 'work/work_main.html', {'wea':wea})

def add_work(request):
        # wea = request.session.get('wea')
        day_list = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31]
        month_list = [1,2,3,4,5,6,7,8,9,10,11,12]
        year_list = [2024,2025,2026,2027,2028,2029,2030]


        farm1 = FarmField(field_name="경작지1")
        farm2 = FarmField(field_name="경작지2")
        farmfield_list = [farm1, farm2]
        machine_list = ['써레', '파종기', '스프레이어']
        crop_list = ['밀', '벼', '콩', '감자']

        if request.method == 'GET':
            formset = WorkForm()
            content = {
            'day_list' : day_list,
            'month_list' : month_list,
            'year_list' : year_list,
            'farm1' : farm1,
            'farm2' : farm2,
            'farmfield_list' : farmfield_list,
            'machine_list' : machine_list,
            'crop_list' : crop_list,
            'formset': formset,
            'wea':wea,
            }
            return render(request, 'work/add_work.html', content)
            

        if request.method == 'POST':
            formset = WorkForm(request.POST)
            if formset.is_valid():
                formset.save()
                render(request, 'work/work_main.html', {'wea':wea})
            else:
                print(formset.errors)
                print(request.POST)
                formset = WorkForm()  
                

        content = {
            'day_list' : day_list,
            'month_list' : month_list,
            'year_list' : year_list,
            'farm1' : farm1,
            'farm2' : farm2,
            'farmfield_list' : farmfield_list,
            'machine_list' : machine_list,
            'crop_list' : crop_list,
            'formset': formset,
            'wea':wea,
            }

        return render(request, 'work/add_work.html', content)


def get_expected_path(request):
    df = pd.read_csv(r'C:\Users\82105\Downloads\AGMO_Data_set1.csv', sheet_name='농지경계', header=None)

    # 특정 범위의 데이터를 선택합니다.
    selected_data = df.iloc[1:6, 1:3]  # B열 2번부터 C열 6번까지

    # 선택된 데이터를 딕셔너리 리스트로 변환합니다.
    expected_path = selected_data.to_dict(orient='records')

    tm_proj = Proj(init='epsg:5179')  # TM 좌표계 (EPSG:5179)
    wgs84_proj = Proj(init='epsg:4326')  # 위경도 좌표계 (EPSG:4326)

    expected_path_lonlat = []
    for point in expected_path:
        tm_x, tm_y = point['x'], point['y']
        lon, lat = transform(tm_proj, wgs84_proj, tm_x, tm_y)
        point['lon'] = lon
        point['lat'] = lat
        expected_path_lonlat.append(point)
        print(f"TM 좌표: ({tm_x}, {tm_y}), 위경도 좌표: ({lon}, {lat})")

    json_expected_path = json.dumps(expected_path_lonlat)
# 이부분에서 문제가 발생한다. JSON 형태로 바꾸는부분에서ㅜㅜ 
    print(json.dumps(expected_path_lonlat))

    return render(request, 'work/work_main.html', {'json_expected_path':json_expected_path})

def add_machine_card(request):
    if request.method == 'GET':
        for obj in Works.objects.all():
            pass
