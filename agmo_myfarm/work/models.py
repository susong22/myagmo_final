from django.db import models
from agmo_myfarm.users import models as user_model
from farm import models as farm_model
from django.contrib.gis.db import models


#데이터의 생성시간 업데이트 시간을 기록한다
class TimeStampedModel(models.Model):
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True

class Works(TimeStampedModel):
    work_name = models.CharField(blank=True, max_length=255)
    #start_date = models.DateField()
    #end_date = models.DateField()
    start_date_year = models.CharField(null=True)
    start_date_month = models.CharField(null=True)
    start_date_day = models.CharField(null=True)

    end_date_year = models.CharField(null=True)
    end_date_month = models.CharField(null=True)
    end_date_day = models.CharField(null=True)

    work_fields = models.ForeignKey(
        farm_model.FarmField, 
        null=True, 
        on_delete=models.CASCADE, #외래키 갖는 유저 삭제시
        related_name='work_farm_farmfield'
        )
    #경작지 위치를 fields table의 location에서 받아올 예정입니다
    
    machine_user = models.ForeignKey(
    user_model.User, 
    null=True, 
    on_delete=models.CASCADE, 
    related_name='machine_user')
    
    machine_name = models.CharField(blank=True, max_length=255)
    contents = models.TextField(blank=True)
    is_active = models.BooleanField(default=True)
    battery = models.IntegerField(null=True)

    start_point = models.PointField(null=True)
    end_point = models.PointField(null=True)
    #template에서 클릭 이벤트 생성->해당 좌표값 서버로 전송->전송된 JSON데이터에서 좌표값 추출->
    #모델에 저장(view에서 구현)
    #좌표값은 위경도값으로 저장
    # location = models. (이부분은 api로 맵을 따오거나, 좌표값으로 받아올것)
    expected_path = models.PointField(null=True)
    #시작점 끝점을 입력하면 예상 경로를 출력한다

    #crop = models.ForeignKey(
    #    farm_model.FarmField, 
    #    null=True, 
    #    on_delete=models.CASCADE, #외래키 갖는 유저 삭제시
    #    related_name='farm_farm_crop'
    #    )
    crop = models.CharField(null=True)
    user_memo = models.TextField(blank=True)
    estimated_hours = models.IntegerField(default=0, help_text='예상 작업시간: 시간')
    estimated_minutes = models.IntegerField(default=0, help_text='예상 작업시간: 분')

    def __str__(self):
        return f'{self.estimated_hours}시간 {self.estimated_minutes}분'
    
    class Meta:
        app_label = 'work'

# Create your models here.
