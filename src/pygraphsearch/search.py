from typing import Callable, Optional, Union, overload
from .Algorithm import Algorithm
from .Node import Node
from .State import State
from .Frontier import Frontier


@overload
def search(frontier: Frontier, is_target: Callable[[Node], bool], /) -> Optional[State]:
	"""Search for the path to a target.

	Args:
		frontier (Frontier): An object derived from Frontier. It should contain only the start state and will be modified by this function.
		is_target (Callable[[Node], bool]): A predicate which tells us if a node is a target.

	Returns:
		Optional[State]: The target state, or None if none exists.
	"""
	...


@overload
def search(
	start: Node, is_target: Callable[[Node], bool], algorithm: Algorithm, /
) -> Optional[State]:
	"""Search for the path to a target

	Args:
		start (Node): The node to start the search from.
		is_target (Callable[[Node], bool]): A predicate which tells us if a node is a target.
		algorithm (Algorithm): The algorithm you want to use for the search.

	Returns:
		Optional[State]: The target state, or None if none exists.
	"""
	...


def search(
	arg1: Union[Frontier, Node],
	arg2: Callable[[Node], bool],
	arg3: Optional[Algorithm] = None,
	/,
) -> Optional[State]:
	is_target = arg2
	if isinstance(arg1, Frontier):
		frontier = arg1
		while not frontier.is_empty():
			state = frontier.extract()
			if state is None or is_target(state.node):
				return state
			for next_state in state.next_states():
				frontier.insert(next_state)
		return None

	elif isinstance(arg1, Node):
		start = arg1
		algorithm = arg3
		assert algorithm is not None
		return search(algorithm.new_frontier(start), is_target)