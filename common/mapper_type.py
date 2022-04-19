from typing import Callable, Iterable

from common.kv_type import KV

# A Mapper is a function that returns an Iterable of key-value pairs
Mapper = Callable[..., Iterable[KV]]
