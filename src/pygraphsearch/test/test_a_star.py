from typing import Callable
from unittest import TestCase
from pygraphsearch import search, Algorithm
from .slidingpuzzle import Board


class TestAStar(TestCase):
	def setUp(self):
		self.size = 3
		self.start = Board(self.size, (1, 2, 5, 3, 7, 0, 6, 8, 4))
		self.target = Board(self.size, range(self.size * self.size))

	def manhattan_distance(self, board: Board, target: Board) -> int:
		"""Calculate the sum of the manhattan distances for each tile in `board` from its intended position in `target`.

		Args:
			board (Board): The board whose manhattan distances we seek.
			target (Board): The board with all the tiles in the correct position.

		Returns:
			int: The sum of the manhattan distances for each tile in `board`.
		"""

		def row_index(index: int) -> int:
			return index // board.size

		def column_index(index: int) -> int:
			return index % board.size

		def index_offset(
			actual_index: int, target_index: int, index_function: Callable[[int], int]
		) -> int:
			return index_function(actual_index) - index_function(target_index)

		def tile_manhattan_distance(actual_index: int, desired_index: int) -> int:
			return abs(index_offset(actual_index, desired_index, row_index)) + abs(
				index_offset(actual_index, desired_index, column_index)
			)

		return sum(
			tile_manhattan_distance(board.tiles.index(i), target.tiles.index(i))
			for i in range(board.size * board.size)
		)

	def test_a_star(self):
		state = search(
			self.start,
			lambda board: board == self.target,
			Algorithm.A_STAR,
			lambda state: self.manhattan_distance(state.node, self.target),
		)

		self.assertEqual(state.node, self.target)
		self.assertEqual(len(state.path), 7)
