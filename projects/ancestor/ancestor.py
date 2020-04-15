from graph import Graph


def earliest_ancestor(ancestors, starting_node):
    # turn the dataset into a graph by looping over the tuples in the array, and passing in the first item in the tuple using add_vertex, and the second item using add_edge
    graph = Graph()
    for ancestor in ancestors:
        for vertex in ancestor:
            if vertex not in graph.vertices:
                graph.add_vertex(vertex)
        graph.add_edge(ancestor[0], ancestor[1])
    # we now have a graph.
    # do a depth first traversal using the starting node


# we need to find the vertex at the farthest path from the individual - depth first search


test_ancestors = [
    (1, 3),
    (2, 3),
    (3, 6),
    (5, 6),
    (5, 7),
    (4, 5),
    (4, 8),
    (8, 9),
    (11, 8),
    (10, 1),
]

earliest_ancestor(test_ancestors, 4)
