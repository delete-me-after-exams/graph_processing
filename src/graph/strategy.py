from abc import ABC, abstractmethod
from graph.iterator import BreadthFirstIterator, DepthFirstIterator


class IterationStrategy(ABC):
    @abstractmethod
    def get_iterator(self, nodes):
        pass


class BreadthStrategy(IterationStrategy):
    def get_iterator(self, graph):
        return BreadthFirstIterator(graph)


class DepthStrategy(IterationStrategy):
    def get_iterator(self, graph):
        return DepthFirstIterator(graph)
