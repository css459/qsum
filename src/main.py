from graphbuilder import *
from importance import *
from sentence import Sentence
import sys

#
# Constants
#

NUMBER_OF_SENTENCE_FOR_SUMMARY = 3


# Print summary
def summarize(sentences, use_query=True, ratio=0.2):
    # Creates the graph and calculates the similarity coefficient for every pair of nodes.
    graph = build_graph([sentence for sentence in sentences])
    set_graph_edge_weights(graph)
    remove_unreachable_nodes(graph)

    # for sentence in graph.nodes():
    #    print sentence.original

    # If it is an empty graph, return an empty array
    if len(graph.nodes()) == 0:
        return []

    # Ranks the tokens using the importance algorithm. Returns dict of sentence -> score
    importance_scores = weighted_importance(graph, use_query)
    # Adds the importance scores to the sentence objects.
    add_scores_to_sentences(sentences, importance_scores)
    # Sorts the extracted sentences by apparition order in the original text.
    sentences.sort(key=lambda s: s.score, reverse=True)

    important_sentences = get_most_important_sentences(sentences, NUMBER_OF_SENTENCE_FOR_SUMMARY)

    return important_sentences


# Main function trigger
if __name__ == "__main__":

    if len(sys.argv) == 1:
        print "You must set a article path as your first argument"
    else:
        if len(sys.argv) == 2:
            s = Sentence.sentences_from_article_file(sys.argv[1])

            summary = summarize(s, use_query=False)
            summary.sort(key=lambda s: s.position_in_article)
            for sentence in summary:
                print sentence.original, "\n[", sentence.score, "]"
        else:
            query = sys.argv[2]

            q = Sentence(query)
            s = Sentence.sentences_from_article_file(sys.argv[1], query)

            summary = summarize(s)
            summary.sort(key=lambda s: s.position_in_article)
            for sentence in summary:
                print sentence.original, "\n[", sentence.score, "]"
