import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt

class Pendulum():
    def __init__(self, theta, omega, L=1, M=1):
        self._theta = theta
        self._omega = omega
        self.L = L
        self.M = M
        self.g = 9.81

    def __call__(self, t, y):
        Y = [
            self._omega, 
            abs( -(self.g/self.L) *  np.sin(self._theta) )
            ]
        return Y
    
    def solve(self, y0, T, dt):
        self._answer = solve_ivp(self.__call__, [0, T], (y0), t_eval=np.linspace(0, T, dt))
        #return self._answer.t, self._answer.y

    @property
    def t(self):
        return self._answer.t
    @property
    def theta(self):
        return self._answer.y[0]
    @property
    def omega(self):
        return self._answer.y[1]

    



if __name__ == '__main__':
    E = Pendulum(np.pi/6, 0.15, L=2.7)
    A = E(1, 1)
    E.solve((0, 0), 10, 100)
    B = E.omega
    print(B)
    
    #plt.plot(E.t, E.theta)
    #plt.plot(E.t, E.omega)
    #plt.show()

    #E = Pendulum(theta=np.pi/6, omega=0.15, L=2.7 )
    #E.solve([0, 0], 10, 10)
    #A = E(1, 1)
    #print(A)
    #print(E.omega)
    #t, theta, omega = E.solve([0, 0.30], 10, 100)
    #print(u[0])
