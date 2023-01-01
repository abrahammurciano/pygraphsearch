from typing import Generic, TypeVar, TYPE_CHECKING

if TYPE_CHECKING:
    from .node import Node

TNode = TypeVar("TNode", bound="Node")


class Edge(Generic[TNode]):
    """Represents a way to reach one node from another.

    Args:
        Generic (TNode): The type of the nodes of the graph.
    """

    def __init__(self, node_a: TNode, node_b: TNode, weight: int = 1):
        """Construct a node.

        Args:
            node_a (TNode): One of the endpoints of the edge
            node_b (TNode): The other endpoint of the edge.
            data (, optional): Data to be stored by the node. Defaults to None.
            weight (int): Weight of the edge. Defaults to 1.
        """
        self.__node_a = node_a
        self.__node_b = node_b
        self.__weight = weight

    @property
    def node_a(self) -> TNode:
        """The first node of the edge."""
        return self.__node_a

    @property
    def node_b(self) -> TNode:
        """The second node of the edge."""
        return self.__node_b

    @property
    def weight(self) -> int:
        return self.__weight

    @property
    def __nodes_set(self) -> set[TNode]:
        """A set of the two nodes in this edge."""
        return {self.node_a, self.node_b}

    def __eq__(self, other):
        return isinstance(other, Edge) and self.__nodes_set == other.__nodes_set

    def __hash__(self) -> int:
        return hash(self.node_a) + hash(self.node_b)

    def __str__(self) -> str:
        return str(self.__nodes_set)

    def __repr__(self) -> str:
        return f"Edge({self.node_a}, {self.node_b}, weight={self.weight})"
