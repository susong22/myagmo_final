from django.db import models
from django.db.models import CharField
from django.db.models import BooleanField
from django.db.models import TextField
from django.db.models import IntegerField
from django.db.models import FloatField
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from agmo_myfarm.users import models as user_model

#데이터의 생성시간 업데이트 시간을 기록한다
class TimeStampedModel(models.Model):
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True

class FarmField(models.Model):
    
    CROP = [
        ('Byeo','벼'),
        ('Oksusu','옥수수'),
    ]

    farm_field_user = models.ForeignKey(
        user_model.User, 
        null=True, 
        on_delete=models.CASCADE, 
        related_name='field_user')
    
    field_name = models.CharField(blank=True, max_length=255)
    # location = models. (이부분은 api로 맵을 따오거나, 좌표값으로 받아올것)
    crop = models.CharField(blank=True, choices=CROP , max_length=225)
    # soil_moisture = models.CharField(_("Name of User"), blank=True, max_length=255) 이부분도 적절한 포맷을 생각해볼 것
    class Meta:
        app_label = 'farm'


class Machine(TimeStampedModel):
    farm_machine_user = models.ForeignKey(
        user_model.User, 
        null=True, 
        on_delete=models.CASCADE, 
        related_name='machine_user')

    
    machine_name = models.CharField(blank=True, max_length=255)
    contents = models.TextField(blank=True)
    is_active = models.BooleanField(default=True)
    battery = models.IntegerField()
    class Meta:
        app_label = 'farm'

class Weather(TimeStampedModel):
     temperature = models.FloatField() #기상청에서 크롤링해서 올 경우 별도의 처리가 필요함
     humidity = models.FloatField() #기상청에서 크롤링해서 올 경우 별도의 처리가 필요함
     wind_speed = models.FloatField() #기상청에서 크롤링해서 올 경우 별도의 처리가 필요함
     
     class Meta:
        app_label = 'farm'

# Create your models here.
# Create your models here.
