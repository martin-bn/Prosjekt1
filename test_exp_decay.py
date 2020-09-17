from exp_decay import ExponentialDecay
import pytest

def test_exp_decay():
    a = 0.4
    u = 3.2
    E = ExponentialDecay(a)
    value = E(1, u)
    delta = 10e6
    assert value - (-1.28) < delta