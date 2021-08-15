from typing import Optional, Set
from collections import deque
from .Frontier import Frontier
from .Node import Node
from .State import State


class BreadthFirstFrontier(Frontier):
	"""A frontier for a graph search algorithm that performs Breadth First Search (BFS) using a queue."""

	def __init__(self, start: Node):
		self.__queue = deque[State]()
		self.__queue.append(State(start))
		self.__visited: Set[Node] = set()

	def extract(self) -> Optional[State]:
		return self.__queue.popleft() if self.__queue else None

	def insert(self, state: State):
		if state.node not in self.__visited:
			self.__visited.add(state.node)
			self.__queue.append(state)

	def __len__(self) -> int:
		return len(self.__queue)