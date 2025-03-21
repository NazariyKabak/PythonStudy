class Multiplier:
    def __init__(self, factors):
        self.factors = factors

    def __call__(self, x):
        return x * self.factors