"""
https://maps.googleapis.com/maps/api/directions/json?origin=Boston,MA&destination=Concord,\
MA&waypoints=Charlestown,MA|via:Lexington,MA&units=imperial&key=API_KEY


coordinates for destination in json response

    data['routes'][0]['legs'][0]['end_location']


coordinates for origin in json response

    data['routes'][0]['legs'][0]['start_location']


address of destination in json response

    data['routes'][0]['legs'][0]['end_address']


address of origin in json response

    data['routes'][0]['legs'][0]['start_address']


steps is a list that contains all latitude and longitude coordinates for the steps in between
origin and destination and including origin and destination.

    data['routes'][0]['legs'][0]['steps']


"""


import requests

API_KEY = None


def read_addresses(a_file='DIRECTIONS'):
    """(File-->List)
    Read addresses from text file.
    """
    file1 = open(a_file, 'r')
    lines = file1.readlines()
    file1.close()
    return lines


def create_request_string(origin,destination):
    """(List-->String)
    Create a cURL request string
    """
    url = 'https://maps.googleapis.com/maps/api/directions/json?'
    origin = 'origin=' + origin.replace(" ", "+")
    destination = "&destination=" + destination.replace(" ", "+")
    api_key = '&key=' + API_KEY
    return url + origin + destination + api_key


def get_response(request_string):
    """(String-->Response)
    Get a json response from google's servers.
    """
    response = requests.post(request_string)
    return response.json()


def get_geocodes(response):
    """(Response-->List of Lists)
    Returns the origin/destination coordinates, addresses of origin/destination, and
    coordinates for the points in between.
    """
    coordinates = []
    names = []
    directions = []
    
    start_location = response['routes'][0]['legs'][0]['start_location']
    coordinates.append([start_location['lat'], start_location['lng']])

    end_location = response['routes'][0]['legs'][0]['end_location']
    coordinates.append([end_location['lat'], end_location['lng']])

    origin = response['routes'][0]['legs'][0]['start_address']
    destination = response['routes'][0]['legs'][0]['end_address']
    names.append(origin)
    names.append(destination)
    
    for geocode in response['routes'][0]['legs'][0]['steps']:
        directions.append([geocode['start_location']['lat'], geocode['start_location']['lng']])
        directions.append([geocode['end_location']['lat'], geocode['end_location']['lng']])

    return (coordinates, names, directions)


def run():
    """
    RUN MODULE
    """
    addresses = read_addresses()
    request_string = create_request_string(addresses[0], addresses[1])
    response = get_response(request_string)
    geocodes = get_geocodes(response)
    return geocodes

if __name__ == "__main__":
    run()

