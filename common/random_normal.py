import random

from common.inverse_normal_cdf import inverse_normal_cdf


def random_normal() -> float:
    """Returns a random draw from a standard normal distribution"""
    return inverse_normal_cdf(random.random())
