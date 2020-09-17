import scipy as sc
from scipy.integrate import solve_ivp
import numpy as np
import matplotlib.pyplot as plt

#print(sc.__version__)
class ExponentialDecay():
    def __init__(self, a):
        self.a = a 
    
    def __call__(self, t, u):
        a = self.a
        dudt = -a*u
        return dudt
    
    def solve(self, u0, T, dt):
        answer = solve_ivp(self.__call__, [0, T], [u0,], t_eval=np.linspace(0, T, dt))
        return answer.t, answer.y[0]


u0 = 2
T = 10
dt = 100

E = ExponentialDecay(0.4)
#test = E(1, 3.2)
t, u = E.solve(u0, T, dt)
#print(u)
plt.plot(t, u)
plt.show()