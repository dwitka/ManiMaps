"""
**durations** module extracts duration times between addresses.

**durations** reads a standard text file where each line consists of an 
address, it builds an http request and sends it to google's 
servers.

**durations** returns matrix of duration time in seconds.
"""

import requests
import numpy as np


class Addresses:
    """ object that puts together a list of addresses """
    def __init__(self, data = []):
        self.data = data

    def add_item(self, item):
        self.data.append(item)

    def get_length(self):
        return self.data.__len__()


def read_addresses(a_file='./data/ADDRESSES') -> list:
    """ read addresses from text file """
    file1 = open(a_file, 'r')
    lines = file1.readlines()
    file1.close()
    return lines


def create_request_string(lines: list) -> "json_data":
    """ create json data for a cURL request """
    json_data = {'origins': [], 'destinations': [],'travelMode': 'DRIVE'}
    for line in lines:
        line = line.strip('\n')
        addresses.add_item(line)
        address = {'waypoint': {'address': line}}
        json_data['origins'].append(address)
        json_data['destinations'].append(address)
    return json_data


def get_response(json_data: "json_data") -> "response":
    """ build cURL request and send """
    headers = {
        'Content-Type': 'application/json',
        'X-Goog-Api-Key': API_KEY,
        'X-Goog-FieldMask': 'originIndex,destinationIndex,duration,distanceMeters',
    }
    response = requests.post('https://routes.googleapis.com/distanceMatrix/v2:computeRouteMatrix', headers=headers, json=json_data)
    return response.json()


def durations_matrix(response: "response") -> "matrix":
    """ returns an asymmetric durations matrix """
    num = addresses.get_length()
    matrix = []
    for x in range(num):
        matrix.append([x for x in range(num)])
    for dictionary in response:
        matrix[dictionary['originIndex']][dictionary['destinationIndex']] = int(dictionary['duration'].strip('s'))
    return np.matrix(matrix)


def run() -> "matrix":
    """ run the module from within another module or from the python shell """
    lines = read_addresses()
    json_data = create_request_string(lines)
    response = get_response(json_data)
    matrix = durations_matrix(response)
    return matrix


if __name__ == "__main__":
    addresses = Addresses()
    print(run())

