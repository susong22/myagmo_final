from django.shortcuts import render
from .path import calculate_paths
import json

def index(request):
    traveled_path_data, expected_path_data = calculate_paths()

    traveled_path_json = json.dumps(traveled_path_data.tolist())
    expected_path_json = json.dumps(expected_path_data.tolist())

    return render(request, 
                  'home/index.html', 
                  {'traveled_path_json': traveled_path_json, 'expected_path_json': expected_path_json}
                  )