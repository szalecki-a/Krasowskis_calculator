import math
from geo_constants import constants_2000_global


mo = constants_2000_global["mo"]
R_L = constants_2000_global["R-Lagrange"]
ecc = constants_2000_global["e-eccentric"]

a2 = constants_2000_global["a2"]
a4 = constants_2000_global["a4"]
a6 = constants_2000_global["a6"]
a8 = constants_2000_global["a8"]

b2 = constants_2000_global["b2"]
b4 = constants_2000_global["b4"]
b6 = constants_2000_global["b6"]
b8 = constants_2000_global["b8"]

c2 = constants_2000_global["c2"]
c4 = constants_2000_global["c4"]
c6 = constants_2000_global["c6"]
c8 = constants_2000_global["c8"]


sin = math.sin
cos = math.cos
tan = math.tan
atan = math.atan
sinh = math.sinh
cosh = math.cosh
log = math.log

def in_2000(x, y, p):

    X_gk = x / mo
    Y_gk = y - constants_2000_global[str(p)]
    
    u = X_gk / R_L
    v = Y_gk / R_L

    alpha = u + (b2 * sin(2 * u) * cosh(2 * v) + b4 * sin(4 * u) * cosh(4 * v) + b6 * sin(6 * u) * cosh(6 * v) + b8 * sin(8 * u) * cosh(8 * v))
    beta = v + (b2 * cos(2 * u) * sinh(2 * v) + b4 * cos(4 * u) * sinh(4 * v) + b6 * cos(6 * u) * sinh(6 * v) + b8 * cos(8 * u) * sinh(8 * v))

    w = 2 * math.atan(math.exp(beta)) - math.pi / 2
    delta = math.atan(math.tan(w) / cos(alpha))
    phi = math.asin(cos(w) * sin(alpha))

    b_radians = phi + c2 * sin(2 * phi) + c4 * sin(4 * phi) + c6 * sin(6 * phi) + c8 * sin(8 * phi) + 0.0000000008


    B_output = math.degrees(b_radians)
    L_output = p + math.degrees(delta)

    return B_output, L_output



def out_2000(B, L, p):
    B_rad = math.radians(B)
    L_rad = math.radians(L)

    Lo_rad = math.radians(p)

    delta_L = L_rad - Lo_rad
    phi_rad = 2 * (math.atan(math.pow((1 - ecc * math.sin(B_rad)) / (1 + ecc * math.sin(B_rad)), ecc / 2) * math.tan(B_rad / 2 + math.pi / 4)) - math.pi / 4)

    X_mer = atan(sin(phi_rad) / (cos(phi_rad) * cos(delta_L)))
    Y_mer = 0.5 * log((1 + cos(phi_rad) * sin(delta_L)) / (1 - cos(phi_rad) * sin(delta_L)))

    X_gk = R_L * (X_mer + (a2 * sin(2 * X_mer) * cosh(2 * Y_mer)) + (a4 * sin(4 * X_mer) * cosh(4 * Y_mer)) + (a6 * sin(6 * X_mer) * cosh(6 * Y_mer)) + (a8 * sin(8 * X_mer) * cosh(8 * Y_mer)))
    Y_gk = R_L * (Y_mer + (a2 * cos(2 * X_mer) * sinh(2 * Y_mer)) + (a4 * cos(4 * X_mer) * sinh(4 * Y_mer)) + (a6 * cos(6 * X_mer) * sinh(6 * Y_mer)) + (a8 * cos(8 * X_mer) * sinh(8 * Y_mer)))
    
    coordinate_X = X_gk * mo
    coordinate_Y = Y_gk + constants_2000_global[str(p)]

    return coordinate_X, coordinate_Y


x = 5495070.04555949
y = 4712392.77757666

if __name__ == "__main__":
   B, L = in_2000(x, y, 21)
   X, Y = out_2000(B, L, 21)
   print(X, Y)