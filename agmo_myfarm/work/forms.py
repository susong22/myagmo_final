from django.contrib.auth import get_user_model, forms
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import forms as admin_forms

from django import forms as django_forms
from .models import Works

class WorkForm(django_forms.ModelForm):
    class Meta:
        model = Works
        fields=['work_name', 
                'work_fields',
                'machine_name',
                'crop',
                'start_date_year', 
                'start_date_month',
                'start_date_day',
                'end_date_year',
                'end_date_month',
                'end_date_day',
                'user_memo'
        ]


