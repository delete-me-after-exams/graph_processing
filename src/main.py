from graph import Graph
from graph.strategy import BreadthStrategy, DepthStrategy
from graph.observer import Observer


class Logger(Observer):
    def notify(self, message):
        print(message)


if __name__ == "__main__":
    graph = Graph()
    graph.add_node(Graph.Vertex("v1"))
    graph.add_node(Graph.Vertex("v2"))
    graph.add_node(Graph.Vertex("v3"))
    graph.add_node(Graph.Vertex("v4"))
    graph.nodes[0].set_neighbor(graph.nodes[1])
    graph.nodes[0].set_neighbor(graph.nodes[2])
    graph.nodes[2].set_neighbor(graph.nodes[3])

    graph.iteration_strategy = BreadthStrategy()
    for vertex in graph:
        print(vertex.name)

    graph.add_observer(Logger())
    graph.iteration_strategy = DepthStrategy()
    for vertex in graph:
        print(vertex.name)


