# -*- coding: utf-8 -*-

# Get the top 10 countries with the highest life expectancy (average woman/man) for kids born on 2015-06-30
# given by the http://d6wn6bmjj722w.population.io//#!/countries
# and http://d6wn6bmjj722w.population.io/#!/life-expectancy/calculateTotalLifeExpectancy
# Use the python "requests" Library for the http requests

import requests
from population_exercise import population_1
from population_exercise.helper import get_the_top_n

countries_list = population_1.get_clean_country_list()

# Visualization functions
def print_2d_list(print_list):
    """Prints the given 2d list slightly formatted

    Keyword arguments:
    print_list -- the list which has to be printed
    """

    # Implementation...
    # ...
    # ...
    # ...


def print_visual_gauge(title, print_list):
    """Prints the given list in gauge style

    Keyword arguments:
    print_list -- the list which has to be printed
    """

    # Implementation...
    # ...
    # ...
    # ...


# Additional functions
def get_life_expectancy(sex, country):
    """Returns the life expectancy for the given arguments for children born on 2015-06-30.

    Keyword arguments:
    sex     -- female or male
    country -- the name of the country (defined by population.io)
    """

    # Implementation...
    # ...
    # ...
    # ...


def get_average_life_expectancy(country):
    """Returns the average life expectancy for the given country.

    Keyword arguments:
    country -- the name of the country (defined by population.io)
    """

    # Implementation...
    # ...
    # ...
    # ...


# General sourcecode
list_to_sort = []

# Implementation...
# ...
# ...
# ...
