from abc import ABC, abstractmethod


class GraphIterator(ABC):

    @abstractmethod
    def __next__(self):
        pass


class BreadthFirstIterator(GraphIterator):
    def __init__(self, graph):
        self.graph = graph
        self.visited = list()
        self.brothers = list()
        if len(self.graph.nodes) > 0:
            self.brothers.append(self.graph.nodes[0])
        self.curr_pos = 0

    def __next__(self):

        if len(self.brothers) == self.curr_pos:
            self.curr_pos = 0
            brothers_copy = self.brothers.copy()
            self.brothers.clear()
            for bro in brothers_copy:
                for neighbor in bro.neighbors:
                    if neighbor not in self.visited:
                        self.brothers.append(neighbor)

        if len(self.brothers) == 0:
            raise StopIteration()
        elif len(self.brothers) > self.curr_pos:
            self.curr_pos += 1

            visited_count = 0
            for neighbor in self.brothers[self.curr_pos-1].neighbors:
                if neighbor in self.visited:
                    visited_count += 1
            if len(self.brothers[self.curr_pos-1].neighbors) == visited_count:
                self.graph.notify_observers("У узла " + self.brothers[self.curr_pos-1].name + " имеются непосещенные соседи")

            self.visited.append(self.brothers[self.curr_pos-1])
            return self.brothers[self.curr_pos-1]


class DepthFirstIterator(GraphIterator):
    def __init__(self, graph):
        self.graph = graph
        self.stack = list()
        self.visited = list()
        if len(self.graph.nodes) > 0:
            self.stack.append(self.graph.nodes[0])

    def __next__(self):
        if len(self.stack) == 0:
            raise StopIteration()

        node = self.stack.pop(len(self.stack)-1)

        visited_count = 0
        for neighbor in node.neighbors:
            if neighbor in self.visited:
                visited_count += 1
        if len(node.neighbors) == visited_count:
            self.graph.notify_observers(
                "У узла " + node.name + " не осталось непосещенных соседей")

        self.visited.append(node)

        if len(node.neighbors) > 0:
            for neighbor in node.neighbors:
                if neighbor not in self.visited:
                    self.stack.append(neighbor)

        return node

