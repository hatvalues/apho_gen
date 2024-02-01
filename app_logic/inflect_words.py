from textblob import TextBlob
from collections import defaultdict


def pre_process(text):
    return TextBlob(text)

def inflect_plur(blob):
    plural_words = defaultdict(str)
    for word in blob.words:
        plural_words[word] = word.pluralize()
    return dict(plural_words)

def get_plurals(text):
    blob = pre_process(text)
    plurals = inflect_plur(blob)
    return plurals
