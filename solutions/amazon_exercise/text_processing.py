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
    """
     Get the tokens from the review text if the given score matches the score of the given review
     If the given score is None than the tokens of the review text are returned anyways
    :param review: review dictionary
    :param score: score from 1-5 or None
    :return: list of tokens
    """
    review_text = ''
    if score:
        if review['review/score'] == score:
            review_text = review['review/text']
    else:
        review_text = review['review/text']
    tokens = nltk.word_tokenize(review_text)
    return tokens


def get_adjectives(reviews, score=None):
    """
     Finds all adjectives in the review texts of a given list of review dictionaries
    :param reviews: list of review dictionaries
    :param score: (optional) only reviews with given score are analyzed
    :return: list of adjectives (with multiple entries)
    """
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
    """
     Finds all lemmas in the review texts of a given list of review dictionaries using the WordNetLemmatizer
    :param reviews: list of review dictionaries
    :param score: (optional) only reviews with given score are analyzed
    :return: list of lemmas (with multiple entries)
    """
    wordnet_lemmatizer = WordNetLemmatizer()
    lemmas = []
    for review in reviews:
        tokens = get_review_tokens(review, score)
        pos_tags = nltk.pos_tag(tokens, tagset='universal')
        for pos in pos_tags:
            word = pos[0].lower()
            if word in custom_stopwords:
                continue
            if pos[1] == 'ADJ':
                word = wordnet_lemmatizer.lemmatize(word, pos='a')
                lemmas.append(word)
            elif pos[1] == 'NOUN':
                word = wordnet_lemmatizer.lemmatize(word, pos='n')
                lemmas.append(word)
            elif pos[1] == 'VERB':
                word = wordnet_lemmatizer.lemmatize(word, pos='v')
                lemmas.append(word)
    return lemmas
