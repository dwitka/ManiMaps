"""
**distance** module extracts distances between addresses.

**distance** reads a standard text file where each line consists of an 
address, it builds an http request and sends it to google's 
servers. The **distance** receives a json response which is then refined 
and structured.

Structures the data in a dictionary for quick look-up of distance between cities.
    {'ROSE WATER ESTATES':  [{'ACCESS STORAGE': 5041, 'WALMART': 150331, 'DOWN RIVER POOLS': 141913}]}
"""

import requests
import itertools

API_KEY = None
ADDRESS_LIST=[]

def read_addresses(a_file='ADDRESSES'):
    """(File-->List)
    Read addresses from text file.
    """
    file1 = open(a_file, 'r')
    lines = file1.readlines()
    file1.close()
    return lines

def create_request_string(lines):
    """(List-->JSON)
    Create json data for a cURL request
    """
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
    Build cURL request and send.
    """
    headers = {
        'Content-Type': 'application/json',
        'X-Goog-Api-Key': API_KEY,
        'X-Goog-FieldMask': 'originIndex,destinationIndex,distanceMeters',
    }
    response = requests.post('https://routes.googleapis.com/distanceMatrix/v2:computeRouteMatrix', headers=headers, json=json_data)
    return response.json()

def refine_data(response):
    """(List(Dictionaries)-->List(Dictionaries))
    Remove duplicates and negligables.
    """
    list1 = []
    for a,b in itertools.combinations(response, 2):
        if a['originIndex'] == b['destinationIndex'] and b['originIndex'] == a['destinationIndex']:
            list1.append(a)
    return list1

def structure_data(data):
    """(List(Dictionaries)-->List(Lists))
    Structure the data.
    """
    struct_list = []
    for dictionary in data:
        struct_list.append([ADDRESS_LIST[dictionary['originIndex']].split(',')[0], 
        ADDRESS_LIST[dictionary['destinationIndex']].split(',')[0], 
        dictionary['distanceMeters']])
    return struct_list

def distance_dictionary(struct_list):
    """(List(Lists)-->Dictionary)
    Structure the data in a dictionary for quick look-up of distance between cities.
    {'ROSE WATER ESTATES':  [{'ACCESS STORAGE': 5041, 'WALMART': 150331, 'DOWN RIVER POOLS': 141913}]}
    """
    points = {}
    for x in struct_list:
        if not x[0] in points.keys():
            points[x[0]] = [{x[1]: x[2]}]
        else:
            points[x[0]][0][x[1]] = x[2]     
        if not x[1] in points.keys():
            points[x[1]] = [{x[0]: x[2]}]
        else:
            points[x[1]][0][x[0]] = x[2]
    return points

def run_module():
    """(None-->Dictionary)
    Run the module from within another module or from the python shell.
    """
    addresses = read_addresses()
    request_string = create_request_string(addresses)
    response = get_response(request_string)
    r_data = refine_data(response)
    s_data = structure_data(r_data)
    dictionary = distance_dictionary(s_data)
    return dictionary

if __name__ == "__main__":
    print(run_module())

            

















