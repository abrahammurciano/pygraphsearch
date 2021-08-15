from typing import Optional
from .State import State
from .Frontier import Frontier
from .Node import Node
from .Stack import Stack


class DepthFirstFrontier(Frontier):
	"""A frontier for a graph search algorithm that performs Depth First Search (DFS) using a stack."""

	def __init__(self, start: Node):
		self.__stack = Stack[State]()
		self.__stack.push(State(start))

	def extract(self) -> Optional[State]:
		return None if self.__stack.is_empty() else self.__stack.pop()

	def insert(self, state: State):
		self.__stack.push(state)

	def __len__(self) -> int:
		return len(self.__stack)