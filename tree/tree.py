from abc import ABC, abstractmethod


class Tree(ABC):
    """An abstract class representing tree DS
    Extends:
        ABC
    """

    class Position:
        """nested Position class for Tree
        """

        def element(self):
            """Return element stored at this position"""
            raise NotImplementedError('must be implemented by subclass')

        def __eq__(self, other):
            """Returns true if other position represents the same location"""
            raise NotImplementedError('must be implemented by subclass')

        def __ne__(self, other):
            """Returns true if other not represents same location"""
            return not (self == other)

    @abstractmethod
    def root(self):
        """Return Position representing the tree's root"""
        raise NotImplementedError('must be implemented by subclass')

    @abstractmethod
    def parent(self, p):
        """Return p's parent or None if empty"""
        raise NotImplementedError('must be implemented by subclass')

    def children(self, p):
        """Return's p's children as iterator"""
        raise NotImplementedError('must be implemented by subclass')

    def num_children(self, p):
        """Return's total no of children of p"""
        raise NotImplementedError('must be implemented by subclass')

    def __len__(self):
        """Return's total no of elements in the tree"""
        raise NotImplementedError('must be implemented by subclass')

    def is_root(self, p):
        """Return's True if Position p represents the root of the tree"""
        return self.root() == p

    def is_leaf(self, p):
        return self.num_children(p) == 0

    def is_empty(self):
        return len(self) == 0

    def depth(self, p):
        if self.is_root(p):
            return 0
        return 1 + self.depth(self.parent(p))

    def _height(self, p):
        if self.is_leaf(p):
            return 0
        return 1 + max(self._height(c) for c in self.children(p))

    def height(self, p=None):
        if p is None:
            p = self.root()
        return self._height(p)
