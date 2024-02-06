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
from work.models import Weather

def main(request):
    wea = Weather()
    # request.session['wea'] = wea  # 이 객체를 다른 함수에서 사용하기 위해서는 Serializer 필요
    sky_status = {
            '1':"맑음", '3':'구름많음', '4': '흐림'
        }
    rain_status = {
        '1':"없음", '1':"비", '2':"비/눈", '3':"눈", '4':"소나기"
    }

    if request.method == 'GET':
        url = 'http://apis.data.go.kr/1360000/VilageFcstInfoService_2.0/getVilageFcst'
        key = 'SlNT2UPLHyxPS1CHGdrY+oqL9cW0Y1WqeXzYEGT8LavFpbmcM1JNhXE8GZtZkggouJQgGddzzfVAjjnI89dIiA=='
        date = '20240205'      # 20240203
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
        return render(request, 'farm/farm_main.html', {'wea':wea})
    

