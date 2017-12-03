from scipy.sparse import csr_matrix
from scipy.linalg import eig
from numpy import empty as empty_matrix

CONVERGENCE_THRESHOLD = 0.0001

def weighted_importance(graph, dampening=0.85):
    """
    Calculate the weighted importance for the graph based on adjacency and probability matrices
    The result should be a selection of sentences that are the most important

    Default dampening value is 0.85 to weed out unimportant sentences.
    """
    adj_matrix = build_adjacency_matrix(graph)
    prb_matrix = build_probability_matrix(graph)

    pagerank_matrix = dampening * adj_matrix.todense() + (1 - dampening) * prb_matrix
    vals, vecs = eig(pagerank_matrix, left=True, right=False)
    return process_results(graph, vecs)

def build_adjacency_matrix(graph):
    row = []
    col = []
    data = []
    nodes = graph.nodes()
    length = len(nodes)

    for i in xrange(length):
        current_node = nodes[i]
        neighbors_sum = sum(graph.edge_weight((current_node, neighbor)) for neighbor in graph.neighbors(current_node))
        for j in xrange(length):
            edge_weight = float(graph.edge_weight((current_node, nodes[j])))
            if i != j and edge_weight != 0:
                row.append(i)
                col.append(j)
                data.append(edge_weight / neighbors_sum)

    return csr_matrix((data,(row,col)), shape=(length,length))

def build_probability_matrix(graph):
    dimension = len(graph.nodes())
    matrix = empty_matrix((dimension,dimension))

    probability = 1 / float(dimension)
    matrix.fill(probability)

    return matrix

def process_results(graph, vecs):
    scores = {}
    for i, node in enumerate(graph.nodes()):
        scores[node] = abs(vecs[i][0])

    return scores

def add_scores_to_sentences(sentences, scores):
    for sentence in sentences:
        # Adds the score to the object if it has one.
        if sentence.token in scores:
            sentence.score = scores[sentence.token]
        else:
            sentence.score = 0

def get_most_important_sentences(sentences):
    word_count = 0
    selected_sentences = []
    # Loops until the word count is reached.
    for sentence in sentences:
        words_in_sentence = len(sentence.text.split())

        # Checks if the inclusion of the sentence gives a better approximation
        # to the word parameter.
        if abs(words - word_count - words_in_sentence) > abs(words - word_count):
            return selected_sentences

        selected_sentences.append(sentence)
        word_count += words_in_sentence

    return selected_sentences
