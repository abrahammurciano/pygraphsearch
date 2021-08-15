from typing import Optional, Set
from .State import State
from .Frontier import Frontier
from .Node import Node
from .Stack import Stack


class DepthFirstFrontier(Frontier):
	"""A frontier for a graph search algorithm that performs Depth First Search (DFS) using a stack."""

	def __init__(self, start: Node):
		self.__stack = Stack[State]()
		self.__stack.push(State(start))
		self.__visited: Set[Node] = set()

	def extract(self) -> Optional[State]:
		return None if self.__stack.is_empty() else self.__stack.pop()

	def insert(self, state: State):
		if state.node not in self.__visited:
			self.__visited.add(state.node)
			self.__stack.push(state)

	def __len__(self) -> int:
		return len(self.__stack)