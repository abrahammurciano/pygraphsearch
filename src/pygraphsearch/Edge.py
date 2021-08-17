from typing import Generic, Optional, Set, TypeVar
from .Node import TNode

TData = TypeVar("TData")


class Edge(Generic[TNode, TData]):
	"""Represents a way to reach one node from another.

	Args:
		Generic (TNode): The type of the nodes of the graph.
		Generic (TData): Data to be contained by an edge. For example if the edge represents getting from one chess board position to another, the data might be "Be5".
	"""

	def __init__(self, node_a: TNode, node_b: TNode, data: Optional[TData] = None):
		"""Construct a node.

		Args:
			node_a (TNode): One of the endpoints of the edge
			node_b (TNode): The other endpoint of the edge.
			data (TData, optional): Data to be stored by the node. Defaults to None.
		"""
		self.__node_a = node_a
		self.__node_b = node_b
		self.__data = data

	@property
	def node_a(self) -> TNode:
		"""The first node of the edge."""
		return self.__node_a

	@property
	def node_b(self) -> TNode:
		"""The second node of the edge."""
		return self.__node_b

	@property
	def data(self) -> Optional[TData]:
		"""The data stored in this edge."""
		return self.__data

	@property
	def __nodes_set(self) -> Set[TNode]:
		"""A set of the two nodes in this edge."""
		return {self.node_a, self.node_b}

	def __eq__(self, other):
		return isinstance(other, Edge) and self.__nodes_set == other.__nodes_set

	def __str__(self) -> str:
		return str(self.data) if self.data is not None else str(self.__nodes_set)

	def __repr__(self) -> str:
		return str(self)