from common.vector_type import Vector
from common.magnitude import magnitude


def direction(w: Vector) -> Vector:
    mag = magnitude(w)
    return [w_i / mag for w_i in w]
