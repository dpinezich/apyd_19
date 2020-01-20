from amazon_exercise import stats
from amazon_exercise import visualization
from amazon_exercise import text_processing
from amazon_exercise import file_reader
import nltk

nltk.data.path.append("nltk_data")

# 'review_files/Kindle_Store.txt'
reviews = file_reader.read_review_file('review_files/Watches.txt', max_reviews=5000)
stats.print_review_statistics(reviews)

#visualization.create_review_length_boxplot(reviews, 'watches_review_length.svg')
#visualization.create_score_barchart(reviews, 'watches_score_barchart.svg')

#adjectives = text_processing.get_adjectives(reviews, 1)
#visualization.create_wordcloud(adjectives, 'watches_1_star_adjectives.png')

#adjectives = text_processing.get_adjectives(reviews, 5)
#visualization.create_wordcloud(adjectives, 'watches_5_star_adjectives.png')

#additional
#lemmas = text_processing.get_lemmas(reviews, 3)
#visualization.create_wordcloud(lemmas, 'watches_3_star_lemmas.png')

#lemmas = text_processing.get_lemmas(reviews, 5)
#visualization.create_wordcloud(lemmas, 'watches_5_star_lemmas.png')