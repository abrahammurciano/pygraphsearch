from enum import Enum
from typing import Any, Dict, Type
from .AStarFrontier import AStarFrontier
from .BreadthFirstFrontier import BreadthFirstFrontier
from .DepthFirstFrontier import DepthFirstFrontier
from .DijkstraFrontier import DijkstraFrontier
from .Edge import TData, TNode
from .Frontier import Frontier
from .IterativeDeepeningFrontier import IterativeDeepeningFrontier
from .Node import Node

frontiers: Dict[str, Type] = {
	"BREADTH_FIRST_SEARCH": BreadthFirstFrontier[TNode, TData],
	"DEPTH_FIRST_SEARCH": DepthFirstFrontier[TNode, TData],
	"ITERATIVE_DEEPENING": IterativeDeepeningFrontier[TNode, TData],
	"DIJKSTRA": DijkstraFrontier[TNode, TData],
	"A_STAR": AStarFrontier[TNode, TData],
}


class Algorithm(Enum):
	A_STAR = 1
	BREADTH_FIRST_SEARCH = 2
	DEPTH_FIRST_SEARCH = 3
	DIJKSTRA = 4
	ITERATIVE_DEEPENING = 5

	def new_frontier(
		self, start: Node[TNode, TData], *options: Any
	) -> Frontier[TNode, TData]:
		"""Construct and return a frontier for this algorithm.

		Args:
			Generic (TNode): The type of the nodes of the graph.
			Generic (TData): The type of the data stored by the edges of the graph.
			start (Node[TNode, TData]): The start node for the search.
			*options (Any): Options to be passed to frontier constructor

		Returns:
			Frontier[TNode, TData]: A frontier for the search capable of containing nodes of type TNode with edges capable of containing data of type TData.
		"""
		return frontiers[self.name](start, *options)