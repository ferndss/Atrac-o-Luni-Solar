import numpy as np
import const

const.accel = []

# constante gravitacional
const.mi = 398600

const.c = 2.998e8

const.S = 1367

const.PSR = const.S / const.c

const.CR = 2

const.m = 100

const.As = 200

c_light = 299792457.999999984 / 1000

const.P_Sol = (1.367 / c_light)

const.AU = 149597870699.99998 / 1000

# constante gravitacional solar
const.GM_Sun = GM_Sun = 132.712e9                   # [km^3/s^2]; DE436

# constante gravitacional lunar
const.GM_Moon = 4902                                # [km^3/s^2]; DE436

# raio da terra
const.rT = 6388

# constante J2
const.J2 = 0.00108263

const.MJD_J2000 = 51544.5

const.tol = 1e-4

const.AU = 149597870.691

const.Arcs = 3600 * 180 / np.pi

const.Rad = np.pi / 180

const.min = 60

const.hor = 3600

const.dia = 86400
