from abc import ABC, abstractmethod
from typing import TYPE_CHECKING, Iterable
from . import TypeVars as T

if TYPE_CHECKING:
	from .Edge import Edge


class Node(ABC):
	"""An abstract base class for a node in a graph.

	Args:
		Generic (E): The type of the edges in the graph.
	"""

	@abstractmethod
	def neighbours(self) -> Iterable[Edge]:
		"""Get the edges to all the nodes adjacent to this one.

		Returns:
			Iterable[E]: The edges to all the nodes adjacent to this one.
		"""
		pass
