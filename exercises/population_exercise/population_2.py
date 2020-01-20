# -*- coding: utf-8 -*-

# Get the top 10 countries with the largest population
# given by the function form population_1 and the helper
# and http://d6wn6bmjj722w.population.io/#!/population/determineTotalPopulationTodayAndTomorrow
# Use the python "requests" Library

import requests
import pygal
from population_exercise import population_1
from population_exercise.helper import get_the_top_n

countries_list = population_1.get_clean_country_list()


# Visualization functions
def print_visual_dots(title, print_list):
    """Prints the given list in dot style

    Keyword arguments:
    print_list -- the list which has to be printed
    """


    # Implementation...
    # ...
    # ...
    # ...


def print_2d_list(print_list):
    """Prints the given 2d list slightly formatted

    Keyword arguments:
    print_list -- the list which has to be printed

    Example:
        China - 1401026603
        India - 1382038624
    """


    # Implementation...
    # ...
    # ...
    # ...



# General sourcecode
list_to_sort = []
# containing sublists [['Guinea-Bissau', 1693398], ['Switzerland', 8211700]...]

# iterating over countries and determine the population numbers
for country in countries_list:
    print("Processing: " + country)
    population = requests.get(
        "https://d6wn6bmjj722w.population.io/1.0/population/{}/today-and-tomorrow/".format(country))

    #population = requests.get("http://api.population.io:80/1.0/population/" + country + "/today-and-tomorrow/")
    total_population = population.json()["total_population"]

    country_list = [country, total_population[0]["population"]]
    list_to_sort.append(country_list)
print("**** End processing ****")
print()


# calling the sorting function
key = (lambda land: land[1])
top_list = get_the_top_n(list_to_sort, 10, key, True)

# calling the printing function
print_2d_list(top_list)
print()

# calling the visualization function
print_visual_dots('largest population (in mio)', top_list)
print()