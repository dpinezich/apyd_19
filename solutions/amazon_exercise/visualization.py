import matplotlib
import pygal
from wordcloud import WordCloud

matplotlib.use('TKAgg')
import matplotlib.pyplot as pyplot


def create_wordcloud(word_list, filename):
    """
     Saves image of a wordcloud
     Documentation: https://github.com/amueller/word_cloud
    :param word_list: list of strings
    :param filename: string
    """
    pyplot.clf()
    wordcloud = WordCloud(background_color='white', max_font_size=40, relative_scaling=.5).generate(' '.join(word_list))
    pyplot.imshow(wordcloud)
    pyplot.axis('off')
    pyplot.savefig(filename)


def create_review_length_boxplot(reviews, filename, box_mode='tukey'):
    """
     Creates a boxplot chart with five entries that show the distribution of the review lengths for all possible scores
     Reviews longer than 1500 words are ignored in this example
     Chart documentation: http://www.pygal.org/en/latest/documentation/types/box.html
    :param reviews: list of review dictionaries
    :param filename: string
    :param box_mode: type of boxchart, e.g. None, 'tukey', 'stdv'
    """
    one_star_review_lengths = []
    two_star_review_lengths = []
    three_star_review_lengths = []
    four_star_review_lengths = []
    five_star_review_lengths = []
    for review in reviews:
        score = int(review['review/score'])
        review_length = len(review['review/text'].split(' '))
        if review_length > 1500:  # ignore some outliers
            continue
        if score == 1:
            one_star_review_lengths.append(review_length)
        elif score == 2:
            two_star_review_lengths.append(review_length)
        elif score == 3:
            three_star_review_lengths.append(review_length)
        elif score == 4:
            four_star_review_lengths.append(review_length)
        elif score == 5:
            five_star_review_lengths.append(review_length)

    box_plot = pygal.Box(box_mode=box_mode)
    box_plot.title = 'Review Lengths by Review Score'
    box_plot.add('1 Star Reviews', one_star_review_lengths)
    box_plot.add('2 Star Reviews', two_star_review_lengths)
    box_plot.add('3 Star Reviews', three_star_review_lengths)
    box_plot.add('4 Star Reviews', four_star_review_lengths)
    box_plot.add('5 Star Reviews', five_star_review_lengths)
    box_plot.x_labels = ['1 Star', '2 Stars', '3 Stars', '4 Stars', '5 Stars']
    box_plot.render_to_file(filename)


def create_score_barchart(reviews, filename):
    """
     Creates a barchart that shows the distribution of the scores, i.e. how many 1-star reviews, 2-star reviews, etc.
     Chart documentation: http://www.pygal.org/en/latest/documentation/types/bar.html
    :param reviews: list of review dictionaries
    :param filename: string
    """
    score_counter = [0, 0, 0, 0, 0]
    for review in reviews:
        score = int(review['review/score'])
        score_counter[score - 1] += 1

    line_chart = pygal.Bar()
    line_chart.add('Scores', score_counter)
    line_chart.title = 'Amazon Review Scores'
    line_chart.x_labels = ['1 Star', '2 Stars', '3 Stars', '4 Stars', '5 Stars']
    line_chart.render_to_file(filename)
