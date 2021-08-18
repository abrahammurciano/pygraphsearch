from typing import Generic, Sequence, List, Union, overload
from .Node import TNode
from .Edge import Edge, TData


class Path(Generic[TNode, TData], Sequence[Edge[TNode, TData]]):
	"""A sequence of edges from one node to another.

	Args:
		Generic (TNode): The type of the nodes of the graph.
		Generic (TData): The type of the data stored by the edges of the graph.
	"""

	def __init__(self, edges: Sequence[Edge[TNode, TData]] = ()):
		self.__edges = list(edges)

	def weight(self) -> int:
		return sum(edge.weight for edge in self.__edges)

	@property
	def edges(self) -> List[Edge[TNode, TData]]:
		return self.__edges.copy()

	@property
	def nodes(self) -> List[TNode]:
		return (
			[self.__edges[0].node_a] + [edge.node_b for edge in self.__edges]
			if self.__edges
			else []
		)

	def __len__(self) -> int:
		return len(self.__edges)

	def __bool__(self) -> bool:
		return bool(self.__edges)

	@overload
	def __getitem__(self, idx: int) -> Edge[TNode, TData]:
		...

	@overload
	def __getitem__(self, s: slice) -> Sequence[Edge[TNode, TData]]:
		...

	def __getitem__(
		self, idx: Union[int, slice]
	) -> Union[Edge[TNode, TData], Sequence[Edge[TNode, TData]]]:
		return self.__edges[idx]

	def __add__(self, other: Sequence[Edge[TNode, TData]]) -> "Path[TNode, TData]":
		return Path(self.__edges + list(other))