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
        struct_list.append([ADDRESS_LIST[dictionary['originIndex']].split(',')[0], 
        ADDRESS_LIST[dictionary['destinationIndex']].split(',')[0], 
        dictionary['distanceMeters']])
    return struct_list

def distance_dictionary(struct_list):
    """(List(Lists)-->Dictionary)
    Structure the data in a dictionary for quick look-up of distance between cities.
    {'ROSE WATER ESTATES':  [{'ACCESS STORAGE': 5041, 'WALMART': 150331, 'DOWN RIVER POOLS': 141913}]}"""
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

def get_coordinates(struct_list):
    """(List-->)
    Using a structured list that contains items of two cities and distance between those cities.
    calculate the coordinates for each city. First coordinates are (0,0) for first city and (0,y)
    second city of your choice. y = distance between first and second cities.
    struct_list=[[city1,city2,distance], [city1,..],..]"""
    first_city = struct_list[0][0]
    second_city = struct_list[0][1]
    y = struct_list[0][2]
    points = {first_city: (0,0), second_city: (0,y)}
    for item in struct_list[2:]:
        get_points(first_city, second_city, item)
    return None

if __name__ == "__main__":
    data = structure_data(refine_data(get_response(create_request_string(read_addresses()))))
    for every_list in data:
        print(every_list)
    dictionary = points_dictionary(data)
    for x in dictionary:
        print(x + ': ', dictionary[x])

            

















