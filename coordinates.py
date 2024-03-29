import math
from sympy import solve, Symbol, simplify
from sympy.abc import x,y

distances = {}

def distance_dictionary(struct_list):
    """(List(Lists)-->Dictionary)
    Structure the data in a dictionary for quick look-up of distance between cities.
    {'ROSE WATER ESTATES':  [{'ACCESS STORAGE': 5041, 'WALMART': 150331, 'DOWN RIVER POOLS': 141913}]}"""
    for x in struct_list:
        if not x[0] in distances.keys():
            distances[x[0]] = [{x[1]: x[2]}]
        else:
            distances[x[0]][0][x[1]] = x[2]     
        if not x[1] in distances.keys():
            distances[x[1]] = [{x[0]: x[2]}]
        else:
            distances[x[1]][0][x[0]] = x[2]
    return distances

def get_coordinates(struct_list):
    """(List-->)
    Using a structured list that contains items of two cities and distance between those cities.
    calculate the coordinates for each city. First coordinates are (0,0) for first city and (0,y)
    second city of your choice. y = distance between first and second cities.
    struct_list=[[city1,city2,distance], [city1,..],..]"""
    new_list = []
    for address in ADDRESS_LIST:
        new_list.append(address.split(',')[0])
    location1 = new_list[0]
    location2 = new_list[1]
    y = distances[location1][0][location2]/1000
    points_dictionary = {location1: (0,0), location2: (0,y)}
    for location in new_list[2:]:
        points = get_points(location1, location2, location)
        points_dictionary[location] = points
    return points_dictionary

def get_points(city1, city2, city3):
    """(String,String,String-->Tuple)
    Three locations are entered. For two coordinates are known and for the last location
    the coordinates are calculated. Return a tuple of coordinates."""
    d1 = distances[city3][0][city1]
    d2 = distances[city2][0][city1]
    d3 = distances[city3][0][city2]
    x = Symbol("x", positive=True)
    y = Symbol("y", positive=True)
    eqs = (x**2 + y**2 - d1**2, x**2 + (y - d2)**2 - d3**2)
    solutions = solve(eqs,x,y)
    value1 = str(solutions[0][0])
    value2 = str(solutions[0][1])
    value1 = value1.replace("sqrt", "math.sqrt")
    value2 = value2.replace("sqrt", "math.sqrt")
    
    solutions = ( eval(value1)/1000, eval(value2)/1000 )
    return solutions
