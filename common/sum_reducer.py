from typing import Callable, Iterable

from common.kv_type import KV
from common.reducer_type import Reducer


def values_reducer(values_fn: Callable) -> Reducer:
    """Return a reducer that just applies values_fn to its values"""
    def reduce(key, values: Iterable) -> KV:
        return (key, values_fn(values))

    return reduce


sum_reducer = values_reducer(sum)
