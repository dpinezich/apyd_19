import statistics


def print_stats(data, description):
    print('The mean {} is: {}'.format(description, statistics.mean(data)))
    print('The median {} is: {}'.format(description, statistics.median(data)))
    print('The mode of {} is: {}'.format(description, statistics.mode(data)))
    print('The standard deviation of {} is: {}'.format(description, statistics.stdev(data)))
    print('\n\n')


def print_review_statistics(reviews):
    """
     Print the mean, media, mode and standard deviation of the review scores and review text lengths
    """
    scores = []
    review_lengths = []

    for review in reviews:
        scores.append(review['review/score'])
        review_lengths.append(len(review['review/text'].split(' ')))

    print_stats(scores, 'score')
    print_stats(review_lengths, 'review length')








