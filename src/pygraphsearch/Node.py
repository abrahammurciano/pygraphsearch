from abc import ABC, abstractmethod
from typing import Generic, TYPE_CHECKING, Iterable
from . import TypeVars as T

if TYPE_CHECKING:
	from .Edge import Edge


class Node(ABC):
	"""An abstract base class for a node in a graph."""

	@abstractmethod
	def neighbours(self) -> Iterable["Edge[T.Node, T.Data]"]:
		"""Get the edges to all the nodes adjacent to this one.

		Returns:
			Iterable[Edge]: The edges to all the nodes adjacent to this one.
		"""
		pass
