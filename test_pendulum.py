from pendulum import Pendulum
import numpy as np
import pytest


@pytest.mark.parametrize("arg, expected", [ [(0, 0), [0, 0]] ])
def test_pendulum_one(arg, expected):
    A = Pendulum(arg[0], arg[1])
    E = A(0, 0)
    assert E == expected

@pytest.mark.parametrize("arg, expected", [[(np.pi/6, 0.15, 2.7), [0.15, 1.8166]]])
def test_pendulum_two(arg, expected):
    A = Pendulum(arg[0], arg[1], arg[2])
    E = A(0, 0)
    tol = [1e-40, 1e-40]
    assert [abs(E[0] - expected[0]), abs(E[1]- expected[1])] <= tol

