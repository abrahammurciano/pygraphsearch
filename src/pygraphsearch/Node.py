from abc import ABC, abstractmethod
from typing import Generic, TYPE_CHECKING, Iterable, TypeVar
from .Edge import TNode, TData, Edge


class Node(Generic[TNode, TData], ABC):
	"""An abstract base class for a node in a graph.

	Args:
		Generic (TNode): The concrete type of the nodes in the graph.
		Generic (TData): The type of the data stored by the edges of the graph.
	"""

	@abstractmethod
	def neighbours(self) -> Iterable[Edge[TNode, TData]]:
		"""Get the edges to all the nodes adjacent to this one.

		Returns:
			Iterable[Edge[TNode, TData]]: The edges to all the nodes adjacent to this one.
		"""
		pass
