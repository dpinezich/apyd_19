# -*- coding: utf-8 -*-

# Get the correlation between the relative growth an life expectancy of the countries
# given the function from Sol_2_1
# and http://d6wn6bmjj722w.population.io/#!/life-expectancy/calculateTotalLifeExpectancy
# Use the python "requests" Library for the http requests

import requests
import numpy
import Sol_2_1

# Additional functions
def get_life_expectancy(sex, country):
    """Returns the life expectancy for the given arguments for children born on 2015-06-30.

    Keyword arguments:
    sex     -- female or male
    country -- the name of the country (defined by population.io)
    """
    date = "2015-06-30"
    data = requests.get("http://d6wn6bmjj722w.population.io/1.0/life-expectancy/total/{}/{}/{}/".format(sex, country, date))
    # data = requests.get("http://api.population.io:80/1.0/life-expectancy/total/" + sex + "/" + country + "/" + date + "/")

    return data.json()["total_life_expectancy"]


def get_average_life_expectancy(country):
    """Returns the average life expectancy for the given country.

    Keyword arguments:
    country -- the name of the country (defined by population.io)
    """
    return (get_life_expectancy("female", country) + get_life_expectancy("male", country)) / 2.


def get_relative_growth(country):
    """Returns current relative growth of a country (today vs. tomorrow).

    Keyword arguments:
    country -- the name of the country (defined by population.io)
    """

    population = requests.get("http://d6wn6bmjj722w.population.io/1.0/population/{}/today-and-tomorrow/".format(country))
    #population = requests.get("http://api.population.io:80/1.0/population/" + country + "/today-and-tomorrow/")
    total_population = population.json()["total_population"]

    return total_population[1]["population"]/float(total_population[0]["population"])


def get_correlation(list_a, list_b):
    """Returns the correlation between the two given lists

    Comment: Numpy is a library which support vector and matrix operation
    In other words you can perform operations on vectors which is more elegant than iterating over the list yourself

    Keyword arguments:
    list_a -- numeric values (same size as list_b)
    list_b -- numeric values
    """

    average_a = numpy.mean(list_a)
    average_b = numpy.mean(list_b)

    variance_a = average_a - list_a
    variance_b = average_b - list_b

    product_a_a = numpy.multiply(variance_a, variance_a)
    product_b_b = numpy.multiply(variance_b, variance_b)
    product_a_b = numpy.multiply(variance_a, variance_b)

    sum_product_a_a = numpy.sum(product_a_a)
    sum_product_b_b = numpy.sum(product_b_b)
    sum_product_a_b = numpy.sum(product_a_b)

    return float(sum_product_a_b) / numpy.sqrt(sum_product_a_a * sum_product_b_b)



# General sourcecode
list_life_expectancy = []
list_life_relative_growth = []
list_to_sort = []

# getting all the countries
countries_list = Sol_2_1.get_clean_country_list()

# iterating over countries and determine the life expectancies and relative growth
for country in countries_list:
    print("Processing: " + country)

    list_life_expectancy.append(get_average_life_expectancy(country))
    list_life_relative_growth.append(get_relative_growth(country))

print("**** End processing ****")
print()
# calling the function which calculates the correspondence between the two lists
print(get_correlation(list_life_expectancy, list_life_relative_growth))
