import json
import math
import sys


def load_data(filepath):
    with open(filepath,'r') as opened_file:
        loaded_data = json.loads(opened_file.read())
    return loaded_data


def get_biggest_bar(bars_file):
    return max(
        bars_file['features'],
        key=lambda x: x['properties']['Attributes']['SeatsCount']
    )['properties']['Attributes']['Name']


def get_smallest_bar(bars_file):
    return min(
        bars_file['features'],
        key=lambda x: x['properties']['Attributes']['SeatsCount']
    )['properties']['Attributes']['Name']


def get_closest_bar(bars_file, longitude, latitude):
    return min(
        bars_file['features'],
        key= lambda x:
        abs(x['geometry']['coordinates'][0] - longitude)
        + abs(x['geometry']['coordinates'][1] - latitude)
    )['properties']['Attributes']['Name']


if __name__ == '__main__':
    user_longitude = int(input('Input your coordinates.\nLongitude: '))
    user_latitude = int(input('Latitude: '))
    try:
        bars_file = load_data(input('Input path to file: '))
        print('The largest bar: ', get_biggest_bar(bars_file))
        print('The smallest bar: ', get_smallest_bar(bars_file))
        print('The closest: ', get_closest_bar(bars_file, user_longitude, user_latitude))
    except FileNotFoundError:
        print('Path is incorrect. Try again.')