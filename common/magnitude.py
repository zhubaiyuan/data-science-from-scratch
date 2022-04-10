import math

from common.sum_of_squares import sum_of_squares
from common.vector_type import Vector


def magnitude(v: Vector) -> float:
    """Returns the magnitude (or length) of v"""
    return math.sqrt(sum_of_squares(v))   # math.sqrt is square root function
