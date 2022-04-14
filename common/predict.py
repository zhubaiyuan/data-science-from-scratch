from common.dot import dot
from common.vector_type import Vector


def predict(x: Vector, beta: Vector) -> float:
    """assumes that the first element of x is 1"""
    return dot(x, beta)
