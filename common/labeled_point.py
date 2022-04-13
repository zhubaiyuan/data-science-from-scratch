from typing import List, NamedTuple

from common.distance import distance
from common.majority_vote import majority_vote
from common.vector_type import Vector


class LabeledPoint(NamedTuple):
    point: Vector
    label: str


def knn_classify(k: int,
                 labeled_points: List[LabeledPoint],
                 new_point: Vector) -> str:
    # Order the labeled points from nearest to farthest.
    by_distance = sorted(labeled_points,
                         key=lambda lp: distance(lp.point, new_point))
    # Find the labels for the k closest
    k_nearest_labels = [lp.label for lp in by_distance[:k]]
    # and let them vote.
    return majority_vote(k_nearest_labels)
