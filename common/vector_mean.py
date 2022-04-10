from typing import List

from common.scalar_multiply import scalar_multiply
from common.vector_sum import vector_sum
from common.vector_type import Vector


def vector_mean(vectors: List[Vector]) -> Vector:
    """Computes the element-wise average"""
    n = len(vectors)
    return scalar_multiply(1/n, vector_sum(vectors))


assert vector_mean([[1, 2], [3, 4], [5, 6]]) == [3, 4]
