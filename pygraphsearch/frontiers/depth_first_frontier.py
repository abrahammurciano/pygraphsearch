from typing import Generic, Optional, Set, TypeVar
from ..frontier import Frontier
from typed_data_structures import Stack
from ..state import State
from ..node import Node


TNode = TypeVar("TNode", bound="Node")


class DepthFirstFrontier(Generic[TNode], Frontier[TNode]):
    """A frontier for a graph search algorithm that performs Depth First Search (DFS) using a stack.

    Args:
        Generic (TNode): The type of the nodes of the graph.
    """

    def __init__(self, start: TNode):
        self.__stack = Stack[State[TNode]]()
        self.__stack.push(State(start))
        self.__visited: Set[TNode] = set()

    def extract(self) -> Optional[State[TNode]]:
        return None if self.__stack.is_empty() else self.__stack.pop()

    def insert(self, state: State[TNode]):
        if state.node not in self.__visited:
            self.__visited.add(state.node)
            self.__stack.push(state)

    def __len__(self) -> int:
        return len(self.__stack)
