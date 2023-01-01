from typing import Any, Callable, Optional, Union, overload, TypeVar
from .algorithm import Algorithm
from .node import Node
from .frontier import Frontier
from .node import Node
from .state import State


TNode = TypeVar("TNode", bound="Node")


@overload
def search(
    frontier: Frontier[TNode], is_target: Callable[[TNode], bool], /
) -> Optional[State[TNode]]:
    """Search for the path to a target.

    Args:
        frontier (Frontier): An object derived from Frontier. It should contain only the start state and will be modified by this function.
        is_target (Callable[[TNode], bool]): A predicate which tells us if a node is a target.

    Returns:
        Optional[State]: The target state, or None if none exists.
    """
    ...


@overload
def search(
    start: TNode,
    is_target: Callable[[TNode], bool],
    algorithm: Algorithm,
    /,
    *options: Any,
) -> Optional[State[TNode]]:
    """Search for the path to a target

    Args:
        start (Node[TNode] The node to start the search from.
        is_target (Callable[[TNode], bool]): A predicate which tells us if a node is a target.
        algorithm (Algorithm): The algorithm you want to use for the search.
        *options (Any): Additional options to pass to the algorithm's frontier constructor.

    Returns:
        Optional[State]: The target state, or None if none exists.
    """
    ...


def search(
    arg1: Union[Frontier[TNode], TNode],
    arg2: Callable[[TNode], bool],
    arg3: Optional[Algorithm] = None,
    /,
    *options,
) -> Optional[State[TNode]]:
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
        return search(algorithm.new_frontier(start, *options), is_target)

    raise TypeError("The first argument must be an instance of Node or Frontier")
