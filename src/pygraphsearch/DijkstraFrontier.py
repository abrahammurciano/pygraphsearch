from typing import Generic, Optional, Set
from .Edge import TData, TNode
from .Frontier import Frontier
from .Heap import Heap
from .State import State


class DijkstraFrontier(Generic[TNode, TData], Frontier[TNode, TData]):
	"""A frontier for a graph search algorithm that performs Dijkstra's algorithm.

	Args:
		Generic (TNode): The type of the nodes of the graph.
		Generic (TData): The type of the data stored by the edges of the graph.
	"""

	def __init__(self, start: TNode):
		"""Construct a frontier for Dijkstra's algorithm.

		Args:
			start (TNode): The node to start the search from.
		"""
		self.__heap = Heap[State[TNode, TData]](key=lambda state: state.path.weight())
		self.__heap.push(State(start))
		self.__visited: Set[TNode] = set()

	def extract(self) -> Optional[State[TNode, TData]]:
		self.__remove_visited()
		state = self.__heap.pop()
		self.__visited.add(state.node)
		return state

	def insert(self, state: State[TNode, TData]):
		self.__heap.push(state)

	def __remove_visited(self):
		"""Remove visited nodes from the heap until the top element is unvisited."""
		while self.__heap and self.__heap.peek() in self.__visited:
			self.__heap.pop()

	def __len__(self) -> int:
		"""Get the number of elements in the frontier.

		Note:
			This number may include elements that have already been popped, in which case they'll not be popped again. Therefore this is really an upper bound on the number of elements that can be popped. The only other thing guaranteed is that when there are no unvisited elements, this function will return 0 (as required by the contract of Frontier).

		Returns:
			int: The number of elements in the frontier.
		"""
		self.__remove_visited()
		return len(self.__heap)