from django.shortcuts import render
from .path import calculate_paths
from .path2 import calculate_paths2
from .path3 import calculate_paths3
from .path4 import calculate_paths4
import json
from django.http import JsonResponse
from farm.models import FarmField

#1번
def index(request):
    traveled_path_data, expected_path_data, roll_data_past, roll_data_future, pitch_data_past, pitch_data_future = calculate_paths()

    print("Here is roll request")
    traveled_path_json = json.dumps(traveled_path_data.tolist())
    expected_path_json = json.dumps(expected_path_data.tolist())
    roll_data_past_json = json.dumps(roll_data_past.tolist())
    roll_data_future_json = json.dumps(roll_data_future.tolist())
    pitch_data_past_json = json.dumps(pitch_data_past.tolist())
    pitch_data_future_json = json.dumps(pitch_data_future.tolist())
    farm_list = FarmField.objects.all()

    return render(request, 
                  'home/index.html', 
                  {'traveled_path_json': traveled_path_json, 
                   'expected_path_json': expected_path_json, 
                   'roll_data_past_json': roll_data_past_json,
                   'roll_data_future_json': roll_data_future_json,
                   'pitch_data_past_json': pitch_data_past_json,
                   'pitch_data_future_json': pitch_data_future_json,
                    'farm_list':farm_list,
                   }
                  )

#2번
def path2(request):
    traveled_path_data, expected_path_data, roll_data_past, roll_data_future, pitch_data_past, pitch_data_future = calculate_paths2()

    print("Here is roll request")
    expected_path_json = json.dumps(expected_path_data.tolist())
    response_data = {'result': expected_path_json,}

#    return render(request, 
#                  'home/index.html', 
#                  {'traveled_path_json': traveled_path_json, 
#                   'expected_path_json': expected_path_json, 
#                   'roll_data_past_json': roll_data_past_json,
#                   'roll_data_future_json': roll_data_future_json,
#                   'pitch_data_past_json': pitch_data_past_json,
#                   'pitch_data_future_json': pitch_data_future_json}
#                  )
    return JsonResponse(response_data)


#3번
def path3(request):
    traveled_path_data, expected_path_data, roll_data_past, roll_data_future, pitch_data_past, pitch_data_future = calculate_paths3()


    expected_path_json = json.dumps(expected_path_data.tolist())
    response_data = {'result': expected_path_json,}

    return JsonResponse(response_data)



#4번
def path4(request):
    traveled_path_data, expected_path_data, roll_data_past, roll_data_future, pitch_data_past, pitch_data_future = calculate_paths4()
    
    expected_path_json = json.dumps(expected_path_data.tolist())
    response_data = {'result': expected_path_json,}

    return JsonResponse(response_data)