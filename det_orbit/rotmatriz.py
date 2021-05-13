import numpy as np


def rotX(angulo):
    co = np.cos(angulo)
    si = np.sin(angulo)
    return np.array([[1, 0, 0], 
                     [0, co, si], 
                     [0, -si, co]])


def rotY(angulo):
    co = np.cos(angulo)
    si = np.sin(angulo)

    return np.array([[co, 0, si], 
                     [0, 1, 0], 
                     [-si, 0, co]])


def rotZ(angulo):
    co = np.cos(angulo)
    si = np.sin(angulo)

    return np.array([[co, si, 0], 
                     [-si, co, 0], 
                     [0, 0, 1]])
