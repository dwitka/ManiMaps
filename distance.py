"""
**app** module extracts distances between addresses.

**app** reads a standard text file where each line consists of an 
address, it builds an http request and sends it to google's 
servers. The **app** receives a json response which is then refined 
and structured.

Output returns list items that contain 2 addreses and the distance between them in meters:

    [[address, address, distance],[address, address, distance],...]
"""

import requests
import itertools

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
        'X-Goog-FieldMask': 'originIndex,destinationIndex,distanceMeters',
    }
    response = requests.post('https://routes.googleapis.com/distanceMatrix/v2:computeRouteMatrix', headers=headers, json=json_data)
    return response.json()

def refine_data(response):
    """(List(Dictionaries)-->List(Dictionaries))
    Remove duplicates and negligables."""
    list1 = []
    for a,b in itertools.combinations(response, 2):
        if a['originIndex'] == b['destinationIndex'] and b['originIndex'] == a['destinationIndex']:
            list1.append(a)
    return list1

def structure_data(data):
    """(List(Dictionaries)-->List(Lists))
    Structure the data."""
    struct_list = []
    for dictionary in data:
        struct_list.append([ADDRESS_LIST[dictionary['originIndex']], 
        ADDRESS_LIST[dictionary['destinationIndex']], 
        dictionary['distanceMeters']])
    return struct_list

if __name__ == "__main__":
    data = structure_data(refine_data(get_response(create_request_string(read_addresses()))))
    for item in data:
        print(item)

            

















