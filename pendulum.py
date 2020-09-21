import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt

class Pendulum():
    def __init__(self, L=1, M=1):
        self.L = L
        self.M = M
        self.g = 9.81

    def __call__(self, t, y):
        theta = y[0]
        omega = y[1]
        Y = [
            omega, 
            -(self.g/self.L) *  np.sin(theta) 
            ]
        return Y
    
    def solve(self, y0, T, dt):
        self._answer = solve_ivp(self.__call__, [0, T], (y0), t_eval=np.linspace(0, T, dt))

    @property
    def t(self):
        return self._answer.t
    @property
    def theta(self):
        return self._answer.y[0]
    @property
    def omega(self):
        return self._answer.y[1]


    @property 
    def x(self):
        return self.L * np.sin(self.theta)
    
    @property
    def y(self):
        return -self.L * np.cos(self.theta)

    @property
    def potential(self):
        P = self.M * self.g * ( np.array(self.y) + self.L )
        return P
    
    @property
    def vx(self):
        A = np.gradient(self.x, self.t)
        return A
    @property
    def vy(self):
        A = np.gradient(self.y, self.t)
        return A

    @property
    def kinetic(self):
        K = (1/2)*self.M*(self.vx**2+self.vy**2)
        return K
    


if __name__ == '__main__':
    E = Pendulum(L=2.7)

    E.solve((np.pi/6, 0.15), 10, 100)
    #print(E.theta)
    #B = E.omega

    #print(A)
    #for i in range(len(E.t)):
    #plt.plot(E.t, E.theta)
    #plt.plot(E.t, E.omega)
    #plt.show()
    #print(E.omega)
    #print(E.potential)

    #print(E.potential)
    plt.plot(E.t, E.potential)
    plt.plot(E.t, E.kinetic)
    plt.show()
