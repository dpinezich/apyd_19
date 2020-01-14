import csv
#import pandas as pd => somehow this is giving the error...
import os


os.chdir("C:/Users/bantel/switchdrive/WORK/2_Classes-Teaching/204-202001-Python_Data-analysis-and-Data-Visualization/apyd_19-master/apyd_19-master/exercises/imdb_exercise")
# os.listdir()

output_file = open('movies_information.txt', 'w')
movies_file = open('movies.csv', 'r')
movies = []


def add_empty_lines():
    output_file.write('\n\n######################\n\n')


"""
 Part 1:
 - Create a csv reader and go through each line in the movies.csv
 - For each movie, create a dictionary that contains the following keys:
   'title', 'year', 'length', 'budget', 'rating', 'votes'
 - Append each dictionary to the movies list
"""

# pandas import
# movies = pd.read_csv('movies.csv', header = 0, index_col=0, na_values = "NA")
# colnames = movies.columns

movie_reader = csv.reader(movies_file, delimiter = ",", )
next(movie_reader)  # skip first row

for row in movie_reader:
    movie = {"title": row[1],
             "year": int(row[2]),
             "length": int(row[3]) if row[3].isdigit() else None,
             "budget": int(row[4]) if row[4].isdigit() else None,
             "rating": float(row[5]) if row[5].replace(".", "", 1) else None, # replace the first "." with ""
             "votes": int(row[6]) if row[6].isdigit() else None}
    movies.append(movie)

movies_file.close() # added this since you had it yesterday

# Implement here
# for movie in movies:
#    output_file.write(str(movie))
#    output_file.write('\n')


add_empty_lines()


"""
 Part 2:
 Write the number of movies form the movies.csv into the output_file
"""

# Implement here
output_file.write("Number of movies: {}".format(len(movies)))
add_empty_lines()

"""
 Part 3:
 - Write all movies that begin with "Zero" into the ouput_file
 - Write the number of movies that begin with "Zero" into the output_file
"""

zero_movie_counter = 0

for movie in movies:
    if movie["title"].startswith("Zero"):
        #output_file.write(movie["title"]) not needed :)
        zero_movie_counter += 1

output_file.write('Movies starting with Zero: {}'.format(zero_movie_counter)) # that is needed

add_empty_lines()


"""
 Part 4:
 Write the average rating per movie and the average rating per vote into the output_file
"""

sum_rating = 0
sum_votes = 0

counter_rating = 0
counter_votes = 0

for movie in movies:
    if movie["rating"] is not None: # if we have a rating
        sum_rating += movie["rating"]
        counter_rating += 1

    if movie["votes"] is not None: # if we have a rating
        sum_votes += movie["votes"]
        counter_votes += 1

average_rating = sum_rating / counter_rating
average_votes = sum_votes / counter_votes

output_file.write("Avg ratings: {}, avg voters per movie: {}.".format(average_rating, average_votes))

# Implement here
add_empty_lines()

"""
 Part 5:
 Sort the movies list by rating and store it into a sorted_movies list
"""

sorted_movies = sorted(movies, key=lambda movie: movie["rating"], reverse=True)


# Implement here
add_empty_lines()

"""
 Part 6:
 Write the 10 best rated movies with more than 5000 votes into the output_file
"""

# Implement here
add_empty_lines()

"""
 Part 7:
 Write the 10 best rated movies with a budget of less than 1,000,000 USD into the output_file
"""

# Implement here
add_empty_lines()

"""
 Part 8:
 Write the 10 best rated movies with a budget of less than 1,000,000 USD and more than 5000 votes into the output_file
"""
output_file.write('Best rated movies with budget lower than 1,000,000 USD and more than 5000 votes:\n\n')

# Implement here
add_empty_lines()

output_file.close()
