from math import log10

def get_similar_score(a, b):

    # Split sentence A and B into words
    a = a.split()
    b = b.split()

    # Make all words lowercase
    a = [x.lower() for x in a]
    b = [x.lower() for x in b]

    # Count the amount of words that A and B have in common
    commons = get_common_words_count(a, b)

    # Compute the amount of common words, divided by the log
    # the length of sentence 1 plus the length of sentence 2.
    # This means that higher similarity weights will be given
    # to longer sentences up to the asymptote of log10

    log_denom = log10(len(a) * len(b))

    # Avoid division by zero
    if log_denom == 0:
        return 0

    return commons / log_denom

def get_query_score(a, query):

    # Split sentence A into words
    a = a.split()
    # Split query into different tokens
    b = b.split()


def get_common_words_count(arr1, arr2):
    sa = set(arr1)
    sb = set(arr2)
    return len(sa & sb)
