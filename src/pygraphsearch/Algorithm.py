from enum import Enum
from typing import Callable

from pygraphsearch.Node import Node
from .Frontier import Frontier
from .IterativeDeepeningFrontier import IterativeDeepeningFrontier
from .DepthFirstFrontier import DepthFirstFrontier
from .BreadthFirstFrontier import BreadthFirstFrontier


class Algorithm(Enum):
	DepthFirstSearch = 1
	BreadthFirstSearch = 2
	IterativeDeepeningSearch = 3

	frontiers = {
		"BreadthFirstSearch": lambda start_node: BreadthFirstFrontier(start_node),
		"DepthFirstSearch": lambda start_node: DepthFirstFrontier(start_node),
		"IterativeDeepeningSearch": lambda start_node: IterativeDeepeningFrontier(
			start_node
		),
	}

	def new_frontier(self, start: Node) -> Frontier:
		return self.frontiers[self.name](start)