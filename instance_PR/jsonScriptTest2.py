import json

def convert_to_text(input_file, output_file):
    with open(input_file, 'r') as file:
        data = json.load(file)
    
    trips = data['cars']
    trip_id = 1256 # Starting trip ID
    
    with open(output_file, 'w') as file:
        for trip in trips:
            trip_id += 1
            trip_data = f'<trip id="veh{trip_id}" type="long_vehicle" depart="0" departLane="best" departSpeed="4.47" from="{trip["path"][0]}" to="{trip["path"][-1]}">\n'
            file.write(trip_data)
            for edge in trip['path'][1:]:  # Start from the second element
                stop_data = f'   <stop edge="{edge}" endPos="5" duration="0"/>\n'
                file.write(stop_data)
            file.write('</trip>\n')

# Example usage
input_file = 'outputPR_long_vehicle.json'
output_file = 'outputFinal_long_vehicle.txt'
convert_to_text(input_file, output_file)
