from abc import ABC, abstractmethod


class Observable(ABC):
    @abstractmethod
    def add_observer(self, observer):
        pass

    @abstractmethod
    def remove_observer(self, observer):
        pass

    @abstractmethod
    def notify_observers(self, message):
        pass


class Observer(ABC):
    @abstractmethod
    def notify(self, message):
        pass
