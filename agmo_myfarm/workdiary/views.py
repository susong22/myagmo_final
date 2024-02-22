from django.shortcuts import render
from work.models import Works
from django.http import JsonResponse
from django.utils import timezone
from datetime import datetime
from .models import WorkDiary
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseBadRequest
import json


def main(request):
    today_day = datetime.now().day
    content={
    'today_day': today_day,
    }

    return render(request, 'workdiary/workdiary_main.html', content)

def update_view(request):
    response_body = {"result": ""}
    if request.method == 'POST':
        diary_instance = WorkDiary.objects.first()
        # 날짜가 다르면  -> 그날 처음 완료하는거면
        if diary_instance.fin_date != int(datetime.now().day):
            diary_instance.fin_date = int(datetime.now().day)
            diary_instance.save()
            response_body["result"] = "change"
            return JsonResponse(status=200, data=response_body)
        else:
            response_body["result"] = "same"
            return JsonResponse(status=200, data=response_body)
    
    # POST 요청이 들어왔지만 작업 상태 업데이트에 실패한 경우
    return JsonResponse({'error': 'dasdfsdf.'}, status=500)



def work_info_view(request):
    if request.method == 'GET':
        date = request.GET.get('date')  # 클라이언트에서 전달된 날짜를 가져옴
        
        if not WorkDiary.objects.exists():
                diary_fin = WorkDiary()
                print('객체 생성')
                diary_fin.save()
        try:

            work_records = Works.objects.all()
            data = []
            for work_record in work_records:
                start_date_day = int(work_record.start_date_day)
                end_date_day = int(work_record.end_date_day)
                query_date = int(date)
                if start_date_day <= query_date <= end_date_day:
                    # 작업이 완료된 경우 'past' 상태로 설정
                    if query_date == WorkDiary.objects.first().fin_date:
                        status = 'past'
                    else:
                        # 작업이 완료되지 않은 경우 날짜에 따라 상태 설정
                        if query_date < datetime.now().day:
                            status = 'past'  # 현재 날짜보다 이전일 경우 'past' 상태로 설정
                        elif query_date == datetime.now().day:
                            status = 'current'  # 현재 날짜와 같거나 이후일 경우 'current' 상태로 설정
                        elif query_date > datetime.now().day:
                            status = 'future'
                    data.append({
                        'date': date,
                        'status': status,
                        'machine_name': work_record.machine_name,
                        'field_name': work_record.work_fields.field_name,
                        'work_name': work_record.work_name,
                        'crop': work_record.work_fields.crop,
                        'user_memo': work_record.user_memo,
                        'turn_over': work_record.turn_over,
                    })
            return JsonResponse(data, safe=False)
        except Works.DoesNotExist:
            return JsonResponse({'error': '작업 정보를 찾을 수 없습니다.'}, status=404)
    else:
        return JsonResponse({'error': '잘못된 요청입니다.'}, status=400)
    

def alert_map(request):
    response_body = {"result": ""}
    if request.method == 'POST':
        data = json.loads(request.body.decode('utf-8'))
        name = data.get('result', [])
        work_objects = Works.objects.filter(work_fields__field_name=name)
        print(work_objects)
        # 날짜가 다르면  -> 그날 처음 완료하는거면
        if 1:
            
            response_body["result"] = "change"
            return JsonResponse(status=200, data=response_body)
        else:
            response_body["result"] = "same"
            return JsonResponse(status=200, data=response_body)
    
    # POST 요청이 들어왔지만 작업 상태 업데이트에 실패한 경우
    return JsonResponse({'error': 'dasdfsdf.'}, status=500)