from graph.observer import Observable


class Graph(Observable):
    class Vertex:
        def __init__(self, name):
            self.name = name
            self.neighbors = list()

        def set_neighbor(self, vertex):
            if not vertex in self.neighbors:
                self.neighbors.append(vertex)
                vertex.neighbors.append(self)

        def remove_neighbor(self, vertex):
            self.neighbors.remove(vertex)
            vertex.neighbors.remove(self)

    def __init__(self):
        self.nodes = list()
        self.iteration_strategy = None
        self.observers = list()

    def add_node(self, vertex):
        if not vertex in self.nodes:
            self.nodes.append(vertex)

    def remove_node(self, vertex):
        for node in self.nodes:
            node.remove_neighbor(vertex)
        self.nodes.remove(vertex)

    def __iter__(self):
        return self.iteration_strategy.get_iterator(self)

    def add_observer(self, observer):
        self.observers.append(observer)

    def remove_observer(self, observer):
        if observer in self.observers:
            self.observers.pop(observer)

    def notify_observers(self, message):
        for observer in self.observers:
            observer.notify(message)
