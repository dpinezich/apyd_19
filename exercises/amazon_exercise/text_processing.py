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

    review_text = ''
    if score:
        if review['review/score'] == score:
            review_text = review['review/text']

    tokens = nltk.word_tokenize(review_text)

    return tokens


def get_adjectives(reviews, score=None):
    adjectives = []

    for review in reviews:
        tokens = get_review_tokens(review, score)
        pos_tags = nltk.pos_tag(tokens, tagset='universal')
        for pos in pos_tags:
            word = pos[0].lower()
            if pos[1] == 'ADJ' and word not in custom_stopwords:
                adjectives.append(word)

    return adjectives


def get_lemmas(reviews, score=None):
    wordnet_lemmatizer = WordNetLemmatizer()
    lemmas = []

    for review in reviews:
        tokens = get_review_tokens(review, score)
        pos_tags = nltk.pos_tag(tokens, tagset='universal')
        for pos in pos_tags:
            word = pos[0].lower()
            if word in custom_stopwords:
                continue
            elif pos[1] == 'ADJ':
                word = wordnet_lemmatizer.lemmatize(word, pos='a')
                lemmas.append(word)
            elif pos[1] == 'NOUN':
                word = wordnet_lemmatizer.lemmatize(word, pos='n')
                lemmas.append(word)
            elif pos[1] == 'VERB':
                word = wordnet_lemmatizer.lemmatize(word, pos='v')
                lemmas.append(word)

    return lemmas