"""
**geocode** module produces longitude and latitude coordinates
from an address file.

**geocode** reads a standard text file where each line consists 
of an address, it builds an http request and sends it to google's 
servers.

make_geocode_list parses out longitude and latitude coordinates 
from the response and returns them in a list.

    [[longitude, latitude],[longitude, latitude],...]
"""

import requests


def read_addresses(a_file='./data/ADDRESSES') -> list:
    """ Read addresses from text file. """
    file1 = open(a_file, 'r')
    lines = file1.readlines()
    file1.close()
    return lines


def create_request_string(address: list) -> str:
    """ Create a cURL request string """
    url = 'https://maps.googleapis.com/maps/api/geocode/json?'
    address = 'address=' + address.replace(" ", "+")
    api_key = '&key=' + API_KEY
    return url + address + api_key


def get_response(request_string: str) -> "response":
    """ Get a json response from google's servers. """
    response = requests.post(request_string)
    return response.json()


def geocodes(line: str) -> list:
    """ longitude and latitude set """
    line.strip('\n')
    request_string = create_request_string(line)
    response = get_response(request_string)
    coordinates = get_coordinates(response)
    coordinates = get_list_coordinates(coordinates)
    return coordinates


def get_list_coordinates(coordinates: tuple) -> list:
    """ Convert tuple to a list. """
    return [coordinates['lat'], coordinates['lng']]   


def get_coordinates(response: "response") -> dict:
    """ Retrieve geocodes from json response. """
    geocodes = response['results'][0]['geometry']['location']
    return geocodes


def run_module() -> list:
    """ Run the module from within another module or from the python shell. """
    lines = read_addresses()
    return [ geocodes(line) for line in lines ]

if __name__ == "__main__":
    print(run_module())






