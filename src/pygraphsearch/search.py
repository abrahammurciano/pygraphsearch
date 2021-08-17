from typing import Callable, Optional, Union, overload
from . import TypeVars as T
from .Algorithm import Algorithm
from .State import State
from .Frontier import Frontier
from .Node import Node


@overload
def search(
	frontier: Frontier[T.Node, T.Data], is_target: Callable[[T.Node], bool], /
) -> Optional[State]:
	"""Search for the path to a target.

	Args:
		frontier (Frontier): An object derived from Frontier. It should contain only the start state and will be modified by this function.
		is_target (Callable[[T.Node], bool]): A predicate which tells us if a node is a target.

	Returns:
		Optional[State]: The target state, or None if none exists.
	"""
	...


@overload
def search(
	start: T.Node, is_target: Callable[[T.Node], bool], algorithm: Algorithm, /
) -> Optional[State]:
	"""Search for the path to a target

	Args:
		start (T.Node): The node to start the search from.
		is_target (Callable[[T.Node], bool]): A predicate which tells us if a node is a target.
		algorithm (Algorithm): The algorithm you want to use for the search.

	Returns:
		Optional[State]: The target state, or None if none exists.
	"""
	...


def search(
	arg1: Union[Frontier[T.Node, T.Data], T.Node],
	arg2: Callable[[T.Node], bool],
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

	raise TypeError("The first argument must be an instance of Node or Frontier")