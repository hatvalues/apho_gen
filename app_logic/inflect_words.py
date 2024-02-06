"""Stub functionality for some initial testing"""

from textblob import TextBlob
from collections import defaultdict


def pre_process(text):
    """
    Return a textblob.

    Parameter
    ---------
    text : str
        text to be preprocessed.

    Returns
    -------
    blob
        a textblob.
    """
    blob = TextBlob(text)
    return blob

def inflect_plur(blob):
    """
    Return a dictionary of (simplified) plurals.
    Note: the textblob library does not error on words that don't have plurals

    Parameter
    ---------
    blob : textblob.textBlob
        a preprocessed text.

    Returns
    -------
    plural_words
        a dictionary containing word: word_plur key-pairs.
    """
    plural_words = defaultdict(str)
    for word in blob.words:
        plural_words[word] = word.pluralize()
    return dict(plural_words)


def get_plurals(text):
    """
    Wrapper function to preprocesses text and return a dictionary of (simplified) plurals.

    Parameter
    ---------
    blob : textblob.textBlob
        a preprocessed text.

    Returns
    -------
    plural_words
        a dictionary containing word: word_plur key-pairs.
    """
    blob = pre_process(text)
    plurals = inflect_plur(blob)
    return plurals
