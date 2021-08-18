from typing import Iterable, Set
from pygraphsearch.Edge import Edge, TData, TNode
from pygraphsearch.Node import Node


class SimpleNode(Node["SimpleNode", str]):
	def __init__(self, name: str):
		self.__name = name
		self.__edges: Set[Edge["SimpleNode", str]] = set()

	def connect(self, node: "SimpleNode", weight: int, edge_name: str = ""):
		edge = Edge(self, node, edge_name, weight)
		self.__edges.add(edge)
		node.__edges.add(edge)

	@property
	def name(self) -> str:
		return self.__name

	def neighbours(self) -> Iterable[Edge["SimpleNode", str]]:
		return self.__edges.copy()

	def __eq__(self, other):
		return isinstance(other, self.__class__) and self.name == other.name

	def __hash__(self) -> int:
		return hash(self.name)