import imp
from common.add import add
from common.ridge_penalty_gradient import ridge_penalty_gradient
from common.sqerror_gradient import sqerror_gradient
from common.vector_type import Vector


def sqerror_ridge_gradient(x: Vector,
                           y: float,
                           beta: Vector,
                           alpha: float) -> Vector:
    """
    the gradient corresponding to the ith squared error term
    including the ridge penalty
    """
    return add(sqerror_gradient(x, y, beta),
               ridge_penalty_gradient(beta, alpha))
