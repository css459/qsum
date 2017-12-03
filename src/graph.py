class Graph(object):
    WEIGHT_ATTRIBUTE_NAME = "weight"
    DEFAULT_WEIGHT = 0

    LABEL_ATTRIBUTE_NAME = "label"
    DEFAULT_LABEL = ""

    def __init__(self):
        """
        Initializer to create an undirected graph with weighted edges
        """
        # Metadata about edges
        self.edge_properties = {}  # Mapping: Edge -> Dict mapping, label-> str, wt->num
        self.edge_attr = {}  # Key value pairs: (Edge -> Attributes)
        # Metadata about nodes
        self.node_attr = {}  # Pairing: Node -> Attributes
        self.node_neighbors = {}  # Pairing: Node -> Neighbors

    def has_edge(self, edge):
        """
        Check if the undirected graph has an edge
        :param edge: Pair of nodes
        """
        u, v = edge
        return (u, v) in self.edge_properties and (v, u) in self.edge_properties

    def edge_weight(self, edge):
        """
        Get the weight of an edge in an undirected Graph
        :param edge: Pair of nodes
        """
        return self.get_edge_properties(edge).setdefault(self.WEIGHT_ATTRIBUTE_NAME, self.DEFAULT_WEIGHT)

    def neighbors(self, node):
        """
        Get the neighbors of a node in an undirected Graph
        :param node: Node to get neighbors
        """
        return self.node_neighbors[node]

    def has_node(self, node):
        """
        Check if a node has another node as its neighbors
        :param node: Node to check neighbors
        """
        return node in self.node_neighbors

    def add_edge(self, edge, wt=1, label='', attrs=None):
        """
        Add an edge association between two nodes
        :param edge: Pair of nodes
        """
        u, v = edge
        if v not in self.node_neighbors[u] and u not in self.node_neighbors[v]:
            self.node_neighbors[u].append(v)
            if u != v:
                self.node_neighbors[v].append(u)

            self.add_edge_attributes((u, v), attrs)
            self.set_edge_properties((u, v), label=label, weight=wt)
        else:
            raise ValueError("Edge (%s, %s) already in graph" % (u, v))

    def add_node(self, node, attrs=None):
        """
        Adds a node into the graph
        :param node: Node to be added
        """
        if attrs is None:
            attrs = []
        if node not in self.node_neighbors:
            self.node_neighbors[node] = []
            self.node_attr[node] = attrs
        else:
            raise ValueError("Node %s already in graph" % node)

    def nodes(self):
        """
        Returns a list of nodes that exist in the graph
        """
        return list(self.node_neighbors.keys())

    def edges(self):
        """
        Returns a list of edges in the existing graph
        """
        return [a for a in self.edge_properties.keys()]

    def del_node(self, node):
        """
        Deletes a node from the graph
        :param node: Node to be deleted
        """
        for each in list(self.neighbors(node)):
            if each != node:
                self.del_edge((each, node))
        del (self.node_neighbors[node])
        del (self.node_attr[node])

    def del_edge(self, edge):
        """
        Deletes an edge association from the graph
        :param edge: Edge to be deleted
        """
        u, v = edge
        self.node_neighbors[u].remove(v)
        self.del_edge_labeling((u, v))
        if u != v:
            self.node_neighbors[v].remove(u)
            self.del_edge_labeling((v, u))

    # Helper methods
    def get_edge_properties(self, edge):
        return self.edge_properties.setdefault(edge, {})

    def add_edge_attributes(self, edge, attrs):
        if attrs is not None:
            for attr in attrs:
                self.add_edge_attribute(edge, attr)

    def add_edge_attribute(self, edge, attr):
        self.edge_attr[edge] = self.edge_attributes(edge) + [attr]

        if edge[0] != edge[1]:
            self.edge_attr[(edge[1], edge[0])] = self.edge_attributes((edge[1], edge[0])) + [attr]

    def edge_attributes(self, edge):
        try:
            return self.edge_attr[edge]
        except KeyError:
            return []

    def set_edge_properties(self, edge, **properties):
        self.edge_properties.setdefault(edge, {}).update(properties)
        if edge[0] != edge[1]:
            self.edge_properties.setdefault((edge[1], edge[0]), {}).update(properties)

    def del_edge_labeling(self, edge):
        keys = [edge, edge[::-1]]

        for key in keys:
            for mapping in [self.edge_properties, self.edge_attr]:
                try:
                    del (mapping[key])
                except KeyError:
                    pass
