# Use the pygal radar (see http://www.pygal.org/en/latest/documentation/types/radar.html) to plot:
#   - Relative Population (to the world),
#   - Life Expectancy for Women                     /100
#   - Life Expectancy of Men'                       /100
#   - Life ExExpectancy A of both women and men     /100
#   - Relative Population Growth
#
# Of the following countries:
#   - "Ghana", "Sudan", "Libya", "South Africa", "Sierra Leone", "Cabo Verde", "Tanzania" and "Angola"
#
# Get the data via http request from the population.io api.
# http://api.population.io:80/1.0/life-expectancy/total/" + sex + "/" + country + "/" + date + "/"
# and http://api.population.io:80/1.0/population/{COUNTRY}/today-and-tomorrow/
# Use the python "requests" Library
#
# Check the the life expectancy of the 1st of January 2015 for all countries
#
# When you are done, feel free to compare other countries from http://api.population.io/1.0/countries
# Try to improve the view of the relative population.

import pygal
import requests

def get_life_expectancy(sex, country, year):
    """Returns the life expectancy for the given arguments for children born on 2015-06-30.

    Keyword arguments:
    sex     -- female or male
    country -- the name of the country (defined by population.io)
    year    -- year of life expectancy
    """


    # Implementation...
    # ...
    # ...
    # ...


def get_average_life_expectancy(country, year):
    """Returns the average life expectancy for the given country.

    Keyword arguments:
    country -- the name of the country (defined by population.io)
    year    -- year of life expectancy
    """


    # Implementation...
    # ...
    # ...
    # ...



def get_current_relative_population_of(country):
    """ Returns the population relative to the world population

    :param country: country of interest
    :return: relative population of the given country
    """


    # Implementation...
    # ...
    # ...
    # ...



def get_relative_growth(country):
    """Returns current relative growth of a country (today vs. tomorrow).

    Keyword arguments:
    country -- the name of the country (defined by population.io)
    """


    # Implementation...
    # ...
    # ...
    # ...



def get_characteristic_country_numbers(country, year):
    """ returns the data for the radar plot (in this case for the 5 categories) for the given country

    :param country:
    :param year:
    :return:
    """


    # Implementation...
    # ...
    # ...
    # ...



def get_data_plot_lists(countries_list, year):
    """prepares the data structure containing the data which will be printed

    :param countries_list:
    :param year_list:
    :return: list with all the needed data
    """


    # Implementation...
    # ...
    # ...
    # ...



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


    # Implementation...
    # ...
    # ...
    # ...


# General sourcecode (already complete)
countries_list = ["Mexico", "Switzerland", "Norway", "Ghana", "United States", "Rep of Korea"]
#countries_list = ["Ghana", "Sudan", "Libya", "South Africa", "Sierra Leone", "Cabo Verde", "Tanzania"]

x_labels = ['Rel. Population', 'Life Ex. F', 'Life Ex. M', 'Life Ex. A', 'Rel. Pop. Growth']
plot_data_list = get_data_plot_lists(countries_list, 2015)

title = "Country Radar"

write_plot_to_browser(title, x_labels, plot_data_list)
