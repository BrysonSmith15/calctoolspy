from time import time
from typing import Callable


class Derivative:
    last_calculate: float
    last_value: float
    func: Callable[[float], float]

    def __init__(self, f: Callable[[float], float]) -> None:
        self.func = f
        self.last_value = 0
        self.last_calculate = f(0)
        _ = self.calculate(0)

    def calculate(self, x: float | None = None) -> float:
        t = x if x is not None else time()
        # print(t, self.last_calculate)
        try:
            out = ((v := self.func(t)) - self.last_value) / (t - self.last_calculate)
        except ZeroDivisionError:
            try:
                return self.calculate(t + 0.01 if x is not None else None)
            except RecursionError:
                return 10
        self.last_value = v
        self.last_calculate = t

        return out
