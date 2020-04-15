from graph import Graph


def earliest_ancestor(ancestors, starting_node):
    # turn the dataset into a graph by looping over the tuples in the array, and passing in the first item in the tuple using add_vertex, and the second item using add_edge
    graph = Graph()
    # for ancestor in ancestors:
    #     for vertex in ancestor:
    #         if vertex not in graph.vertices:
    #             graph.add_vertex(vertex)
    #     graph.add_edge(ancestor[0], ancestor[1])
    for pair in ancestors:
        parent = pair[0]
        child = pair[1]
        if parent not in graph.vertices:
            graph.add_vertex(parent)
        if child not in graph.vertices:
            graph.add_vertex(child)
        # we're doing child: parent because we're traversing from bottom to top
        graph.add_edge(child, parent)
    print(graph.vertices)

    # do depth first search with starting node, and return all the possible paths that end in None
    # compare the paths, and return the one with the longest length


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

earliest_ancestor(test_ancestors, 7)
