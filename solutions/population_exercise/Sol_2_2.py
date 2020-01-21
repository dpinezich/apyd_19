# -*- coding: utf-8 -*-

# Get the top 10 countries with the largest population
# given by the function form Sol_2_1 and the helper
# and http://api.population.io/#!/population/determineTotalPopulationTodayAndTomorrow
# Use the python "requests" Library

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
        print(' - '.join(item))

def print_visual_dots(title, print_list):
    """Prints the given list in dot style

    Keyword arguments:
    print_list -- the list which has to be printed
    """
    countries = []
    numbers = []

    for item in print_list:
        countries.append(item[0])
        numbers.append(int(item[1]) / 1000000)


    dot_chart = pygal.Dot(x_label_rotation=30)
    dot_chart.title = title
    dot_chart.x_labels = countries
    dot_chart.add('Countries', numbers)
    dot_chart.render_in_browser()

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

