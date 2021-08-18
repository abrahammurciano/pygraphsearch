from unittest import TestCase

from .SimpleNode import SimpleNode
from pygraphsearch import search, DijkstraFrontier


class DijkstraTest(TestCase):
	def setUp(self):
		nodes = [SimpleNode(str(i)) for i in range(6)]
		nodes[0].connect(nodes[5], 5)
		nodes[0].connect(nodes[1], 1)
		nodes[1].connect(nodes[5], 3)
		nodes[1].connect(nodes[2], 1)
		nodes[2].connect(nodes[3], 1)
		nodes[2].connect(nodes[5], 1)
		nodes[3].connect(nodes[4], 1)
		nodes[4].connect(nodes[5], 1)
		self.nodes = nodes

	def test_Dijkstra(self):
		Dijkstra_frontier = DijkstraFrontier[SimpleNode, str](self.nodes[0])
		state = search(Dijkstra_frontier, lambda node: node == self.nodes[5])
		self.assertEqual(state.node, self.nodes[5])
		self.assertEqual(
			state.path.nodes,
			[self.nodes[0], self.nodes[1], self.nodes[2], self.nodes[5]],
		)
