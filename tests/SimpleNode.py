from typing import Iterable, Set
from pygraphsearch.edge import Edge
from pygraphsearch.node import Node


class SimpleNode(Node):
    def __init__(self, name: str):
        self.__name = name
        self.__edges: Set[Edge["SimpleNode"]] = set()

    def connect(self, node: "SimpleNode", weight: int):
        edge = Edge(self, node, weight)
        self.__edges.add(edge)
        node.__edges.add(edge)

    @property
    def name(self) -> str:
        return self.__name

    def neighbours(self) -> Iterable[Edge["SimpleNode"]]:
        return self.__edges.copy()

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.name == other.name

    def __hash__(self) -> int:
        return hash(self.name)
