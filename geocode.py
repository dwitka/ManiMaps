"""
**geocode** module produces longitude and latitude coordinates
from an address file.

**geocode** reads a standard text file where each line consists 
of an address, it builds an http request and sends it to google's 
servers.

make_geocode_list parses out longitude and latitude coordinates 
from the reponse and returns them in a list.

    [[longitude, latitude],[longitude, latitude],...]
"""

import requests

API_KEY = None

def read_addresses(a_file='ADDRESSES'):
    """(File-->List)
    Read addresses from text file.
    """
    file1 = open(a_file, 'r')
    lines = file1.readlines()
    file1.close()
    return lines

def create_request_string(address):
    """(List-->String)
    Create a cURL request string
    """
    url = 'https://maps.googleapis.com/maps/api/geocode/json?'
    address = 'address=' + address.replace(" ", "+")
    api_key = '&key=' + API_KEY
    return url + address + api_key

def get_response(request_string):
    """(String-->Response)
    Get a json reponse from google's servers.
    """
    response = requests.post(request_string)
    return response.json()

def make_geocode_list(lines):
    """(List-->List)
    Make a list of longitude and latitude coordinates.
    """
    geocode_list = []
    for line in lines:
        line = line.strip('\n')
        request_string = create_request_string(line)
        response = get_response(request_string)
        coordinates = get_coordinates(response)
        coordinates = get_list_coordinates(coordinates)
        geocode_list.append(coordinates)
    return geocode_list

def get_list_coordinates(coordinates):
    """(Tuple-->List)
    Convert tuple to a list.
    """
    return [coordinates['lat'], coordinates['lng']]   

def get_coordinates(response):
    """(Response-->Dictionary)
    Retrieve geocodes from json response.
    """
    geocodes = response['results'][0]['geometry']['location']
    return geocodes

if __name__ == "__main__":
    geo_list = make_geocode_list(read_addresses())
    print(geo_list)






