class Graph:
    def __init__(self) -> None:
        self.adj_list = {}

    def print_graph(self):
        for vertex in self.adj_list:
            print(vertex, ":", self.adj_list[vertex])

    def add_vertex(self, vertex):
        if vertex not in self.adj_list.keys():
            self.adj_list[vertex] = []
            return True
        return False

    def add_edge(self, v1, v2):
        if v1 not in self.adj_list or v2 not in self.adj_list:
            return False
        self.adj_list[v1].append(v2)
        self.adj_list[v2].append(v1)
        return True

    def remove_edge(self, v1, v2):

        if v1 in self.adj_list and v2 in self.adj_list:
            try:
                self.adj_list[v1].remove(v2)
                self.adj_list[v2].remove(v1)
            except ValueError:
                pass
            return True
        return False

    def remove_vertex(self, v):
        
        if v not in self.adj_list:
            return False

        # remove all edges with the vertex-to-be-deleted
        for i in self.adj_list[v]:
            try:
                self.adj_list[i].remove(v)
            except ValueError:
                pass
        # after deleting all edges, the vertex itself can now be deleted
        del(self.adj_list[v])
        return True



# Test adding a vertex

# my_graph = Graph()
# my_graph.add_vertex("A")
# my_graph.add_vertex("B")

# my_graph.print_graph()


# Test add_edge()

# my_graph = Graph()

# my_graph.add_vertex(1)
# my_graph.add_vertex(2)

# my_graph.add_edge(1,2)

# my_graph.print_graph()



# Test remove_edge()

# my_graph = Graph()
# my_graph.add_vertex('A')
# my_graph.add_vertex('B')
# my_graph.add_vertex('C')

# my_graph.add_edge('A','B')
# my_graph.add_edge('B','C')
# my_graph.add_edge('C','A')

# print('Graph before remove_edge():')
# my_graph.print_graph()


# my_graph.remove_edge('A','C')


# print('\nGraph after remove_edge():')
# my_graph.print_graph()


# Test remove_vertex()
my_graph = Graph()
my_graph.add_vertex('A')
my_graph.add_vertex('B')
my_graph.add_vertex('C')
my_graph.add_vertex('D')

my_graph.add_edge('A','B')
my_graph.add_edge('A','C')
my_graph.add_edge('A','D')
my_graph.add_edge('B','D')
my_graph.add_edge('C','D')


print('Graph before remove_vertex():')
my_graph.print_graph()


my_graph.remove_vertex('D')


print('\nGraph after remove_vertex():')
my_graph.print_graph()
