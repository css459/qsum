from preprocess import *
from similarity import get_similar_score


class Sentence(object):
    def __init__(self, sentence_string, index=0, norm_to_query=0.0):
        self.original = sentence_string
        self.preprocessed = auto_preprocess_single(sentence_string)
        self.position_in_article = index
        self.norm_to_query = norm_to_query

    def get_similar_scores_to_self(self, sentences, sort=True):
        """
            For a preprocessed query sentence, find the score of the most
            similar and least similar sentence in `sentences` to self.`preprocessed`.
            Returns a list of normalized floats in range [0, 1] where 0 is
            the least similar sentence to the query string, and 1 is the most similar.
            :param sentences: A list of Sentence objects to score
            :return: A list of tuples where the first value is the normalized similarity
            score, and the second value is the sentence for such score from `sentences`
            """

        query = self.preprocessed

        # Stores a list of tuples of:
        #   (normalized score, sentence from sentences)
        out = []

        # Get the min and max score in sentences
        min_score = float('inf')
        max_score = -float('inf')

        for s in sentences:
            score = get_similar_score(query, s.preprocessed)

            if score < min_score:
                min_score = score
            if score > max_score:
                max_score = score

            out.append((score, s))

        # Normalize all scores
        for i in range(len(out)):
            norm = (out[i][0] - min_score) / (max_score - min_score)
            out[i] = (norm, out[i][1])

        # Return list sorted by score in reverse order (if sort is True)
        if sort:
            return sorted(out, key=lambda tup: tup[0], reverse=True)
        else:
            return out

    @staticmethod
    def sentences_from_article_file(file_path, query):
        """
        From a file containing an article, will create a set of Sentence objects
        for every sentence in the article
        :param file_path: Path to article file
        :return: A list of Sentence objects in order of article occurrence
        """

        article = ""
        with open(file_path, 'r') as a:
            for line in a:
                article += remove_non_ascii(line) + " "
                article.strip()

        out = []

        # Generate Sentence Objects from article string
        chunks = chunk_article(article)
        for i in range(len(chunks)):
            out.append(Sentence(chunks[i], i))

        # Assign query similarity normals (not sorted and index-aligned with 'out')
        norms = Sentence(query).get_similar_scores_to_self(out, sort=False)
        for i in range(len(out)):
            out[i].norm_to_query = norms[i][0]

        return out
