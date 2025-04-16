from time import time
from typing import Callable


class Integral:
    last_calculate: float | None
    func: Callable[[float], float]
    acc: float

    def __init__(self, f: Callable[[float], float]) -> None:
        self.func = f
        self.last_calculate = None
        self.acc = 0
        _ = self.calculate(0)

    def calculate(self, x: float | None = None) -> float | None:
        if self.last_calculate is not None:
            t = x if x is not None else time()
            # print(t, self.last_calculate)
            try:
                self.acc += self.func(t) * (t - self.last_calculate)
            except ZeroDivisionError:
                try:
                    return self.calculate(t + 0.01 if x is not None else None)
                except RecursionError:
                    return 10
            self.last_calculate = t

            return self.acc
        else:
            self.last_calculate = x if x is not None else time()
            return 1
