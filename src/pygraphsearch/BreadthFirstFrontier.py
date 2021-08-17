from typing import Generic, Optional, Set
from collections import deque
from .Frontier import Frontier
from .State import State
from . import TypeVars as T


class BreadthFirstFrontier(Generic[T.Node, T.Data], Frontier[T.Node, T.Data]):
	"""A frontier for a graph search algorithm that performs Breadth First Search (BFS) using a queue.

	Args:
		Generic (T.Node): The type of the nodes of the graph.
		Generic (T.Data): The type of the data stored by the edges of the graph.
	"""

	def __init__(self, start: T.Node):
		self.__queue = deque[State[T.Node, T.Data]]()
		self.__queue.append(State(start))
		self.__visited: Set[T.Node] = set()

	def extract(self) -> Optional[State[T.Node, T.Data]]:
		return self.__queue.popleft() if self.__queue else None

	def insert(self, state: State[T.Node, T.Data]):
		if state.node not in self.__visited:
			self.__visited.add(state.node)
			self.__queue.append(state)

	def __len__(self) -> int:
		return len(self.__queue)