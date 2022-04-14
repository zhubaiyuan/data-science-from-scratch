from common.predict import predict
from common.vector_type import Vector


def error(x: Vector, y: float, beta: Vector) -> float:
    return predict(x, beta) - y
