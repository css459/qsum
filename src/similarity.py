from math import log10


def get_common_words_count(arr1, arr2):
    """
    For two lists of strings, get the count intersect of
    common elements between them.
    :param arr1: A preprocessed list of stings for sentence A
    :param arr2: A preprocessed list of stings for sentence B
    :return: The count of similar elements
    """
    return len(list(set(arr1).intersection(arr2)))


def get_similar_score(a, b):
    """
    Creates a similarity score for two preprocessed lists
    of strings representing sentences. The similarity score is
    evaluated based upon the common stems in each of the lists.
    The total number of common stems is then dived by the log base
    10 of the sentence lengths. The similarity is not normalized
    and can be any floating point number over 0. Thus, the
    similarity score should only be used for *ordinal* purposes.
    :param a: A preprocessed list of stings for sentence A
    :param b: A preprocessed list of stings for sentence B
    :return: A score of similarity
    """

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


def get_similar_scores_to_query(query, sentences):
    """
    For a preprocessed query sentence, find the score of the most
    similar and least similar sentence in `sentences` to `query`.
    Returns a list of normalized floats in range [0, 1] where 0 is
    the least similar sentence to the query string, and 1 is the most similar.
    :param query: A preprocessed query string to normalize scores against
    :param sentences: A list of preprocessed sentences to  score
    :return: A list of tuples where the first value is the normalized similarity
    score, and the second value is the sentence for such score from `sentences`
    """

    # Stores a list of tuples of:
    #   (normalized score, sentence from sentences)
    out = []

    # Get the min and max score in sentences
    min_score = float('inf')
    max_score = -float('inf')

    for s in sentences:
        score = get_similar_score(query, s)

        if score < min_score:
            min_score = score
        if score > max_score:
            max_score = score

        out.append((score, s))

    # Normalize all scores
    for i in range(len(out)):
        norm = (out[i][0] - min_score) / (max_score - min_score)
        out[i] = (norm, out[i][1])

    out = sorted(out, key=lambda tup: tup[0], reverse=True)

    print "Query: ", query
    print "Min similarity: ", min_score
    print "Max similarity: ", max_score, "\n"
    for o in out:
        print o

    # Return list sorted by score in reverse order
    return out
