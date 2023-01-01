from abc import ABC, abstractmethod
from typing import Iterable, TypeVar, TYPE_CHECKING

if TYPE_CHECKING:
    from .edge import Edge


TNode = TypeVar("TNode", bound="Node")


class Node(ABC):
    """An abstract base class for a node in a graph.

    Args:
        Generic (TNode): The concrete type of the nodes in the graph.
    """

    @abstractmethod
    def neighbours(self: TNode) -> Iterable["Edge[TNode]"]:
        """Get the edges to all the nodes adjacent to this one.

        Returns:
            Iterable[Edge[TNode]]: The edges to all the nodes adjacent to this one.
        """
        pass
