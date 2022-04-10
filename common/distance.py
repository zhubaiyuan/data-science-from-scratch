from common.magnitude import magnitude
from common.subtract import subtract
from common.vector_type import Vector


def distance(v: Vector, w: Vector) -> float:  # type: ignore
    return magnitude(subtract(v, w))
