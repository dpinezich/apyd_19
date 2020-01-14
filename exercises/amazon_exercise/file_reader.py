def read_review_file(filename, max_reviews=-1):
    """
     This method reads an Amazon review file and stores each review entry into a list of entry dictionaries
    :param filename: path/name of review file
    :param max_reviews: (opitional) only process a given number of reviews
    :return:
    """
    reviews = []
    reviews_file = open(filename, 'r')
    entry = {}
    for line in reviews_file:
        line = line.strip()

        # Implementation...
        # ...
        # ...
        # ...

    print('Finished reading {} reviews'.format(len(reviews)))
    return reviews