from typing import List

import pytest

from .SimpleNode import SimpleNode
from pygraphsearch import search, DijkstraFrontier


class DijkstraTest:
	@pytest.fixture
	def nodes(self) -> List[SimpleNode]:
		nodes = [SimpleNode(str(i)) for i in range(6)]
		nodes[0].connect(nodes[5], 5)
		nodes[0].connect(nodes[1], 1)
		nodes[1].connect(nodes[5], 3)
		nodes[1].connect(nodes[2], 1)
		nodes[2].connect(nodes[3], 1)
		nodes[2].connect(nodes[5], 1)
		nodes[3].connect(nodes[4], 1)
		nodes[4].connect(nodes[5], 1)
		return nodes

	def test_Dijkstra(self, nodes: List[SimpleNode]):
		dijkstra_frontier = DijkstraFrontier[SimpleNode, str](nodes[0])
		state = search(dijkstra_frontier, lambda node: node == nodes[5])
		assert state is not None
		assert state.node == nodes[5]
		assert state.path.nodes == [nodes[0], nodes[1], nodes[2], nodes[5]]
