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


def calculate_paths4():
    df = pd.read_excel("C:/Users/캐리어/song/myagmo_final/agmo_myfarm/data_file/AGMO_Dataset4_output.xlsx")

    path_data1 = df.iloc[:, [4,5]]
    roll_data = df.iloc[:,8].values
    pitch_data = df.iloc[:,9].values
    #print(path_data1)

    coord = np.array(path_data1)
    #print(coord)

    agmo_data = convert_coords(coord)
    length = len(agmo_data)

    agmo_data_edit = agmo_data[:length//2]
    edit_length = len(agmo_data_edit)

    print(agmo_data_edit[:10])
    print(len(agmo_data_edit))

    mid_index = edit_length // 2
    traveled_path_data = agmo_data_edit[:1].copy()
    expected_path_data = agmo_data_edit[1:].copy()

    roll_data_past = roll_data[:1].copy()
    roll_data_future = roll_data[1:].copy()

    pitch_data_past = pitch_data[:1].copy()
    pitch_data_future = pitch_data[1:].copy()

    return traveled_path_data, expected_path_data, roll_data_past, roll_data_future, pitch_data_past, pitch_data_future

