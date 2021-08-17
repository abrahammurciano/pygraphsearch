from enum import Enum
from .Frontier import Frontier
from .IterativeDeepeningFrontier import IterativeDeepeningFrontier
from .DepthFirstFrontier import DepthFirstFrontier
from .BreadthFirstFrontier import BreadthFirstFrontier
from . import TypeVars as T

frontiers = {
	"BreadthFirstSearch": lambda start_node: BreadthFirstFrontier[T.Node, T.Data](
		start_node
	),
	"DepthFirstSearch": lambda start_node: DepthFirstFrontier[T.Node, T.Data](
		start_node
	),
	"IterativeDeepeningSearch": lambda start_node: IterativeDeepeningFrontier[
		T.Node, T.Data
	](start_node),
}


class Algorithm(Enum):
	DepthFirstSearch = 1
	BreadthFirstSearch = 2
	IterativeDeepeningSearch = 3

	def new_frontier(self, start: T.Node) -> Frontier[T.Node, T.Data]:
		"""Construct and return a frontier for this algorithm.

		Args:
			Generic (T.Node): The type of the nodes of the graph.
			Generic (T.Data): The type of the data stored by the edges of the graph.
			start (T.Node): The start node for the search.

		Returns:
			Frontier[T.Node, T.Data]: A frontier for the search capable of containing nodes of type T.Node with edges capable of containing data of type T.Data.
		"""
		return frontiers[self.name](start)