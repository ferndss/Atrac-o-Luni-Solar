import const
import numpy as np


def semE(r: float = None, p: float = None, e: float = None, u: float = None, E: float = None, T: float = None):
    if E is not None:
        return - const.mi/2*E
    elif r is not None:
        return r/(1 - e*np.cos(u))
    elif p is not None:
        return p/(1 - e**2)
    elif T is not None:
        return const.mi*T/4*np.pi**2


def vel(e, a, r, E):
    if e == 0:
        return np.sqrt(const.mi/r)
    if E is not None:
        return np.sqrt(2*((const.mi/r) + E))
    if a is not None:
        return np.sqrt(const.mi*((2/r)+(1/a)))


def tax_A(a=None, b=None, h=None, m=None, r=None, v=None, T=None):
    if T is not None:
        return np.pi*a*b/T
    if h is not None:
        return h/2*m
    if r is not None:
        return 0.5*np.cross(r, v)


if __name__ == '__main__':
    print('semieixo maior: ', tax_A(a=7000))
