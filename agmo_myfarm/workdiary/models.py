from django.db import models
from datetime import timezone
from work import models as work_model
from tracking import models as tracking_model
from django.contrib.gis.db import models

#데이터의 생성시간 업데이트 시간을 기록한다
class TimeStampedModel(models.Model):
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True

class WorkDiary(TimeStampedModel):
    fin_date = models.IntegerField(default=0, null=True)
    is_complete =models.BooleanField(default=False)

    workdiary_work_detail = models.ForeignKey(
        work_model.Works, 
        null=True, 
        on_delete=models.CASCADE, #외래키 갖는 유저 삭제시
        related_name='workdiary_work_workdetail'
        )
    #작업에 관련된 정보들을 work의 Wokrs에서 받아온다 여기에 작업 일자도 들어가있다

    workdiary_tracking = models.ForeignKey(
        tracking_model.Tracking, 
        null=True, 
        on_delete=models.CASCADE, #외래키 갖는 유저 삭제시
        related_name='workdiary_tracking_tracking'
        )
    #주행에 관련된 정보들을 tracking의 Tracking에서 받아온다

    workdiary_progress = models.ForeignKey(
        tracking_model.Progress, 
        null=True, 
        on_delete=models.CASCADE, #외래키 갖는 유저 삭제시
        related_name='workdiary_tracking_progress'
        )
    #진행률에 관련된 정보들을 tracking의 Progress에서 받아온다

    mymemo = models.TextField(blank=True)


    class Meta:
        app_label = 'workdiary'


# Create your models here.

# Create your models here.
