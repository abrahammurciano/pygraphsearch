from typing import Any, Callable, Generic, Iterable, List, Tuple, TypeVar
import heapq
import deprecation

T = TypeVar("T")


class Heap(Generic[T]):
	"""A heap (aka priority queue) data structure.

	Args:
		Generic (T): The type of the elements in the heap.
	"""

	def __init__(
		self, items: Iterable[T] = None, key: Callable[[T], Any] = lambda _: _
	):
		"""Construct a heap data structure.

		Args:
			items (Iterable[T], optional): The items to initialize the heap with. If omitted will create an empty heap.
			key (Callable[[T], Any], optional): A function to be used to determine the priority of the elements in the heap. It should take an element of type T and return some comparable object (e.g. an integer) which represents the priority. Lower priorities are extracted first. If no priority function is provided, then the inserted objects themselves are used and a min-heap is created.
		"""
		self.__heap_key = key
		self.__heap_index = -1
		self.__heap_list = [self.__heap_node(item) for item in (items or [])]
		heapq.heapify(self.__heap_list)

	def push(self, item: T, key: Any = None):
		"""Insert a new item into the heap.

		Args:
			item (T): The item to insert.
			key (Any, optional): Override the key returned by the `key` function provided in the constructor.
		"""
		heapq.heappush(self.__heap_list, self.__heap_node(item, key))

	def pop(self) -> T:
		"""Extrace an item from the heap.

		Returns:
			T: The item extracted from the heap.

		Raises:
			IndexError: If there are no more items in the heap.
		"""
		return heapq.heappop(self.__heap_list)[-1]

	@deprecation.deprecated("0.0.2", details="Use len(heap) instead.")
	def size(self) -> int:
		"""Get the number of items in the heap.

		Returns:
			int: The number of items in the heap.
		"""
		return len(self)

	def items(self) -> List[T]:
		"""Get the items in the heap.

		Returns:
			List[T]: The items in the heap.
		"""
		return [node[-1] for node in self.__heap_list]

	def show(self):
		"""Print the items in the heap."""
		print(*self.items())

	def peek(self) -> T:
		"""Get the first item from the heap without extracting it.

		Returns:
			T: The first item in the heap.

		Raises:
			IndexError: If the heap is empty.
		"""
		return self.__heap_list[0][-1]

	def __len__(self):
		return len(self.__heap_list)

	def __bool__(self):
		return bool(self.__heap_list)

	def __heap_node(self, item: T, key: Any = None) -> Tuple[Any, int, T]:
		"""Create a comparable tuple that can be inserted into the heap's list.

		Args:
			item (T): The item to be inserted.
			key (Any, optional): Override the key returned by the `key` function provided in the constructor.

		Returns:
			Tuple[Any, int, T]: The tuple that can be inserted into the heap's list.
		"""
		self.__heap_index += 1
		return (self.__heap_key(item) if key is None else key, self.__heap_index, item)


if __name__ == "__main__":
	print("Nothing to Show")
