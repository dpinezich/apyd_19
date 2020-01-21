# -*- coding: utf-8 -*-

# Get the top 10 countries with the highest life expectancy (average woman/man) for kids born on 2015-06-30
# given the function from Sol_2_1
# and http://d6wn6bmjj722w.population.io/#!/life-expectancy/calculateTotalLifeExpectancy
# Use the python "requests" Library for the http requests

import requests
import pygal
import Sol_2_1
from helper import get_the_top_n

countries_list = Sol_2_1.get_clean_country_list()

# Visualization functions
def print_2d_list(print_list):
    """Prints the given 2d list slightly formatted

    Keyword arguments:
    print_list -- the list which has to be printed
    """

    for item in print_list:
        # this command
        print(' - '.join(item))

def print_visual_gauge(title, print_list):
    """Prints the given list in gauge style

    Keyword arguments:
    print_list -- the list which has to be printed
    """

    gauge = pygal.SolidGauge(
        half_pie=True, inner_radius=0.70,
        style=pygal.style.styles['default'](value_font_size=10))

    for item in print_list:
        gauge.add(item[0], [{'value': float(item[1]), 'max_value': 100}])

    gauge.render_in_browser()


# Additional functions
def get_life_expectancy(sex, country):
    """Returns the life expectancy for the given arguments for children born on 2015-06-30.

    Keyword arguments:
    sex     -- female or male
    country -- the name of the country (defined by population.io)
    """
    date = "2015-06-30"
    data = requests.get("http://d6wn6bmjj722w.population.io/1.0/life-expectancy/total/" + sex + "/" + country + "/" + date + "/")

    return data.json()["total_life_expectancy"]


def get_average_life_expectancy(country):
    """Returns the average life expectancy for the given country.

    Keyword arguments:
    country -- the name of the country (defined by population.io)
    """
    return (get_life_expectancy("female", country) + get_life_expectancy("male", country)) / 2.



# General sourcecode
list_to_sort = []
# containing sublists [['Afghanistan', 77.3009302725], ['Switzerland', 92.7132960888]...]

# iterating over countries and determine the life expectancies
for country in countries_list:
    print("Processing: " + country)

    average_life_expectancy = get_average_life_expectancy(country)

    # Calculating relative population growth from today to tomorrow
    country_list = [country, average_life_expectancy]
    list_to_sort.append(country_list)
print("**** End processing ****")
print()

# calling the sorting function
key = (lambda land: land[1])
top_list = get_the_top_n(list_to_sort, 20, key, False)

# calling the printing function
print_2d_list(top_list)
print()

# calling the visualization function
print_visual_gauge('life expectancy', top_list)
print()