import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt

import scipy.integrate as integrate
import matplotlib.animation as animation


class DoublePendulum:
    def __init__(self, M1=1, L1=1, M2=1, L2=1, g=9.81):
        self.M1 = M1
        self.L1 = L1
        self.M2 = M2
        self.L2 = L2
        self.g = g

    def __call__(self, t, y):
        M1 = self.M1
        L1 = self.L1
        M2 = self.M2
        L2 = self.L2
        theta1 = y[0]
        theta2 = y[2]
        omega1 = y[1]
        omega2 = y[3]
        g = self.g

        self.delta_theta = theta2 - theta1
        delta_theta = self.delta_theta

        Y = [
            omega1,
            (((M2* L2 * (omega2 ** 2) * np.sin(delta_theta) * np.cos(delta_theta)) + 
            M2 * g * np.sin(theta2) * np.cos(delta_theta) + 
            M2 * L2 * (omega2 ** 2) * np.sin(delta_theta) - 
            (M1 + M2) * g * np.sin(theta1)) / 
            ((M1 + M2) * L1 - M2 * L1 * np.cos(delta_theta) ** 2)),
            
            omega2,
            ((-M2 * L2 * (omega2 ** 2) * np.sin(delta_theta) * np.cos(delta_theta) + 
            (M1 + M2) * g * np.sin(theta1) * np.cos(delta_theta) - 
            (M1 + M2) * L1 * (omega1 ** 2) * np.sin(delta_theta) -
            (M1 + M2) * g * np.sin(theta2)) / 
            ((M1 + M2) * L2 - M2 * L2 * (np.cos(delta_theta) ** 2)))
            ]
        return Y


    def solve(self, y0, T, dt, angles="rad"):
        self.dt = dt
        if angles == "deg":
            y0 = np.radians(y0)
        self._answer = solve_ivp(self.__call__, [0, T], (y0), t_eval=np.linspace(0, T, dt), method="Radau")

    @property
    def t(self):
        if hasattr(self, '_answer'):
            return self._answer.t
        else:
            raise AttributeError

    @property
    def theta1(self):
        if hasattr(self, '_answer'):
            return self._answer.y[0]
        else:
            raise AttributeError
    
    @property
    def theta2(self):
        if hasattr(self, '_answer'):
            return self._answer.y[2]
        else:
            raise AttributeError


    @property 
    def x1(self):
        return self.L1 * np.sin(self.theta1)
    
    @property
    def y1(self):
        return -self.L1 * np.cos(self.theta1)
    
    @property 
    def x2(self):
        return self.x1 + self.L2 * np.sin(self.theta2)
    
    @property 
    def y2(self):
        return self.y1 - self.L2 * np.cos(self.theta2)

    @property
    def potential(self):
        P1 = self.M1 * self.g * (self.y1 + self.L1)
        P2 = self.M2 * self.g * (self.y2 + self.L1 + self.L2)
        return P1 + P2

    @property
    def vx1(self):
        return np.gradient(self.x1, self.t)
    @property
    def vy1(self):
        return np.gradient(self.y1, self.t)
    @property
    def vx2(self):
        return np.gradient(self.x2, self.t)
    @property
    def vy2(self):
        return np.gradient(self.y2, self.t)

    @property
    def kinetic(self):
        K1 = (1/2)*self.M1*(self.vx1**2+self.vy1**2)
        K2 = (1/2)*self.M2*(self.vx2**2+self.vy2**2)
        return K1 + K2

    @property
    def total_energy(self):
        return self.potential + self.kinetic


    def create_animation(self):
        fig = plt.figure()

        plt.axis('equal')
        plt.axis('off')
        plt.axis((-3, 3, -3, 3))

        self.pendulums, = plt.plot([], [], 'o-', lw=2)
        
        self.animation = animation.FuncAnimation(fig,
                                                 self._next_frame,
                                                 frames=range(len(self.x1)), 
                                                 repeat=None,
                                                 interval=1000*self.dt, 
                                                 blit=True)
        
    def _next_frame(self, i):
        self.pendulums.set_data((0, self.x1[i], self.x2[i]),
                                (0, self.y1[i], self.y2[i]))
        return self.pendulums,

    def show_animation(self):
        plt.show()

    def save_animation(self, filename):
        self.animation.save(filename, fps=60)


if __name__ == '__main__':
    E = DoublePendulum()
    E.solve((np.pi/6, 0.15, np.pi/6, 0.15), 10, 100)
    plt.plot(E.t, E.kinetic)
    plt.plot(E.t, E.potential)
    plt.plot(E.t, E.total_energy)
    plt.show()

    E.create_animation()
    E._next_frame(60)
    E.save_animation("animasjon.png")
    