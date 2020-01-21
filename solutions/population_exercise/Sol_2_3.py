# -*- coding: utf-8 -*-

# Get the top 10 countries with the larges relative population growth
# given by the function from Sol_2_1 and the helper
# and http://d6wn6bmjj722w.population.io/#!/population/determineTotalPopulationTodayAndTomorrow
# Use the python "requests" Library for the http requests

import requests
import pygal
import Sol_2_1
from helper import get_the_top_n

countries_list = Sol_2_1.get_clean_country_list()

def get_relative_growth(country):
    """Returns current relative growth of a country (today vs. tomorrow).

    Keyword arguments:
    country -- the name of the country (defined by population.io)
    """

    population = requests.get("http://d6wn6bmjj722w.population.io/1.0/population/{}/today-and-tomorrow/".format(country))
    #population = requests.get("http://api.population.io:80/1.0/population/" + country + "/today-and-tomorrow/")
    total_population = population.json()["total_population"]

    return total_population[1]["population"]/float(total_population[0]["population"])

# Visualization functions
def print_2d_list(print_list):
    """Prints the given 2d list slightly formatted

    Keyword arguments:
    print_list -- the list which has to be printed
    """
    for item in print_list:
        # this command
        print(' - '.join(item))


def print_visual_bar(title, print_list):
    """Prints the given list in horizontal bar style

    Keyword arguments:
    print_list -- the list which has to be printed
    """

    line_chart = pygal.HorizontalBar()
    line_chart.title = title
    for item in print_list:
        line_chart.add(item[0], [float(item[1]) - 1])

    line_chart.render_in_browser()


# General sourcecode
list_to_sort = []
# containing sublists [['Guinea-Bissau', 1693398], ['Switzerland', 8211700]...]

# iterating over countries and determine the population numbers
for country in countries_list:
    print("Processing: " + country)

    # Calculating relative population growth from today to tomorrow
    country_list = [country, get_relative_growth(country)]
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
print_visual_bar('largest growth', top_list)
print()

