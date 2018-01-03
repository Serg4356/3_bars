import json
import math
import sys


def load_data(filepath):
    with open(filepath,'r') as opened_file:
        loaded_data = json.loads(opened_file.read())
    return loaded_data


def create_bars_description_list(loaded_data):
    return loaded_data['features']


def get_biggest_bar(bars_description_list):
    return max(
        bars_description_list,
        key=lambda x: x['properties']['Attributes']['SeatsCount']
    )


def get_smallest_bar(bars_description_list):
    return min(
        bars_description_list,
        key=lambda x: x['properties']['Attributes']['SeatsCount']
    )


def calculate_coordinates(bar_longitude, bar_latitude, user_longitude, user_latitude):
    return abs(bar_longitude - user_longitude) + abs(bar_latitude - user_latitude)


def get_closest_bar(bars_description_list, longitude, latitude):
    return min(
        bars_description_list,
        key= lambda x:
        calculate_coordinates(
            x['geometry']['coordinates'][0],
            x['geometry']['coordinates'][1],
            longitude,
            latitude
        )
    )


if __name__ == '__main__':
    try:
        user_longitude = float(input('Input your coordinates.\nLongitude: '))
        user_latitude = float(input('Latitude: '))
        loaded_data = load_data(sys.argv[1])
        bars = create_bars_description_list(loaded_data)
        print('The largest bar: ',
              get_biggest_bar(
                  bars
              )['properties']['Attributes']['Name'])
        print('The smallest bar: ',
              get_smallest_bar(
                  bars
              )['properties']['Attributes']['Name'])
        print('The closest: ',
              get_closest_bar(
                  bars,
                  user_longitude,
                  user_latitude
              )['properties']['Attributes']['Name'])
    except FileNotFoundError:
        print('Path is incorrect. Try again.')
    except IndexError:
        print('Please enter path to file.')
    except ValueError:
        print('Type of coordinates is incorrect. Try again.')