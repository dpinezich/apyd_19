# -*- coding: utf-8 -*-

# Use the pygal line (see http://www.pygal.org/en/latest/documentation/types/line.html) to plot
# the life expectancy of "Ghana", "Sudan", "Libya", "South Africa", "Sierra Leone", "Cabo Verde", "Tanzania" and "Angola"
# From 1920 until 2010, with a step width of 10 years
#
# Get the data via http request from the population.io api.
# http://d6wn6bmjj722w.population.io/1.0/life-expectancy/total/" + sex + "/" + country + "/" + date + "/"
# Use the python "requests" Library
#
# Use and complete (if necessary) the prepared functions and feel free to add more functions yourself
#
# When you are done, feel free to compare other countries from http://d6wn6bmjj722w.population.io/1.0/countries

import pygal
import requests


def write_plot_to_browser(plot_title, x_labels_map, list_plot_data):
    """
    :param plot_title: Title of the chart. For example "Browser usage evolution (in %)"
    :param x_labels_map: For example map(str, range(2002, 2013))
    :param list_plot_data:
    list_plot_data = ['Firefox', [None, None,    0, 16.6,   25,   31, 36.4, 45.5, 46.3, 42.8, 37.1],
                     ['Chrome',  [None, None, None, None, None, None,    0,  3.9, 10.8, 23.8, 35.3],
                     ... ]
    :return: picture in default web browser
    """
    line_chart = pygal.Line()
    line_chart.title = plot_title
    line_chart.x_labels = x_labels_map

    for plot_data in list_plot_data:
        line_chart.add(plot_data[0], plot_data[1])

    line_chart.render_in_browser()


def get_life_expectancy(sex, country, year):
    """Returns the life expectancy for the given arguments for children born on 2015-06-30.

    Keyword arguments:
    sex     -- female or male
    country -- the name of the country (defined by population.io)
    year    -- year of life expectancy
    """

    # get use a html request to get the life expectancy from population.io
    # Request the 1st of January for the given year

    date = str(year) + '-01-01'
    data = requests.get('http://d6wn6bmjj722w.population.io/1.0/life-expectancy/total/{}/{}/{}/'.format(sex, country, date))

    return data.json()["total_life_expectancy"]


def get_average_life_expectancy(country, year):
    """Returns the average life expectancy for the given country.

    Keyword arguments:
    country -- the name of the country (defined by population.io)
    year    -- year of life expectancy
    """

    return (get_life_expectancy('female', country, year) + get_life_expectancy("male", country, year)) / 2




def get_average_life_expectancy_of_country_for_years(country, year_list):
    """Returns a list with the life expectancy for each year (given by the list) for the given country

    :param country: the country of interest
    :param year_list: list of the years which will be compared
    :return: returns list with the life expectancies
    """
    data = []

    for year in year_list:
        data.append(get_average_life_expectancy(country, year))

    return data



def get_data_plot_lists(countries_list, year_list):

    plot_data_list = []

    for country in countries_list:
        plot_data_list.append([country, get_average_life_expectancy_of_country_for_years(country, year_list)])


    return plot_data_list



# General sourcecode (already complete)
# countries_list = ["Mexico", "Switzerland", "Norway", "Ghana", "United States", "Rep of Korea"]
countries_list = ["Ghana", "Sudan", "Libya", "South Africa", "Sierra Leone", "Cabo Verde", "Tanzania", "Angola"]

year_list = range(1920, 2020, 10)

plot_data_list = get_data_plot_lists(countries_list, year_list)


title = "Life Expectancy over Decades"
x_labels = map(str, year_list)

write_plot_to_browser(title, x_labels, plot_data_list)
