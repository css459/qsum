from graphbuilder import *
from importance import *
from preprocess import *
from similarity import *


# Preprocess
def preprocess_from_file(file_name):
    art = ""
    with open(file_name, 'r') as a:
        for line in a:
            art += remove_non_ascii(line) + " "
            art.strip()

    return auto_preprocess(art)


# Get similarity

# Graph building

# Graph traversal

# Print summary
def summarize(text, ratio=0.2, q=None):
    # Creates the graph and calculates the similarity coefficient for every pair of nodes.
    graph = build_graph([sentence.token for sentence in sentences])
    set_graph_edge_weights(graph)
    remove_unreachable_nodes(graph)

    # If it is an empty graph, return an empty array
    if len(graph.nodes()) == 0:
        return []

    # Ranks the tokens using the importance algorithm. Returns dict of sentence -> score
    importance_scores = weighted_importance(graph)
    # Adds the importance scores to the sentence objects.
    add_scores_to_sentences(sentences, importance_scores)
    # Extracts the most important sentences with the selected criterion.
    extracted_sentences = get_most_important_sentences(sentences)
    # Sorts the extracted sentences by apparition order in the original text.
    extracted_sentences.sort(key=lambda s: s.index)

    return print_results(extracted_sentences, importance_scores)


def print_results(extracted_sentences, score):
    if score:
        return [(sentence.text, sentence.score) for sentence in extracted_sentences]
    return "\n".join([sentence.text for sentence in extracted_sentences])


# Main function trigger
if __name__ == "__main__":
    query = "Mr. Trump's thoughts on the tax cut"
    sentences = preprocess_from_file("text/nytimes.txt")

    processed_query = auto_preprocess_single(query)
    get_similar_scores_to_query(processed_query, sentences)
