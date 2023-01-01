from typing import Generic, Optional, Set, TypeVar
from typed_data_structures import Queue
from ..frontier import Frontier
from ..state import State
from ..node import Node


TNode = TypeVar("TNode", bound="Node")


class BreadthFirstFrontier(Generic[TNode], Frontier[TNode]):
    """A frontier for a graph search algorithm that performs Breadth First Search (BFS) using a queue.

    Args:
            Generic (TNode): The type of the nodes of the graph.
    """

    def __init__(self, start: TNode):
        self.__queue = Queue[State[TNode]]()
        self.__queue.append(State(start))
        self.__visited: Set[TNode] = set()

    def extract(self) -> Optional[State[TNode]]:
        return self.__queue.pop() if self.__queue else None

    def insert(self, state: State[TNode]):
        if state.node not in self.__visited:
            self.__visited.add(state.node)
            self.__queue.push(state)

    def __len__(self) -> int:
        return len(self.__queue)
