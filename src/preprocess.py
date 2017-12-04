import re

from nltk import wordpunct_tokenize
from nltk.corpus import stopwords
from nltk.stem.snowball import SnowballStemmer
from nltk.tokenize.punkt import PunktSentenceTokenizer, PunktParameters

ABBREV_TYPES = ['dr', 'vs', 'mr', 'mrs', 'prof', 'inc']
PUNCTUATION = ['.', ',', '"', "'", '?', '!', ':', ';', '(', ')', '[', ']', '{', '}']


def remove_non_ascii(string):
    """
    Replaces all non-ascii elements in string with a single space
    :param string: A string containing non-ascii characters
    :return: A sanitized string containing only ascii characters
    """
    return re.sub(r'[^\x00-\x7F]+', ' ', string)


def chunk_article(article):
    """
    Given a long string, article, representing the full text of a given article,
    convert the string into a list of sentences
    :param article: A string representing the full text of an article
    :return: A list of strings representing the sentences of the article
    """

    # Add support to NOT falsely split a sentence at a title like dr or mr
    p_params = PunktParameters()
    p_params.abbrev_types = set(ABBREV_TYPES)
    p = PunktSentenceTokenizer(p_params)

    sen = p.sentences_from_text(article, realign_boundaries=False)

    # Strip extra spaces
    for s in sen:
        s.strip()

    return sen


def remove_stopwords(sentence):
    """
    From the given sentence, return an array of tokens (words)
    containing no stop words
    :param sentence: A string or list of strings representing a sentence
    :return: A list of strings which do not contain stop words (or None if
    `sentence` is a type other than `list` or `str`)
    """

    stops = set(stopwords.words('english'))
    stops.update(PUNCTUATION)

    # If sentence is a string, then tokenize, if not, then treat as array
    # If sentence is something else, return None
    if isinstance(sentence, str):
        return [x.lower() for x in wordpunct_tokenize(sentence) if x.lower() not in stops]
    elif isinstance(sentence, list):
        return [x.lower() for x in sentence if x.lower() not in stops]
    else:
        return


def stems_only(sentence, no_stop_words):
    """
    From the given sentence, converts all non stop words to stems
    only
    :param sentence: A string representing a sentence
    :param no_stop_words: Bool to specify if stop words are to be included in output
    :return: A list of strings which contain only stems (and no stop words)
    """

    if no_stop_words:
        s = remove_stopwords(sentence)
    else:
        s = wordpunct_tokenize(sentence)

    out = []
    stemmer = SnowballStemmer('english', ignore_stopwords=True)
    for w in s:
        out.append(stemmer.stem(w))

    return out


def auto_preprocess(article):
    """
    For a long string, article, run all the default preprocessing operations defined
    in this file
    :param article: A string representing the full text of an article
    :return: A 2D list of sentences, and stemmed words with stop words removed from sentences
    """
    sentences = chunk_article(remove_non_ascii(article))

    out = []
    for s in sentences:
        out.append(stems_only(s, no_stop_words=True))

    return out


def auto_preprocess_single(sentence):
    """
    Auto preprocess a single sentence
    :param sentence: A string representing a sentence
    :return: The preprocessed sentence
    """
    return auto_preprocess(sentence)[0]
