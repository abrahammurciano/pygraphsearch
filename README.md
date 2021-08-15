# pygraphsearch

## A python package to search graphs.

---

### 1. Installation

To install the package, run the following command.

```
pip install pygraphsearch
```

### 2. Usage

As an example on how to use this package, we will make a program that will solve sliding puzzles. The complete source code is in the folder (example)[example]. We will provide the program with some shuffled arrangement of tiles as the starting node, and we will tell it what the correct tile arrangement is as the target node.

We will also tell it how to move from one board to another.

#### 2.1 Node

This package includes a Node class which your nodes should inherit from. In our example, we will make a class `Board` that extends `Node`. This class will represent the layout of the tiles on the board at any given time.

To override `Node` we must override the function `neighbours`. This function should return edges to all the nodes reachable from the current node.

In a sliding puzzle, there are always up to four legal moves. The empty tile can move up, down, left, or right, unless it's on an edge of the board in which case it can't move past the edge. We can make an enum called [Move](example/Move.py) to store these four options.

To check if a move is legal, we can create a method `can_move`. If we are able to move in a direction, then we call the board's `move` method which will return a copy of the board but with the given move applied.

The important thing here is that we define the function `neighbours` which returns some edges.

**Note**: Your node objects must also implement `__hash__` and `__eq__`.

```py
from pygraphsearch import Node, Edge
from typing import Iterable # it's always good to specify types
from .Move import Move

class Board(Node):

	# ...

	def neighbours(self) -> Iterable[Edge]:
		return [
			Edge(self, self.move(move), move)
			for move in Move
			if self.can_move(move)
		]

	def __eq__(self, board: object) -> bool:
		return isinstance(board, Board) and self.__tiles == board.__tiles

	def __hash__(self) -> int:
		return hash(tuple(self.__tiles))
```

#### 2.2 Edges

As we saw in the previous section, the `neighbours` method has to return an `Edge`. This class is defined in this package and can be constructed py passing it two nodes and some optional data. The data, if passed, is used to convert an edge into a string for convenience, but otherwise not used by the search package.

In our example it will be useful to store the direction that the empty tile is moved in an edge, as it will allow us to reconstruct the solution later.

#### 2.3 Basic Usage

Now that we have our nodes, we will write a basic program that will request a puzzle from the user and attempt to solve it using the `search` function provided by this package.

To get the puzzle size and initial board layout, we'll make the following function.

```py
def get_board_details() -> Tuple[int, List[int]]:
	# get board size
	size = int(
		input("Enter the size of the sliding puzzle. (e.g. for a 3x3 puzzle enter 3): ")
	)
	print(
		f"Enter {size * size} tile values row by row from top left to bottom right."
		" (Use 0 for the empty tile)"
	)
	# get list of size * size integer inputs from user
	tiles = [int(input()) for _ in range(size * size)]

	return size, tiles
```

Then we'll use the following code to perform the search.

```py
# Get board details from the user
size, tiles = get_board_details()

# Construct the initial node
start_board = Board(size, tiles)

# Construct the target node, eg a board with the tiles in order: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
target = Board(size, range(size * size))

# Create a frontier with custom parameters
frontier = IterativeDeepeningFrontier(start_board, initial_depth=2, depth_step=2)

# Call the search function with our frontier and with a lambda to tell it that a node is a target if it is equal to `target`
state1 = search(frontier, lambda node: node == target)

# Or simply call the function with the default options for one of the predefined algorithms
state2 = search(
	start_board, lambda node: node == target, Algorithm.DepthFirstSearch
)
```

As you can see, there are two ways to call the search function. The simplest way is to provide it with:

-   a start node,
-   a function which takes a node and returns true if the node is a target node or false otherwise, and
-   which algorithm to use.

The other way to call the search function is to provide it with:

-   a frontier (more on that in the next section) and
-   a function which takes a node and returns true if the node is a target node or false otherwise.

#### 2.4 Frontiers

A frontier is the heart of the search algorithm. It is a data structure which holds the furthest nodes we have explored and it determines the order in which we will explore them further.

For BFS, the frontier would be a FIFO queue. For DFS, it would be a LIFO stack.

If you want to implement your own search algorithms, all you need is to implement a frontier to pass to the `search` function by extending the abstract `Frontier` class provided by this package and implementing the abstract methods. These are:

-   `insert(self, state: State)` to insert states into the stack,
-   `extract(self) -> Optional[State]` to extract states from the stack, and
-   `__len__(self) -> int` which is the number of states stored in the frontier. The only important thing to be aware of about this function is that it should return 0 only when there are no more states to extract. If for some reason you can't or don't want to conform to this, you'll have to override `is_empty` to return true only when there are no more states to extract, and the search is done.

#### 2.5 State

The search function returns a state object. This object has two properties.

-   `node (Node)`: The target node. In our example this would be the state of the solved board.
-   `path (List[Edge])`: A list of the edges that lead from the start to the target node.

Using these, we can print the moves to solve the puzzle to the user, like so (continuing from the previous code):

```py
if state1 is not None:
	for edge in state1.path:
		print(edge.data, end=" ")
```

Here we're using edge.data which we set before by passing the moves to the `Edge` constructor in the `Board` class. By accessing the edges' data, we can retrieve the moves that were taken by the search algorithm to reach the solved state and print it back to the user.
