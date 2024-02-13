import pandas as pd
import numpy as np
from pyproj import Transformer
import folium

def convert_coords(coord):
    transformer = Transformer.from_crs("epsg:5186", "epsg:4326")

    transformed_coords = []
    for x, y in coord:
        lon, lat = transformer.transform(x, y)
        transformed_coords.append([lon, lat])

    return np.array(transformed_coords)

def get_coord(file_path):
    df = pd.read_excel(file_path, sheet_name="자율주행 결과")

    path_data1 = df.iloc[:, [4,5]]
    print(path_data1)

    coord = np.array(path_data1)
    print(coord)

    result = convert_coords(coord)

    downsampled_data = result[::100]

    return downsampled_data

def calculate_paths():
    agmo_data = get_coord("C:/Users/82105/Downloads/AGMO1.xlsx")
    length = len(agmo_data)

    agmo_data_edit = agmo_data[:length//2]
    edit_length = len(agmo_data_edit)

    print(agmo_data_edit[:10])
    print(len(agmo_data_edit))

    mid_index = edit_length // 2
    traveled_path_data = agmo_data_edit[:mid_index].copy()
    expected_path_data = agmo_data_edit[mid_index:].copy()

    return traveled_path_data, expected_path_data



