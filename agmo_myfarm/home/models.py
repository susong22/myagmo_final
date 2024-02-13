from django.db import models
from farm import models as farm_model
from work import models as work_model
from tracking import models as tracking_model
from django.contrib.gis.db import models

class TimeStampedModel(models.Model):
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True

class Home(TimeStampedModel):
    selected_date = models.DateField(blank=True, null=True)

    home_work = models.ForeignKey(
        work_model.Works, 
        null=True, 
        on_delete=models.CASCADE,
        related_name='home_work_works'
        )
    #crop을 work의 Works에서 받아온다

    home_farmfield = models.ForeignKey(
        farm_model.FarmField, 
        null=True, 
        on_delete=models.CASCADE,
        related_name='home_farm_farmfield'
        )
    #soil_moisture, weather을 farm의 FarmField에서 받아온다

    mymemo = models.TextField(blank=True, null=True)

    class Meta:
        app_label = 'home'