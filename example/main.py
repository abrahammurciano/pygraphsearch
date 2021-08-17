from typing import List, Tuple
from pygraphsearch.Algorithm import Algorithm
from pygraphsearch.IterativeDeepeningFrontier import IterativeDeepeningFrontier
from pygraphsearch import search
from example.Board import Board
from example.Move import Move


def get_board_details() -> Tuple[int, List[int]]:
	size = int(
		input("Enter the size of the sliding puzzle. (e.g. for a 3x3 puzzle enter 3): ")
	)
	print(
		f"Enter {size * size} tile values row by row from top left to bottom right."
		" (Use 0 for the empty tile)"
	)
	tiles = [int(input()) for _ in range(size * size)]
	return size, tiles


if __name__ == "__main__":

	# Get board details from the user
	size, tiles = get_board_details()

	# Construct the initial node
	start_board = Board(size, tiles)

	# Construct the target node, eg a board with the tiles in order: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
	target = Board(size, range(size * size))

	# Create a frontier with custom parameters
	frontier = IterativeDeepeningFrontier[Board, Move](
		start_board, initial_depth=2, depth_step=2
	)

	# Call the search function with our frontier and with a lambda to tell it that a node is a target if it is equal to `target`
	state1 = search(frontier, lambda node: node == target)

	# Or simply call the function with the default options for one of the predefined algorithms
	state2 = search(
		start_board, lambda node: node == target, Algorithm.BreadthFirstSearch
	)

	if state2 is not None:
		for edge in state2.path:
			print(edge.data, end=" ")
