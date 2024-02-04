from django.db import models
from farm import models as farm_model
from work import models as work_model
from tracking import models as tracking_model
from django.contrib.gis.db import models


#데이터의 생성시간 업데이트 시간을 기록한다
class TimeStampedModel(models.Model):
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True

class Home(TimeStampedModel):
    selected_date = models.DateField()

    home_tracking = models.ForeignKey(
        tracking_model.Tracking, 
        null=True, 
        on_delete=models.CASCADE, #외래키 갖는 유저 삭제시
        related_name='home_tracking_tracking'
        )
    #주행에 관련된 정보들을 tracking의 Tracking에서 받아온다
    #current_point, traveled_path

    home_work = models.ForeignKey(
        work_model.Works, 
        null=True, 
        on_delete=models.CASCADE, #외래키 갖는 유저 삭제시
        related_name='home_work_works'
        )
    #expected_path와 crop을 work의 Works에서 받아온다

    home_machines = models.ForeignKey(
        farm_model.Machine, 
        null=True, 
        on_delete=models.CASCADE, #외래키 갖는 유저 삭제시
        related_name='home_farm_machine'
        )
    #is_active, battery, machine_name을 farm의 Machine에서 받아온다

    home_weather = models.ForeignKey(
        farm_model.Weather, 
        null=True, 
        on_delete=models.CASCADE, #외래키 갖는 유저 삭제시
        related_name='hoem_farm_weather'
        )
    #weather을 farm의 Weather에서 받아온다

    home_farmfield = models.ForeignKey(
        farm_model.FarmField, 
        null=True, 
        on_delete=models.CASCADE, #외래키 갖는 유저 삭제시
        related_name='home_farm_farmfield'
        )
    #soil_moisture을 farm의 FarmField에서 받아온다

    mymemo = models.TextField(blank=True)


    class Meta:
        app_label = 'home'

# Create your models here.
