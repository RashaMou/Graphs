"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy


class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""

    def __init__(self):
        self.vertices = {}  # This is our adjacency list

    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        """
        self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph from v1 to v2
        """
        # Check if they exist
        if v1 in self.vertices and v2 in self.vertices:
            # Add the edge
            self.vertices[v1].add(v2)
        else:
            print("ERROR ADDING EDGE: Vertex not found")

    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        if vertex_id in self.vertices:
            return self.vertices[vertex_id]
        else:
            return None

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        # Create a q and enqueue starting vertex as an array
        qq = Queue()
        qq.enqueue([starting_vertex])
        # Create a set of traversed vertices
        visited = set()
        # While queue is not empty:
        while qq.size() > 0:
            # dequeue/pop the first vertex
            path = qq.dequeue()
            # if not visited
            if path[-1] not in visited:
                # DO THE THING!!!!!!!
                print(path[-1])
                # mark as visited
                visited.add(path[-1])
                # enqueue all neightbors
                for next_vert in self.get_neighbors(path[-1]):
                    # we copy bcs lists pass by reference, so if we don't create a copy we would mess up our list
                    new_path = list(path)
                    new_path.append(next_vert)
                    qq.enqueue(new_path)

    def dft(self, starting_vertex):
        ## create stack
        ss = Stack()
        ## add starting vertex to stack as an array
        ss.push([starting_vertex])
        # initialize visited set
        visited = set()
        ancestor_path = [starting_vertex]
        # while stack is not empty
        while ss.size() > 0:
            # pop the head of the stack
            path = ss.pop()
            if len(path) > len(ancestor_path):
                ancestor_path = path
            if len(path) == len(ancestor_path):
                if path[-1] < ancestor_path[-1]:
                    ancestor_path = path
            # if not in visited, do the thing, then add to visited
            if path[-1] not in visited:
                visited.add(path[-1])
                # add neighbors to the stack
                for next_vert in self.get_neighbors(path[-1]):
                    new_path = list(path)
                    new_path.append(next_vert)
                    ss.push(new_path)
        return ancestor_path

    def dft_recursive(self, starting_vertex, visited=None):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """
        # base case
        # track visited nodes
        # call function recursively

        # Initial case
        if visited is None:
            visited = set()

        # base case: how do we know when we're done? When we have no more neighbors

        # track visited nodes
        visited.add(starting_vertex)
        print(starting_vertex)

        # call function recursively on neighbors not visited
        for neighbor in self.vertices[starting_vertex]:
            if neighbor not in visited:
                self.dft_recursive(neighbor, visited)

    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        # initialize queue
        qq = Queue()
        # enqueue A PATH TO the starting vertex
        qq.enqueue([starting_vertex])
        # make a set for visited
        visited = set()

        # while queue is not empty
        while qq.size() > 0:
            # dequeue first vertex, add it to path
            path = qq.dequeue()
            # if not visited
            if path[-1] not in visited:
                # Do the thing!
                if path[-1] == destination_vertex:
                    return path
                # mark as visited
                visited.add(path[-1])
                # enqueue all neighbors
                for next_vert in self.get_neighbors(path[-1]):
                    new_path = list(path)
                    new_path.append(next_vert)
                    qq.enqueue(new_path)

    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        ss = Stack()
        ss.push([starting_vertex])
        visited = set()

        # while queue is not empty
        while ss.size() > 0:
            # pop first vertex
            path = ss.pop()
            # if not visited
            if path[-1] not in visited:
                # Do the thing!
                if path[-1] == destination_vertex:
                    return path
                # mark as visited
                visited.add(path[-1])
                # push all neighbors
                for next_vert in self.get_neighbors(path[-1]):
                    new_path = list(path)
                    new_path.append(next_vert)
                    ss.push(new_path)

    def dfs_recursive(
        self, starting_vertex, destination_vertex, visited=None, path=None
    ):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """
        if visited is None:
            visited = set()
        if path is None:
            path = []

        # base case: how do we know when we're done? When we have no more neighbors

        # track visited nodes
        visited.add(starting_vertex)
        new_path = path + [starting_vertex]  # with plus python returns result as copy

        # do the thing
        if starting_vertex == destination_vertex:
            return new_path

        # call function recursively on neighbors not visited
        for neighbor in self.vertices[starting_vertex]:
            if neighbor not in visited:
                neighbor_path = self.dfs_recursive(
                    neighbor, destination_vertex, visited, new_path
                )
                if neighbor_path:
                    return neighbor_path

                # if a node has no unvisited neightbors, do nothing
                # essentially the base case


if __name__ == "__main__":
    graph = Graph()  # Instantiate your graph
    # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_edge(5, 3)
    graph.add_edge(6, 3)
    graph.add_edge(7, 1)
    graph.add_edge(4, 7)
    graph.add_edge(1, 2)
    graph.add_edge(7, 6)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)
    graph.add_edge(2, 3)
    graph.add_edge(4, 6)

    """
    Should print:
        {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    """
    # print(graph.vertices)

    """
    Valid BFT paths:
        1, 2, 3, 4, 5, 6, 7
        1, 2, 3, 4, 5, 7, 6
        1, 2, 3, 4, 6, 7, 5
        1, 2, 3, 4, 6, 5, 7
        1, 2, 3, 4, 7, 6, 5
        1, 2, 3, 4, 7, 5, 6
        1, 2, 4, 3, 5, 6, 7
        1, 2, 4, 3, 5, 7, 6
        1, 2, 4, 3, 6, 7, 5
        1, 2, 4, 3, 6, 5, 7
        1, 2, 4, 3, 7, 6, 5
        1, 2, 4, 3, 7, 5, 6
    """
    # graph.bft(1)

    """
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    """
    graph.dft(1)
    # graph.dft_recursive(1)

    """
    Valid BFS path:
        [1, 2, 4, 6]
    """
    # print(graph.bfs(1, 6))

    """
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    """
    # print(graph.dfs(1, 6))
    # print(graph.dfs_recursive(1, 6))
