from django.shortcuts import render
from .forms import WorkDiaryForm  # forms.py에서 정의한 폼 import
from work.models import Works
from django.http import JsonResponse
from django.utils import timezone
from farm.models import FarmField
from .models import WorkDiary


def main(request):
    today_day = timezone.now().day
    content={
    'today_day': today_day,
    }

    return render(request, 'workdiary/workdiary_main.html', content)



def work_info_view(request):
    if request.method == 'GET':
        date = request.GET.get('date')  # 클라이언트에서 전달된 날짜를 가져옴

        try:
            work_records = Works.objects.all()
            data = []
            for work_record in work_records:
                start_date_day = int(work_record.start_date_day)
                end_date_day = int(work_record.end_date_day)
                query_date = int(date)
                if start_date_day <= query_date <= end_date_day:
                    data.append({
                        'date': date,
                        'machine_name':work_record.machine_name,
                        'field_name': work_record.work_fields.field_name,
                        'work_name': work_record.work_name,
                        'crop': work_record.work_fields.crop,
                        'user_memo': work_record.user_memo,
                    })
            return JsonResponse(data, safe=False)
        except Works.DoesNotExist:
            return JsonResponse({'error': '작업 정보를 찾을 수 없습니다.'}, status=404)
    else:
        return JsonResponse({'error': '잘못된 요청입니다.'}, status=400)
