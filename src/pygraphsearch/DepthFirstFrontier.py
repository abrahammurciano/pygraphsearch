from typing import Generic, Optional, Set
from .State import State
from .Frontier import Frontier
from .Stack import Stack
from . import TypeVars as T


class DepthFirstFrontier(Generic[T.Node, T.Data], Frontier[T.Node, T.Data]):
	"""A frontier for a graph search algorithm that performs Depth First Search (DFS) using a stack.

	Args:
		Generic (T.Node): The type of the nodes of the graph.
		Generic (T.Data): The type of the data stored by the edges of the graph.
	"""

	def __init__(self, start: T.Node):
		self.__stack = Stack[State[T.Node, T.Data]]()
		self.__stack.push(State(start))
		self.__visited: Set[T.Node] = set()

	def extract(self) -> Optional[State[T.Node, T.Data]]:
		return None if self.__stack.is_empty() else self.__stack.pop()

	def insert(self, state: State[T.Node, T.Data]):
		if state.node not in self.__visited:
			self.__visited.add(state.node)
			self.__stack.push(state)

	def __len__(self) -> int:
		return len(self.__stack)