""" direto obter as posições e velocidades """
import const
import numpy as np
from rotmatriz import rotX, rotZ
from A_excentrica import A_excentrica


def P_direto(exce, incl, ascR, argP, semE=None, momA=None, anoM=None, anoV=None):
    global Npos, Nvel

    if anoM is not None and momA is None:
        E = A_excentrica(anoM, exce)

        c1 = np.sqrt(1 - exce ** 2)
        cE = np.cos(E)
        c3 = np.sqrt(const.mi / semE) / (1. - exce * cE)
        sE = np.sin(E)

        """ posição """
        rx = semE * (cE - exce)
        ry = semE * c1 * sE
        rz = 0
        Npos = np.array([rx, ry, rz])

        """ velocidade """
        vx = -c3 * sE
        vy = c1 * c3 * cE
        vz = 0
        Nvel = np.array([vx, vy, vz])

    else:
        if momA is None:
            momA = np.sqrt(const.mi * semE * (1 - exce ** 2))

        """ posição """
        rx = pow(momA, 2) / const.mi * (1 / (1 + exce * np.cos(anoV))) * np.cos(anoV)
        ry = pow(momA, 2) / const.mi * (1 / (1 + exce * np.cos(anoV))) * np.sin(anoV)
        rz = pow(momA, 2) / const.mi * (1 / (1 + exce * np.cos(anoV))) * 0
        Npos = np.array([rx, ry, rz])

        """ velocidade """
        vx = const.mi / momA * -np.sin(anoV)
        vy = const.mi / momA * (exce + np.cos(anoV))
        vz = const.mi / momA * 0
        Nvel = np.array([vx, vy, vz])

    rot1 = np.dot(rotX(incl), rotZ(ascR))
    rot2 = np.dot(rotZ(argP), rot1)
    Qx_T = np.matrix.transpose(rot2)

    Pos = np.dot(Qx_T, Npos)
    Vel = np.dot(Qx_T, Nvel)

    return Pos, Vel
