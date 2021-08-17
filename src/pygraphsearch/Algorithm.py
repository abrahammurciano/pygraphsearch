from enum import Enum
from .Frontier import Frontier
from .IterativeDeepeningFrontier import IterativeDeepeningFrontier
from .DepthFirstFrontier import DepthFirstFrontier
from .BreadthFirstFrontier import BreadthFirstFrontier
from .Node import Node, TNode
from .Edge import TData

frontiers = {
	"BreadthFirstSearch": lambda start_node: BreadthFirstFrontier[TNode, TData](
		start_node
	),
	"DepthFirstSearch": lambda start_node: DepthFirstFrontier[TNode, TData](start_node),
	"IterativeDeepeningSearch": lambda start_node: IterativeDeepeningFrontier[
		TNode, TData
	](start_node),
}


class Algorithm(Enum):
	DepthFirstSearch = 1
	BreadthFirstSearch = 2
	IterativeDeepeningSearch = 3

	def new_frontier(self, start: Node[TNode, TData]) -> Frontier[TNode, TData]:
		"""Construct and return a frontier for this algorithm.

		Args:
			Generic (TNode): The type of the nodes of the graph.
			Generic (TData): The type of the data stored by the edges of the graph.
			start (Node[TNode, TData] The start node for the search.

		Returns:
			Frontier[TNode, TData]: A frontier for the search capable of containing nodes of type TNode with edges capable of containing data of type TData.
		"""
		return frontiers[self.name](start)