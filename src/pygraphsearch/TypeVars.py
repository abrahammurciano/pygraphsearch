from typing import TypeVar, TYPE_CHECKING

if TYPE_CHECKING:
	from .Node import Node as AbstractNode


Node = TypeVar("Node", bound="AbstractNode")
Data = TypeVar("Data")