from enum import Enum
from typing import Any, Dict, Type
from .frontiers.a_star_frontier import AStarFrontier
from .frontiers.breadth_first_frontier import BreadthFirstFrontier
from .frontiers.depth_first_frontier import DepthFirstFrontier
from .frontiers.dijkstra_frontier import DijkstraFrontier
from .edge import TNode
from .frontier import Frontier
from .frontiers.iterative_deepening_frontier import IterativeDeepeningFrontier
from .node import Node

frontiers: Dict[str, Type] = {
    "BREADTH_FIRST_SEARCH": BreadthFirstFrontier[TNode],
    "DEPTH_FIRST_SEARCH": DepthFirstFrontier[TNode],
    "ITERATIVE_DEEPENING": IterativeDeepeningFrontier[TNode],
    "DIJKSTRA": DijkstraFrontier[TNode],
    "A_STAR": AStarFrontier[TNode],
}


class Algorithm(Enum):
    A_STAR = 1
    BREADTH_FIRST_SEARCH = 2
    DEPTH_FIRST_SEARCH = 3
    DIJKSTRA = 4
    ITERATIVE_DEEPENING = 5

    def new_frontier(self, start: Node, *options: Any) -> Frontier[TNode]:
        """Construct and return a frontier for this algorithm.

        Args:
            Generic (TNode): The type of the nodes of the graph.
            start (Node[TNode]): The start node for the search.
            *options (Any): Options to be passed to frontier constructor

        Returns:
            Frontier[TNode]: A frontier for the search capable of containing nodes of type TNode with edges capable of containing data of type .
        """
        return frontiers[self.name](start, *options)
