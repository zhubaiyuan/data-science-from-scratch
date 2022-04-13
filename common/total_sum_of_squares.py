from common.de_mean import de_mean
from common.vector_type import Vector


def total_sum_of_squares(y: Vector) -> float:
    """the total squared variation of y_i's from their mean"""
    return sum(v ** 2 for v in de_mean(y))
