#!/bin/env python3
from math import pi, sin
from time import time
import matplotlib.pyplot as plt

from derivative import Derivative
from integral import Integral


def main():
    start = time()
    f = lambda x: x * sin(x)
    i: Integral = Integral(f)
    d: Derivative = Derivative(f)
    d2: Derivative = Derivative(d.calculate)
    sample_frequency = 10
    start = 0
    end = 200
    xs: list[float] = list(
        map(
            lambda x: x / sample_frequency,
            range(int(start * sample_frequency), int(end * sample_frequency)),
        )
    )

    ys1: list[float] = []
    ys2: list[float] = []
    ys3: list[float] = []
    ys4: list[float] = []

    for x in xs:
        v = i.calculate(x)
        if v is not None:
            ys1.append(v)
        v2 = d.calculate(x)
        ys2.append(v2)
        v3 = f(x)
        ys3.append(v3)
        v4 = d2.calculate(x)
        ys4.append(v4)

    graph = plt.plot(xs, ys1)
    graph2 = plt.plot(xs, ys2)
    graph3 = plt.plot(xs, ys3)
    graph3 = plt.plot(xs, ys4)
    plt.legend(["integral", "derivative", "f", "d^2"])
    plt.grid(True)
    plt.show()


if __name__ == "__main__":
    main()
