from typing import Generic, Optional, Set
from .Edge import TData, TNode
from .Frontier import Frontier
from .Stack import Stack
from .State import State


class DepthFirstFrontier(Generic[TNode, TData], Frontier[TNode, TData]):
	"""A frontier for a graph search algorithm that performs Depth First Search (DFS) using a stack.

	Args:
		Generic (TNode): The type of the nodes of the graph.
		Generic (TData): The type of the data stored by the edges of the graph.
	"""

	def __init__(self, start: TNode):
		self.__stack = Stack[State[TNode, TData]]()
		self.__stack.push(State(start))
		self.__visited: Set[TNode] = set()

	def extract(self) -> Optional[State[TNode, TData]]:
		return None if self.__stack.is_empty() else self.__stack.pop()

	def insert(self, state: State[TNode, TData]):
		if state.node not in self.__visited:
			self.__visited.add(state.node)
			self.__stack.push(state)

	def __len__(self) -> int:
		return len(self.__stack)