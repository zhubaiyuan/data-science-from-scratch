import math


def tanh(x: float) -> float:
    # If x is very large or very small, tanh is (essentially) 1 or -1.
    # We check for this because e.g. math.exp(1000) raises an error.
    if x < -100:
        return -1
    elif x > 100:
        return 1

    em2x = math.exp(-2 * x)
    return (1 - em2x) / (1 + em2x)
