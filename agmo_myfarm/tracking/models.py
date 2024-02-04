from django.db import models
from work import models as work_model
from django.contrib.gis.db import models

#데이터의 생성시간 업데이트 시간을 기록한다
class TimeStampedModel(models.Model):
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True

class Tracking(TimeStampedModel):
    track_work_name = models.ForeignKey(
        work_model.Works, 
        null=True, 
        on_delete=models.CASCADE, #외래키 갖는 유저 삭제시
        related_name='tracking_work_work_name'
        )
    #작업명을 work의 Wokrs에서 받아온다

    track_expected_path = models.ForeignKey(
        work_model.Works, 
        null=True, 
        on_delete=models.CASCADE, #외래키 갖는 유저 삭제시
        related_name='tracking_work_expected_path'
        )
    #예상 경로를 work의 Works에서 받아온다

    current_point = models.PointField(blank=True, null=True)

    #실시간 좌표값을 전송받는다 해당 로직은 다시 구성필요

    traveled_path = models.PointField(blank=True, null=True)

    def __str__(self):
        return f'Coordinates: {self.traveled_path.x}, {self.traveled_path.y}'
    #주행기록에 관한 데이터이다. 다만 PointField는 소규모 좌표에 적합하기 때문에, 실시간으로 방대한 양의 데이터를
    #받아올 예정이라면 PostGIS 등을 이용하는 것이 좋다.
    #실시간 서버통신이 힘들 것 같다면 수기로 입력하는 방법도 고려해볼 것.

    roll = models.FloatField()
    pitch = models.FloatField()

    height = models.FloatField()
    
    class Meta:
        app_label = 'tracking'

class Progress(TimeStampedModel):
    progress = models.FloatField()
    #진행률 계산은 view에서 맡을 것

    class Meta:
        app_label = 'tracking'

# Create your models here.

# Create your models here.

# Create your models here.
