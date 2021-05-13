""" inverso obter os elementos keplerianos """
import numpy as np
import const


def P_inverso(Rpos, Rvel):
    """ posição (r)"""
    r_e = np.linalg.norm(Rpos)
    print('r_e: ', r_e)
    """ velocidade (v)"""
    v_e = np.linalg.norm(Rvel)
    print('v_e', v_e)

    """ multiplicação vetorial de posição com a velocidade"""
    vr = np.dot(Rvel, Rpos)
    print('vr: ', vr)
    vr = (vr / r_e)

    """ Magnetude do momento angular (h)"""
    h = np.cross(Rpos, Rvel)
    print('h: ', h)
    momA = np.linalg.norm(h)
    print('momA: ', momA)

    """ inclinação (i)"""
    i_1 = (h[2] / momA)
    incl = np.cos(i_1)

    """ multiplicação vetorial de K com h """
    k = np.array([0, 0, 1])
    n1 = np.cross(k, h)
    n1_e = np.linalg.norm(n1)

    """ excentricidade """
    e = (1 / const.mi * (((pow(v_e, 2) - const.mi / r_e) * Rpos) - r_e * vr * Rvel))
    exce = np.linalg.norm(e)
    print(exce)

    """ Raio do Perigeu """
    rp = pow(momA, 2) / (const.mi * (1 + exce * np.cos(0)))
    """ Raio do Apogeu """
    ra = pow(momA, 2) / (const.mi * (1 + exce * np.cos(np.radians(180))))
    print('ra: ', ra, 'rp: ', rp)

    """ Semi eixo maior """
    semE = 0.5 * (int(rp + ra))
    print('semE: ', semE)
    """ argumento do perigeu """
    Ne = np.dot(n1, e)
    if e[2] > 0 or e[2] == 0:
        argP = np.cos(Ne / (n1_e * exce))
    else:
        argP = np.radians(360) - np.cos(Ne / (n1_e * exce))

    """ ascenção da reta """
    if n1[1] > 0 or n1[1] == 0:
        ascR = np.cos((n1[0] / n1_e))
    else:
        ascR = np.radians(360) - np.cos((n1[0] / n1_e))

    """ anomalia Verdadeira """
    er = np.dot(e, Rpos)
    print('er: ', er, exce, r_e)
    if vr > 0 or vr == 0:
        anoV = np.cos(er / (exce * r_e))
        print(anoV)
    else:
        anoV = np.radians(360) - np.cos(er / (exce * r_e))

    """ periodo """
    periodo = 2 * np.pi / np.sqrt(const.mi) * pow(semE, 1.5)
    print('T: ', periodo, pow(semE, 1.5))
    """ Anomalia excentrica """
    anom_exce = 2 * np.tan(np.tan(anoV / 2) / np.sqrt((1 + exce) / (1 - exce)))

    """ Anomalia Media """
    anoM = anom_exce - exce * np.sin(anom_exce)

    """ Movimento Médio """
    mov_med = 2 * np.pi / periodo
    print(mov_med)
    """ Anomalia excentrica Inicial """
    anoEI = np.tan(np.sqrt((1 - exce) / (1 + exce)) * (np.tan(anoV / 2))) * 2

    """ Tempo Inicial """
    tempo = (anoEI - exce * np.sin(anoEI)) / mov_med
    print('tempo', tempo)

    elk = [semE, exce, incl, ascR, argP, momA, anoM, anoV, mov_med, tempo, periodo]

    return elk
