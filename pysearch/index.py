from abc import ABC, abstractmethod


class Indexer(ABC):

    @abstractmethod
    def index(self, document):
        pass

    @abstractmethod
    def search(self, word):
        pass
