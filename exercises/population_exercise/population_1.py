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

    # Implementation...
    # ...
    # ...
    # ...



def run_exercise():
    print("There are {} countries fetched in total".format(len(countries_list)))
    clean_country_list = get_clean_country_list()
    print(clean_country_list)
    print("There are " + str(len(countries_list)) + " countries available in the population.io")


if __name__ == '__main__':
    run_exercise()