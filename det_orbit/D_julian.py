""" Data Juliana """
import numpy as np


def parâmetros(ano, mes, dia):
    b = 0
    c = 0

    if mes <= 2:
        ano = ano - 1
        mes = mes + 12

    if ano < 0:
        c = -.75

    # check for valid calendar date
    if ano < 1582:
        pass
    elif ano > 1582:
        a = np.fix(ano / 100)
        b = 2 - a + np.floor(a / 4)
    elif mes < 10:
        pass
    elif mes > 10:
        a = np.fix(ano / 100)
        b = 2 - a + np.floor(a / 4)
    elif dia <= 4:
        pass
    elif dia > 14:
        a = np.fix(ano / 100)
        b = 2 - a + np.floor(a / 4)
    else:
        print('\\n\\n  esta é uma data inválida para este calendário!!\\n')

    jd = np.fix(365.25 * ano + c) + np.fix(30.6001 * (mes + 1))

    return jd + dia + b + 1720994.5


class D_julian(object):
    def __init__(self, data=None, hora=None, JD=None, TT=None):
        if data is None:
            data = [0, 0, 0]
            hora = [0, 0, 0]

        self.JD = JD
        self.TT = TT
        self.hor = hora[0]
        self.min = hora[1]
        self.seg = hora[2]
        self.ano = data[2]
        self.mes = data[1]
        self.dia = data[0]

    @property
    def Data_J(self):

        if self.hor and self.min or self.seg is None:
            self.hor = 0
            self.min = 0
            self.seg = 0

        jd = parâmetros(self.ano, self.mes, self.dia)
        return jd + (self.hor + self.min / 60 + self.seg / 3600) / 24

    @property
    def Data_G(self):
        if self.hor is None and self.min is None and self.seg is None:
            self.hor = 0
            self.min = 0
            self.seg = 0

        djm0 = 2400000.5

        jd = parâmetros(self.ano, self.mes, self.dia)
        jd = jd + (self.hor + self.min / 60 + self.seg / 3600) / 24

        return jd - djm0

    def Data_SyG(self, h, m, s):
        # Data Juliana since J2000
        if self.JD is not None:
            Sg0 = self.JD

        else:
            print('Data Juliana: ', self.Data_J)
            n = self.Data_J - 2415020

            # Julian centuries since J2000
            cy = n / 36525
            print('tempo Sideral', cy)

            Sg0 = 99.6909833 + 36000.7689*cy + 0.00038708*cy**2

        # Sg = 360.985647 / (h + (m/60) + (s/3600))
        Sg = Sg0 + (h + (m / 60) + (s / 3600))*15
        # 259.79275147804583
        return Sg0, Sg0 + Sg

    @property
    def Data_TDB(self):
        # Data Juliana since J2000
        n = self.JD - 2451545

        # Julian centuries since J2000
        cy = n / 36525

        # Compute Julian Centureis of TT
        TT = 36525 * cy + 51544.5
        #cy = (self.TT - 51544.5) / 36525

        # Compute Modified Julian Date of TDB
        return TT + (0.001658 * np.sin(628.3076 * cy + 6.2401) + 0.000022 * np.sin(
            575.3385 * cy + 4.2970) + 0.000014 * np.sin(1256.6152 * cy + 6.1969) + 0.000005 * np.sin(
            606.9777 * cy + 4.0212) + 0.000005 * np.sin(52.9691 * cy + 0.4444) + 0.000002 * np.sin(
            21.3299 * cy + 5.5431) + 0.000010 * np.sin(628.3076 * cy + 4.2490)) / 86400

    @property
    def Data(self):
        z = np.fix(self.JD + .5)
        fdia = self.JD + 0.5 - z

        if fdia < 0:
            fdia = fdia + 1
            z = z - 1

        if z < 2299161:
            a = z
        else:
            alpha = np.floor((z - 1867216.25) / 36524.25)
            a = z + 1 + alpha - np.floor(alpha / 4)

        b = a + 1524
        c = np.fix((b - 122.1) / 365.25)
        d = np.fix(365.25 * c)
        e = np.fix((b - d) / 30.6001)
        dia = b - d - np.fix(30.6001 * e) + fdia

        if e < 14:
            mes = e - 1
        else:
            mes = e - 13

        if mes > 2:
            ano = c - 4716
        else:
            ano = c - 4715

        hor = abs(dia - np.floor(dia)) * 24
        min = abs(hor - np.floor(hor)) * 60
        seg = abs(min - np.floor(min)) * 60

        dia = np.floor(dia)
        hor = np.floor(hor)
        min = np.floor(min)

        return [dia, mes, ano], [hor, min, seg]
