# use this when my PR is merged: from generic_heap import Heap
from typing import Any, Callable, Generic, Optional, TypeVar
from .Edge import TData
from .Frontier import Frontier
from .Node import Node
from .State import State
from .Heap import Heap

TNode = TypeVar("TNode", bound="Node")


class AStarFrontier(Generic[TNode, TData], Frontier[TNode, TData]):
	"""A frontier to be used for search algorithms which implements A* Search."""

	def __init__(self, start: TNode, heuristic: Callable[[State[TNode, TData]], Any]):
		"""Create a frontier for the A* Search algorithm.

		Args:
			heuristic (Callable[[State], Any]): A function which takes a state and returns some comparable object representing the estimated distance from that state to a target state.
		"""
		self.__heap = Heap[State[TNode, TData]](
			key=lambda state: state.path.weight() + heuristic(state)
		)
		self.insert(State[TNode, TData](start))

	def extract(self) -> Optional[State[TNode, TData]]:
		return self.__heap.pop() if not self.is_empty() else None

	def insert(self, state: State[TNode, TData]):
		self.__heap.push(state)

	def __len__(self) -> int:
		return len(self.__heap)