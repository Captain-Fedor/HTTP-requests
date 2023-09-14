import requests
import json
from pprint import pprint


def get_the_smartest_superhero(superheros):
    base_url = 'https://akabab.github.io/superhero-api/api'
    response = requests.get(base_url + '/all.json')
    all_heroes_data = response.json()
    clever_heroes_dict = {}
    for hero in all_heroes_data:
        for id in superheros:
            if id == hero['id']:
                clever_heroes_dict[hero['name']] = hero['powerstats']['intelligence']
    the_smartest_superhero = max(clever_heroes_dict, key=clever_heroes_dict.get)
    return the_smartest_superhero

id_list = [1, 2, 3]
print(get_the_smartest_superhero(id_list))

