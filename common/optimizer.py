from common.layer import Layer


class Optimizer:
    """
    An optimizer updates the weights of a layer (in place) using information
    known by either the layer or the optimizer (or by both).
    """

    def step(self, layer: Layer) -> None:
        raise NotImplementedError
