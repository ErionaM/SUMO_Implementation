import json
import pandas as pd

def create_street_sumo_mapping(excel_file):
    df = pd.read_excel(excel_file)
    street_sumo_mapping = dict(zip(df['street_name'], df['SUMO_name'].astype(str)))  
    return street_sumo_mapping


def map_street_to_sumo_id(street_name, street_sumo_mapping):
    return street_sumo_mapping.get(street_name, None)

def process_path_list(path_list, street_sumo_mapping):
    return [map_street_to_sumo_id(street, street_sumo_mapping) for street in path_list]

def convert_street_to_sumo(json_file, street_sumo_mapping):
    with open(json_file, 'r') as file:
        data = json.load(file)
    
    for car in data['cars']:
        car['path'] = process_path_list(car['path'], street_sumo_mapping)
    
    return data

def write_json(data, output_file):
    with open(output_file, 'w') as file:
        json.dump(data, file, indent=4)

excel_file = 'test_2.xlsx'  
json_file = 'instance_fk_long_vehicle.json'
output_file = 'outputFK_long_vehicle.json'

street_sumo_mapping = create_street_sumo_mapping(excel_file)
converted_data = convert_street_to_sumo(json_file, street_sumo_mapping)
write_json(converted_data, output_file)
