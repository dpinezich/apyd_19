import csv

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

movie_reader = csv.reader(movies_file)
# skipping the first line (header file) of the csv
next(movie_reader)

for row in movie_reader:
    movie = {
        'title': row[1],
        'year': int(row[2]),
        'length': int(row[3]) if row[3].isdigit() else None,
        'budget': int(row[4]) if row[4].isdigit() else None,
        'rating': float(row[5]) if row[5].replace(".", "", 1).isdigit() else None,
        'votes': int(row[6]) if row[6].isdigit() else None
    }
    movies.append(movie)

movies_file.close()


add_empty_lines()

"""
 Part 2:
 Write the number of movies form the movies.csv into the output_file
"""

output_file.write('Number of movies: {}'.format(len(movies)))
add_empty_lines()

"""
 Part 3:
 - Write all movies that begin with "Zero" into the ouput_file
 - Write the number of movies that begin with "Zero" into the output_file
"""

zero_movie_counter = 0

for movie in movies:
    if movie['title'].startswith('Zero'):
        zero_movie_counter += 1

output_file.write('Movies starting with Zero: {}'.format(zero_movie_counter))

add_empty_lines()

"""
 Part 4:
 Write the average score of all movies and the average score of all votes into the output_file
"""

sum_rating = 0
sum_votes = 0
counter_rating = 0
counter_votes = 0
for movie in movies:
    if movie['rating'] is not None:
        sum_rating += movie['rating']
        counter_rating +=1

    if movie['votes'] is not None:
        sum_votes += movie['votes']
        counter_votes += 1

average_rating = sum_rating / counter_rating
average_votes = sum_votes / counter_votes

output_file.write('The average ratings are: {} and the average votes per movie are: {}'.format(
    average_rating, average_votes))

add_empty_lines()

"""
 Part 5:
 Sort the movies list by rating and store it into a sorted_movies list
"""

sorted_movies = sorted(movies, key=lambda movie: movie['rating'], reverse=True)

"""
 Part 6:
 Write the 10 best rated movies with more than 5000 votes into the output_file
"""
output_file.write('Best rated movies with more than 5000 votes:\n\n')

count_selected_movies = 0
for movie in sorted_movies:

    if movie['votes'] <= 5000:
        continue

    count_selected_movies += 1
    output_file.write("Title: {} rating: {}\n".format(movie['title'], movie['rating']))

    if count_selected_movies >= 10:
        break


add_empty_lines()

"""
 Part 7:
 Write the 10 best rated movies with a budget of less than 1,000,000 USD into the output_file
"""
output_file.write('Best rated movies with budget lower than 1,000,000 USD:\n\n')
count_selected_movies = 0
for movie in sorted_movies:

    if movie['budget'] is None or movie['budget'] >= 1000000:
        continue

    count_selected_movies += 1
    output_file.write("Title: {} rating: {} budget: {}\n".format(movie['title'], movie['rating'], movie['budget']))

    if count_selected_movies >= 10:
        break

add_empty_lines()

"""
 Part 8:
 Write the 10 best rated movies with a budget of less than 1,000,000 USD and more than 5000 votes into the output_file
"""
output_file.write('Best rated movies with budget lower than 1,000,000 USD and more than 5000 votes:\n\n')

count_selected_movies = 0
for movie in sorted_movies:

    if movie['budget'] is None or movie['budget'] >= 1000000 or movie['votes'] <= 5000:
        continue

    count_selected_movies += 1
    output_file.write("Title: {} rating: {} budget: {} \n".format(movie['title'], movie['rating'], movie['budget']))

    if count_selected_movies >= 10:
        break

output_file.close()