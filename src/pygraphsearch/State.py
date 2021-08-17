from typing import Generic, Iterable, List, Optional

from .Path import Path
from .Edge import Edge
from .Node import TNode
from .Edge import TData


class State(Generic[TNode, TData]):
	"""Represents the state of a search.

	A state is made up of the current node and the path taken to get there.

	Args:
		Generic (TNode): The concrete type of the node that this state contains.
		Generic (TData): The type of the data stored in the edges.
	"""

	def __init__(self, node: TNode, path: Path = Path()):
		"""Construct a state.

		Args:
			node (TNode): The current node.
			path (Path, optional): The sequence of edges taken to reach the current node. Defaults to an empty path.
		"""
		self.__node = node
		self.__path = Path(path or [])

	@property
	def node(self) -> TNode:
		"""The current node in the search."""
		return self.__node

	@property
	def path(self) -> Path[TNode, TData]:
		"""The list of edges taken to reach the current node."""
		return self.__path

	def next_states(self) -> Iterable["State[TNode,TData]"]:
		"""The states reachable by taking one edge from the current node of this state. This does not include backtracking to the node before the current one.

		Returns:
			Iterable[State]: The states that can be reached from the current node by taking a single edge.
		"""
		return [
			State[TNode, TData](edge.node_b, self.__path + [edge])
			for edge in self.node.neighbours()
			if not self.path or edge != self.path[-1]
		]
