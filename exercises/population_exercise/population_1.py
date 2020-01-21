# -*- coding: utf-8 -*-

import os.path
import pickle
import requests

# fetches all countries from population.io
countries = requests.get("https://d6wn6bmjj722w.population.io/1.0/countries")
countries_list = countries.json()["countries"]


def get_clean_country_list():
    """
    We need to clean the countries list from entries like "Least developed countries"
    and save them to a pickle file and include life expectancy
    """
    pickle_file = 'all_countries_list.pkl'

    if os.path.isfile(pickle_file):
        print('Pickle file was loaded')
        clean_country_list = pickle.load(open(pickle_file, 'rb'))
        return clean_country_list
    else:
        print('No pickle file available')

    clean_country_list = []
    black_list_country = [
        'Less developed regions',
        'Less developed regions, excluding China',
        'Less developed regions, excluding least developed countries',
        'More developed regions',
        'Other non-specified areas',
        'World',
        'Least developed countries'
    ]

    for country in countries_list:
        if country in black_list_country:
            continue
        response = requests.get('https://d6wn6bmjj722w.population.io/1.0/life-expectancy/remaining/male/{}/2001-05-11/49y2m'.format(country))

        if response.status_code == 200:
            clean_country_list.append(country)

    pickle.dump(clean_country_list, open(pickle_file, 'wb'))
    return clean_country_list


def run_exercise():
    print("There are {} countries fetched in total".format(len(countries_list)))
    clean_country_list = get_clean_country_list()
    print(clean_country_list)
    print("There are " + str(len(clean_country_list)) + " countries available in the population.io")


if __name__ == '__main__':
    run_exercise()