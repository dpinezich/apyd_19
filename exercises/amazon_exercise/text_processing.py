import string

import nltk
import os.path
from nltk.stem import WordNetLemmatizer

base = os.path.dirname(os.path.abspath(__file__))
nltk.data.path.append(base + '/nltk_data')

stopwords_file = open(os.path.join(base, 'custom_stopwords.txt'))
custom_stopwords = []
for stop_word in stopwords_file.read().split(' '):
    custom_stopwords.append(stop_word)

def get_review_tokens(review, score):
    # Implementation...
    # ...
    # ...
    # ...
    return


def get_adjectives(reviews, score=None):
    adjectives = []

    # Implementation...
    # ...
    # ...
    # ...

    return ' '.join(adjectives)


def get_lemmas(reviews, score=None):
    wordnet_lemmatizer = WordNetLemmatizer()
    lemmas = []

    # Implementation...
    # ...
    # ...
    # ...

    return ' '.join(lemmas)