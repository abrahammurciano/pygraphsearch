from typing import Generic, Optional, Set
from collections import deque
from .Frontier import Frontier
from .State import State
from .Node import TNode
from .Edge import TData


class BreadthFirstFrontier(Generic[TNode, TData], Frontier[TNode, TData]):
	"""A frontier for a graph search algorithm that performs Breadth First Search (BFS) using a queue.

	Args:
		Generic (TNode): The type of the nodes of the graph.
		Generic (TData): The type of the data stored by the edges of the graph.
	"""

	def __init__(self, start: TNode):
		self.__queue = deque[State[TNode, TData]]()
		self.__queue.append(State(start))
		self.__visited: Set[TNode] = set()

	def extract(self) -> Optional[State[TNode, TData]]:
		return self.__queue.popleft() if self.__queue else None

	def insert(self, state: State[TNode, TData]):
		if state.node not in self.__visited:
			self.__visited.add(state.node)
			self.__queue.append(state)

	def __len__(self) -> int:
		return len(self.__queue)