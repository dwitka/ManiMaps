import requests
import itertools
import numpy as np

API_KEY = None
ADDRESS_LIST=[]

def read_addresses(a_file='ADDRESSES'):
    """(File-->List)
    Read addresses from text file."""
    file1 = open(a_file, 'r')
    lines = file1.readlines()
    file1.close()
    return lines

def create_request_string(lines):
    """(List-->JSON)
    Create json data for a cURL request"""
    json_data = {'origins': [], 'destinations': [],'travelMode': 'DRIVE'}
    for line in lines:
        line = line.strip('\n')
        ADDRESS_LIST.append(line)
        address = {'waypoint': {'address': line}}
        json_data['origins'].append(address)
        json_data['destinations'].append(address)
    return json_data

def get_response(json_data):
    """(JSON-->Response)
    Build cURL request and send."""
    headers = {
        'Content-Type': 'application/json',
        'X-Goog-Api-Key': API_KEY,
        'X-Goog-FieldMask': 'originIndex,destinationIndex,duration,distanceMeters',
    }
    response = requests.post('https://routes.googleapis.com/distanceMatrix/v2:computeRouteMatrix', headers=headers, json=json_data)
    return response.json()

def durations_matrix(response):
    num = len(ADDRESS_LIST)
    durations_list = []
    for x in range(num):
        durations_list.append([x for x in range(num)])
    for dictionary in response:
        durations_list[dictionary['originIndex']][dictionary['destinationIndex']] = int(dictionary['duration'].strip('s'))
    return durations_list

if __name__ == "__main__":
    lines = read_addresses()
    json_data = create_request_string(lines)
    response = get_response(json_data)
    matrix = durations_matrix(response)
    matrix = np.matrix(matrix)
    print(matrix)

