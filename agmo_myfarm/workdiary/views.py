from django.shortcuts import render
from .forms import WorkDiaryForm  # forms.py에서 정의한 폼 import

def my_view(request):
    form = WorkDiaryForm()
# Create your views here.
