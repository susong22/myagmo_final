from django.db import models
from django.db.models import CharField
from django.db.models import BooleanField
from django.db.models import TextField
from django.db.models import IntegerField
from django.db.models import FloatField
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from agmo_myfarm.users import models as user_model
from django.contrib.gis.db import models

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
    location = models.JSONField(null=True)
    crop = models.CharField(blank=True, choices=CROP , max_length=225)
    # soil_moisture = models.CharField(_("Name of User"), blank=True, max_length=255) 이부분도 적절한 포맷을 생각해볼 것
    
    weather_date = models.CharField(null=True)
    weather_time = models.CharField(null=True)
    is_rain = models.FloatField(null=True)             # 강수 확률(POP)
    rain_sh = models.CharField(null=True)              # 강수 형태(PTY)
    temperature = models.FloatField(null=True)         # 1시간 기온(TMP)
    humidity = models.FloatField(null=True)            # 습 도(REH)
    wind_direction = models.CharField(null=True)       # 풍 향(VEC)
    wind_speed = models.FloatField(null=True)          # 풍 속(WSD)
    sky_sh = models.CharField(null=True)               # 하늘 상태(SKY)
    
    user_memo = models.TextField(blank=True, null=True)
    is_selected = models.BooleanField(default=False)
    

    class Meta:
        app_label = 'farm'



# Create your models here.
# Create your models here.
