import requests
import urllib.request
from django.shortcuts import render
from django.utils.translation import gettext_lazy as _

def add_farmfield(request):
    return render(request, 'farm/add_farmfield.html')