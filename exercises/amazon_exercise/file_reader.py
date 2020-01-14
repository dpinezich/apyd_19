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
        colon_pos = line.find(':')
        if colon_pos == -1:
            reviews.append(entry)
            entry = {}
            if len(reviews) >= max_reviews > 0:
                print('Finished reading {} reviews'.format(len(reviews)))
                return reviews
        else:
            entry_key = line[:colon_pos]
            entry_content = line[colon_pos + 2:]
            try:
                entry_content = float(entry_content)
            except ValueError:
                pass
            entry[entry_key] = entry_content


        # Implementation...
        # ...
        # ...
        # ...





    print('Finished reading {} reviews'.format(len(reviews)))
    return reviews