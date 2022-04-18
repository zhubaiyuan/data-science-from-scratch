import math


def sigmoid(t: float) -> float:
    return 1 / (1 + math.exp(-t))
