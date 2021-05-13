""" Anomalia Excentrica """
import numpy as np


def A_excentrica(anoM, exce):
    erro = 1 * pow(10, -8)

    print(anoM)

    if anoM < np.pi:
        anoE = anoM + exce / 2
    else:
        anoE = anoM - exce / 2

    ratio = 1

    while abs(ratio) < erro:
        ratio = (anoE - exce * np.sin(anoE) - anoM) / (1 + exce * np.cos(anoE))
        anoE = anoE - ratio

    return anoE
