import json
import math
import sys


def load_data(filepath):
    with open(filepath,'r') as opened_file:
        loaded_data = json.loads(opened_file.read())
    return loaded_data

def get_biggest_bar(data):
    biggest_bar_dict = dict()
    for i in data['features']:
        biggest_bar_dict[i['properties']['Attributes']['SeatsCount']] = i['properties']['Attributes']['Name']
    return biggest_bar_dict.get(max(biggest_bar_dict)),max(biggest_bar_dict)


def get_smallest_bar(data):
    smallest_bar_dict = dict()
    for i in data['features']:
        smallest_bar_dict[i['properties']['Attributes']['SeatsCount']] = i['properties']['Attributes']['Name']
    return smallest_bar_dict.get(min(smallest_bar_dict)),min(smallest_bar_dict)


def get_closest_bar(data, longitude, latitude):
    closest_bar_dict = dict()
    for i in data['features']:
        closest_bar_dict[i['properties']['Attributes']['Name']] = i['geometry']['coordinates']
    closest_bar_dict2 = dict()
    for i in closest_bar_dict.keys():
        closest_bar_dict2[get_diff_coord(closest_bar_dict[i], [longitude, latitude])] = i
    return closest_bar_dict2[min(closest_bar_dict2.keys())]

def get_diff_coord(coordinates,coordinates2): return math.sqrt(((coordinates[0] - coordinates2[0])+(coordinates[1] - coordinates2[1]))**2)

if __name__ == '__main__':
    print('Что нужно найти? \n 1. Наименьший бар \n 2. Наибольший бар \n 3. Ближайший бар \n ')
    users_answer = int(input('Введите цифру от 1 до 3: \n'))
    if(users_answer == 1):
        print('Наименьший бар', get_smallest_bar(load_data(sys.argv[1])))
    elif(users_answer == 2):
        print('Наибольший бар', get_biggest_bar(load_data(sys.argv[1])))
    elif(users_answer == 3):
        users_coord = [float(coord) for coord in input("Введите ваши координаты через запятую: \n").split(',')]
        print('Ближайший бар: ',get_closest_bar(load_data(sys.argv[1]),users_coord[0],users_coord[1]))
    else:
        print('Некорректный формат ответа')