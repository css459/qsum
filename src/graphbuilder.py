from graph import Graph

def build_graph(list_sentences):
    """
    Create a graph without weights from a list of sentences
    """
    graph = Graph()
    for line in list_sentences:
        if not graph.has_node(line):
            graph.add_node(line)
    return graph

def set_graph_edge_weights(graph):
    for sentence_1 in graph.nodes():
        for sentence_2 in graph.nodes():

            edge = (sentence_1, sentence_2)
            if sentence_1 != sentence_2 and not graph.has_edge(edge):
                similarity = get_similarity(sentence_1, sentence_2)
                if similarity != 0:
                    graph.add_edge(edge, similarity)

    # Handles the case in which all similarities are zero.
    # The resultant summary will consist of random sentences.
    if all(graph.edge_weight(edge) == 0 for edge in graph.edges()):
        create_random_graph(graph)

def create_random_graph(graph):
    """
    Baseline random graph. This function will only be triggered when
    there are no similarities in the graph
    """
    nodes = graph.nodes()

    for i in xrange(len(nodes)):
        for j in xrange(len(nodes)):
            if i == j:
                continue
            edge = (nodes[i], nodes[j])
            if graph.has_edge(edge):
                graph.del_edge(edge)
            graph.add_edge(edge, 1)

def remove_unreachable_nodes(graph):
    for node in graph.nodes():
        if sum(graph.edge_weight((node, other)) for other in graph.neighbors(node)) == 0:
            graph.del_node(node)
