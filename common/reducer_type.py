from typing import Iterable, Callable, Any, Tuple

# A key-value pair is just a 2-tuple
KV = Tuple[Any, Any]

# A Reducer is a function that takes a key and an iterable of values
# and returns a key-value pair
Reducer = Callable[[Any, Iterable], KV]
