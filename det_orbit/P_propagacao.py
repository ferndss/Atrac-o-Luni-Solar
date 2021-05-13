import const
import numpy as np
from D_julian import D_julian
from P_direto import P_direto
from P_inverso import P_inverso
from A_excentrica import A_excentrica


def P_propagação(pos, vel, ano, mes, dia, hor, min, seg):
    elk = P_inverso(pos, vel)

    ListT = []
    ListP = []
    
    semE = elk[0]
    exce = elk[1]
    incl = elk[2]
    ascR = elk[3]
    argP = elk[4]
    momA = elk[5]
    temI = elk[9]
    tempo = elk[10]
    mov_med = elk[8]

    Tinicial = D_julian(ano, mes, dia, hor, min, seg).Data_J

    per = hor + tempo/60

    while hor < per:

        min += 1

        if min >= 59:
            hor += 1
            min = 1

        data = D_julian(ano, mes, dia, hor, min, seg).Data_J
        delta_t = (data - Tinicial) * 86400

        temp_fin = temI + delta_t
        ListT.append(["%.1f" % round(delta_t, 2)])

        np2 = temp_fin / tempo
        t32 = (np2 - np.floor(np2)) * tempo

        """ Anomalia Média """
        anoMF = mov_med * t32

        """ Anomalia Excentrica """
        anoE = A_excentrica(anoMF, exce)        
 
        """ Ascensão da Reta """
        asc1 = -1.5 * (np.sqrt(const.mi) * const.J2 * pow(const.rT, 2) /
                       (((1 - pow(exce, 2)) ** 2) * pow(semE, 3.5))) * np.cos(incl)

        g = np.degrees(asc1)
        ascRF = np.radians(np.degrees(ascR) + g * delta_t)

        """ Argumento do Perigeu """
        arg1 = -1.5 * (np.sqrt(const.mi) *
                       const.J2 * pow(const.rT, 2) /
                       ((1 - pow(exce, 2) ** 2) *
                        pow(semE, 3.5))) * (2.5 * pow(np.sin(incl), 2) - 2)

        g2 = np.degrees(arg1)

        argPF = np.radians(np.degrees(argP) + g2 * delta_t)

        """ anomalia Verdadeira """
        anoVF = 2 * np.tan(np.sqrt((1 + exce) / (1 - exce)) * np.tan(anoE / 2))

        posF, velF = P_direto(exce, incl, ascRF, argPF, momA=momA, anoV=anoVF)
        ListP.append(posF)

    return [ListP[0], ListP[1], ListP[2]]
