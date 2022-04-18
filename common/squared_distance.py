from common.subtract import subtract
from common.sum_of_squares import sum_of_squares
from common.vector_type import Vector


def squared_distance(v: Vector, w: Vector) -> float:
    """Computes (v_1 - w_1) ** 2 + ... + (v_n - w_n) ** 2"""
    return sum_of_squares(subtract(v, w))
