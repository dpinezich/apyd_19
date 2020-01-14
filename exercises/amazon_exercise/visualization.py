import matplotlib
import pygal
from wordcloud import WordCloud

matplotlib.use('TKAgg')
import matplotlib.pyplot as pyplot


def create_wordcloud(processed_text, filename):
    """
     Create a wordcloud from the input text
     Documentation about wordcloud: https://github.com/amueller/word_cloud
    :param processed_text:
    :param filename:
    :return:
    """
    pyplot.clf()

    # Implementation...
    # ...
    # ...
    # ...

    pyplot.savefig(filename)


def create_review_length_boxplot(reviews, filename):
    """
     Create a graph that shows a boxplot visualizes the review length for each score (1-star, 2-star, 3-star, 4-star, 5-star)
     Documentation about boxplot charts: http://www.pygal.org/en/latest/documentation/types/box.html
    :param reviews: list with review dictionaries
    :param filename: name of the saved file
    :return:
    """
    one_star_review_lengths = []
    two_star_review_lengths = []
    three_star_review_lengths = []
    four_star_review_lengths = []
    five_star_review_lengths = []

    # for review in reviews:
    # ...
    # ...

    box_plot = pygal.Box(box_mode='tukey')

    # Implementation...
    # ...
    # ...
    # ...

    box_plot.render_to_file(filename)


def create_score_barchart(reviews, filename):
    """
     Create a barchart that shows the distribution of the scores, e.g. how many reviews received a 1-star score, a 2-star
     score, and so on.
     Documentation about barcharts: http://www.pygal.org/en/latest/documentation/types/bar.html
    :param reviews:
    :param filename:
    :return:
    """
    line_chart = pygal.Bar()

    # Implementation...
    # ...
    # ...
    # ...

    line_chart.render_to_file(filename)