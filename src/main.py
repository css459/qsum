from graphbuilder import *
from importance import *
from preprocess import *
from similarity import *
from sentence import Sentence


# Preprocess

# Get similarity

# Graph building

# Graph traversal

# Print summary
def summarize(sentences, ratio=0.2, q=None):
    # Creates the graph and calculates the similarity coefficient for every pair of nodes.
    graph = build_graph([sentence for sentence in sentences])
    set_graph_edge_weights(graph)
    remove_unreachable_nodes(graph)

    #for sentence in graph.nodes():
    #    print sentence.original

    # If it is an empty graph, return an empty array
    if len(graph.nodes()) == 0:
        return []

    # Ranks the tokens using the importance algorithm. Returns dict of sentence -> score
    importance_scores = weighted_importance_random_traversal(graph)
    # Adds the importance scores to the sentence objects.
    add_scores_to_sentences(sentences, importance_scores)
    # Sorts the extracted sentences by apparition order in the original text.
    sentences.sort(key=lambda s: s.score, reverse=True)

    important_sentences = get_most_important_sentences(sentences, 5)

    return important_sentences


# Main function trigger
if __name__ == "__main__":
    query = "Mr. Trump's thoughts on the tax cut"

    q = Sentence(query)
    s = Sentence.sentences_from_article_file("text/nytimes.txt", query)

    summary = summarize(s, 0.2, query)
    summary.sort(key=lambda s: s.position_in_article)
    for sentence in summary:
        print sentence.original, "\n[", sentence.score, "]"


    #print query, "\n"
    #for sen in s:
    #    print sen.norm_to_query, sen.position_in_article, sen.original
