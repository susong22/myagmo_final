from django.contrib.auth import get_user_model, forms
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import forms as admin_forms

from django import forms as django_forms
from .models import FarmField

class FarmForm(django_forms.ModelForm):
    class Meta:
        model = FarmField
        fields=['field_name', 
                'crop',
                'user_memo',
        ]

