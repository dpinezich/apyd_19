# -*- coding: utf-8 -*-

# Use the pygal worldmap_chart
# (see http://www.pygal.org/en/latest/documentation/types/maps/pygal_maps_world.html
# and take the example "Minimum deaths by capital punishement (source: Amnesty International)" to plot
# all of the countries listed in the dictionary below (the common subset of population.io and pygal).
#
# Get the data via http request from the population.io api.
# http://api.population.io:80/1.0/life-expectancy/total/" + sex + "/" + country + "/" + date + "/"
# Use the 1st of January 2015 for all countries
#
#
# Use the python "requests" Library
#
# When you are done, feel free to compare other countries from http://api.population.io/1.0/countries

import pygal.maps.world
import requests

country_dict = {
    "Afghanistan":  "af",
    "Albania": "al",
    "Algeria": "dz",
    "Angola": "ao",
    "Argentina": "ar",
    "Armenia": "am",
    "Australia": "au",
    "Austria": "at",
    "Azerbaijan": "az",
    "Bahrain": "bh",
    "Bangladesh": "bd",
    "Belarus": "by",
    "Belgium": "be",
    "Belize": "bz",
    "Benin": "bj",
    "Bhutan": "bt",
    "Bolivia": "bo",
    "Bosnia and Herzegovina": "ba",
    "Botswana": "bw",
    "Brazil": "br",
    "Brunei Darussalam": "bn",
    "Bulgaria": "bg",
    "Burkina Faso": "bf",
    "Burundi": "bi",
    "Cambodia": "kh",
    "Cameroon": "cm",
    "Canada": "ca",
    "Cabo Verde": "cv",
    "Central African Republic": "cf",
    "Chad": "td",
    "Chile": "cl",
    "China": "cn",
    "Colombia": "co",
    "Congo": "cg",
    "Dem Rep of Congo": "cd",
    "Costa Rica": "cr",
    "Cote-d-Ivoire": "ci",
    "Croatia": "hr",
    "Cuba": "cu",
    "Cyprus": "cy",
    "Czech Republic": "cz",
    "Denmark": "dk",
    "Djibouti": "dj",
    "Dominican Republic": "do",
    "Ecuador": "ec",
    "Arab Rep of Egypt": "eg",
    "El Salvador": "sv",
    "Equatorial Guinea": "gq",
    "Eritrea": "er",
    "Estonia": "ee",
    "Ethiopia": "et",
    "Finland": "fi",
    "France": "fr",
    "French Guiana": "gf",
    "Gabon": "ga",
    "The Gambia": "gm",
    "Georgia": "ge",
    "Germany": "de",
    "Ghana": "gh",
    "Greece": "gr",
    "Guam": "gu",
    "Guatemala": "gt",
    "Guinea": "gn",
    "Guinea-Bissau": "gw",
    "Guyana": "gy",
    "Haiti": "ht",
    "Honduras": "hn",
    "Hong Kong SAR-China": "hk",
    "Hungary": "hu",
    "Iceland": "is",
    "India": "in",
    "Indonesia": "id",
    "Iraq": "iq",
    "Ireland": "ie",
    "Islamic Republic of Iran": "ir",
    "Israel": "il",
    "Italy": "it",
    "Jamaica": "jm",
    "Japan": "jp",
    "Jordan": "jo",
    "Kazakhstan": "kz",
    "Kenya": "ke",
    "Dem Peoples Rep of Korea": "kp",
    "Rep of Korea": "kr",
    "Kuwait": "kw",
    "Kyrgyz Republic": "kg",
    "Lao PDR": "la",
    "Latvia": "lv",
    "Lebanon": "lb",
    "Lesotho": "ls",
    "Liberia": "lr",
    "Libya": "ly",
    "Lithuania": "lt",
    "Luxembourg": "lu",
    "Macao SAR China": "mo",
    "Guadeloupe": "mk",
    "Madagascar": "mg",
    "Malawi": "mw",
    "Malaysia": "my",
    "Maldives": "mv",
    "Mali": "ml",
    "Malta": "mt",
    "Mauritania": "mr",
    "Mauritius": "mu",
    "Mayotte": "yt",
    "Mexico": "mx",
    "Moldova": "md",
    "Mongolia": "mn",
    "Montenegro": "me",
    "Morocco": "ma",
    "Mozambique": "mz",
    "Myanmar": "mm",
    "Namibia": "na",
    "Nepal": "np",
    "The Netherlands": "nl",
    "New Zealand": "nz",
    "Nicaragua": "ni",
    "Niger": "ne",
    "Nigeria": "ng",
    "Norway": "no",
    "Oman": "om",
    "Pakistan": "pk",
    "Panama": "pa",
    "Papua New Guinea": "pg",
    "Paraguay": "py",
    "Peru": "pe",
    "Philippines": "ph",
    "Poland": "pl",
    "Portugal": "pt",
    "Puerto Rico": "pr",
    "Reunion": "re",
    "Romania": "ro",
    "Russian Federation": "ru",
    "Rwanda": "rw",
    "Sao Tome and Principe": "st",
    "Saudi Arabia": "sa",
    "Senegal": "sn",
    "Serbia": "rs",
    "Seychelles": "sc",
    "Sierra Leone": "sl",
    "Singapore": "sg",
    "Slovak Republic": "sk",
    "Slovenia": "si",
    "Somalia": "so",
    "South Africa": "za",
    "Spain": "es",
    "Sri Lanka": "lk",
    "Sudan": "sd",
    "Suriname": "sr",
    "Swaziland": "sz",
    "Sweden": "se",
    "Switzerland": "ch",
    "Syrian Arab Rep": "sy",
    "Tajikistan": "tj",
    "Tanzania": "tz",
    "Thailand": "th",
    "Timor-Leste": "tl",
    "Togo": "tg",
    "Tunisia": "tn",
    "Turkey": "tr",
    "Turkmenistan": "tm",
    "Uganda": "ug",
    "Ukraine": "ua",
    "United Arab Emirates": "ae",
    "United Kingdom": "gb",
    "United States": "us",
    "Uruguay": "uy",
    "Uzbekistan": "uz",
    "RB-de-Venezuela": "ve",
    "Vietnam": "vn",
    "Western Sahara": "eh",
    "Rep of Yemen": "ye",
    "Zambia": "zm",
    "Zimbabwe": "zw"
}

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

def write_plot_to_browser(title, plot_data_dict, year):
    """
    :param title: Title of the chart. For example "Browser usage evolution (in %)"
    :param plot_data_dict: Dictionary as defined in http://www.pygal.org/en/latest/documentation/types/maps/pygal_maps_world.html
    :param year: The year of interest

    :return: picture in default web browser
    """


    # Implementation...
    # ...
    # ...
    # ...



# General sourcecode (already complete)
data_dict = {}

year = 2015

for country, country_short in country_dict.items():
    data_dict[country_short] = round(get_average_life_expectancy(country, year), 0)

write_plot_to_browser('World Wide Life Expectancy', data_dict, year)
