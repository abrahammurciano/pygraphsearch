from abc import ABC, abstractmethod
from typing import Generic, Optional, Sized, TypeVar
from .state import State
from .node import Node


TNode = TypeVar("TNode", bound="Node")


class Frontier(ABC, Sized, Generic[TNode]):
    """A data structure which holds the furthest nodes we have explored and it determines the order in which we will explore them further.

    Args:
        Generic (TNode): The type of the nodes of the graph.

    To implement your own frontier, you must subclass this class and implement the following methods:
    - `extract(self) -> Optional[State]` to extract the next state from the frontier.
    - `insert(self, state: State) -> Optional[State]` to insert a state into the frontier.
    """

    def is_empty(self) -> bool:
        """Check if the frontier has more states to extract.

        Returns:
            bool: True if the frontier is empty, false otherwise.
        """
        return len(self) == 0

    @abstractmethod
    def extract(self) -> Optional[State[TNode]]:
        """Extract a state to expand from the frontier.

        Returns:
            State: The state to expand, or None if the frontier is empty.
        """
        pass

    @abstractmethod
    def insert(self, state: State[TNode]):
        """Insert a state into the frontier.

        Args:
            state (State): The state to insert.
        """
        pass

    def __bool__(self) -> bool:
        return not self.is_empty()
