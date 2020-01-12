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

# Implement here
add_empty_lines()


"""
 Part 2:
 Write the number of movies form the movies.csv into the output_file
"""

# Implement here
add_empty_lines()

"""
 Part 3:
 - Write all movies that begin with "Zero" into the ouput_file
 - Write the number of movies that begin with "Zero" into the output_file
"""

# Implement here
add_empty_lines()

"""
 Part 4:
 Write the average rating per movie and the average rating per vote into the output_file
"""

# Implement here
add_empty_lines()

"""
 Part 5:
 Sort the movies list by rating and store it into a sorted_movies list
"""

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
