from typing import List, Tuple

from common.standard_deviation import standard_deviation
from common.vector_mean import vector_mean
from common.vector_type import Vector


def scale(data: List[Vector]) -> Tuple[Vector, Vector]:
    """returns the means and standard deviations for each position"""
    dim = len(data[0])
    means = vector_mean(data)
    stdevs = [standard_deviation([vector[i] for vector in data])
              for i in range(dim)]
    return means, stdevs
