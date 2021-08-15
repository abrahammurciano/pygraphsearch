from abc import ABC, abstractmethod
from typing import Optional, Sized
from .State import State


class Frontier(ABC, Sized):
	def is_empty(self) -> bool:
		"""Check if the frontier has more states to extract.

		Returns:
			bool: True if the frontier is empty, false otherwise.
		"""
		return len(self) == 0

	@abstractmethod
	def extract(self) -> Optional[State]:
		"""Extract a state to expand from the frontier.

		Returns:
			State: The state to expand, or None if the frontier is empty.
		"""
		pass

	@abstractmethod
	def insert(self, state: State):
		"""Insert a state into the frontier.

		Args:
			state (State): The state to insert.
		"""
		pass
