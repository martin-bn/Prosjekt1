from pendulum import Pendulum
import numpy as np
import unittest

class TestPendulum(unittest.TestCase):
    def test_pendulum_omega(self):
        E = Pendulum(L=2.7)
        value = E(1, [np.pi/6, 0.15])
        self.assertEqual(value[0], 0.15)

    def test_pendulum_theta(self):
        E = Pendulum(L=2.7)
        value = E(1, [np.pi/6, 0.15])
        self.assertAlmostEqual(value[1], -1.8166666666)

    def test_pendulum_zero(self):
        E = Pendulum()
        value = E(0, (0, 0))
        self.assertEqual(value, [0, 0])

    def test_pendulum_cartesian(self):
        E = Pendulum(L=2.7)
        E.solve((np.pi/6, 0.15), 10, 100)
        for i in range(len(E.x)):
            answer = (E.x[i]**2 + E.y[i]**2)
        self.assertAlmostEqual(E.L**2,  answer)



if __name__ == '__main__':
    unittest.main()
