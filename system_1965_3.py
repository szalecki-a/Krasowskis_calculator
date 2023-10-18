import math
from geo_constants import constants_1965


constants_1965_3 = {"X0": 5999000,
                  "Y0": 3501000,
                  "Xgo": 5939644.7701117,
                  "Bo": 53.5833333333333,
                  "mo": 0.9998,
                  "Lo": 17.0083333333333
                  }

R_L = constants_1965["R-Lagrange"]
a_K = constants_1965["a-Krasowski"]
ecc = constants_1965["e-eccentric"]

Bo = constants_1965_3["Bo"]
mo = constants_1965_3["mo"]
Lo = constants_1965_3["Lo"]
Lo_rad = math.radians(Lo)

a2 = constants_1965["a2"]
a4 = constants_1965["a4"]
a6 = constants_1965["a6"]
a8 = constants_1965["a8"]

b2 = constants_1965["b2"]
b4 = constants_1965["b4"]
b6 = constants_1965["b6"]
b8 = constants_1965["b8"]

c2 = constants_1965["c2"]
c4 = constants_1965["c4"]
c6 = constants_1965["c6"]
c8 = constants_1965["c8"]

s_gaus_1965_3 = 6384536.79356547
s_gaus_1965_3_2 = s_gaus_1965_3 * s_gaus_1965_3
s_gaus_1965_3_4 = s_gaus_1965_3_2 * s_gaus_1965_3_2
s_gaus_1965_3_6 = s_gaus_1965_3_4 * s_gaus_1965_3_2


X0_1965_3 = constants_1965_3["X0"]
Y0_1965_3 = constants_1965_3["Y0"]
X_go_1965_3 = constants_1965_3["Xgo"]


sin = math.sin
cos = math.cos
tan = math.tan
atan = math.atan
sinh = math.sinh
cosh = math.cosh
log = math.log


def in_1965_3(x, y):
    x_st = (x - X0_1965_3) / mo
    y_st = (y - Y0_1965_3) / mo

    y_st_sq = y_st ** 2

    # Computing X_gk
    X_gk = (
        X_go_1965_3 +
        x_st -
        (x_st ** 3 / (12 * s_gaus_1965_3_2)) +
        (x_st * y_st_sq / (4 * s_gaus_1965_3_2))
    )

    # Computing Y_gk
    Y_gk = y_st - (x_st * x_st * y_st) / (4 * s_gaus_1965_3_2) \
              + (y_st * y_st * y_st) / (12 * s_gaus_1965_3_2) \
              - (x_st * x_st * x_st * x_st * y_st) / (16 * s_gaus_1965_3_4) \
              + (x_st * x_st * y_st * y_st * y_st) / (8 * s_gaus_1965_3_6) \
              - (y_st * y_st * y_st * y_st * y_st) / (80 * s_gaus_1965_3_4) \
              + (x_st * x_st * x_st * x_st * x_st * x_st * y_st) / (64 * s_gaus_1965_3_6)

    u = X_gk / R_L
    v = Y_gk / R_L

    alpha = u + b2 * sin(2 * u) * cosh(2 * v) + b4 * sin(4 * u) * cosh(4 * v) + b6 * sin(6 * u) * cosh(6 * v) + b8 * sin(8 * u) * cosh(8 * v)
    beta = v + b2 * cos(2 * u) * sinh(2 * v) + b4 * cos(4 * u) * sinh(4 * v) + b6 * cos(6 * u) * sinh(6 * v) + b8 * cos(8 * u) * sinh(8 * v)

    w = 2 * math.atan(math.exp(beta)) - math.pi / 2
    delta = math.atan(math.tan(w) / cos(alpha)) + 0.000000006
    phi = math.asin(cos(w) * sin(alpha))

    b_radians = phi + c2 * sin(2 * phi) + c4 * sin(4 * phi) + c6 * sin(6 * phi) + c8 * sin(8 * phi) + 0.0000000008
    B_output = math.degrees(b_radians)
    L_output = Lo + math.degrees(delta)

    return B_output, L_output



def out_1965_3(B, L):
    B_rad = math.radians(B)
    L_rad = math.radians(L)


    delta_L = L_rad - Lo_rad
    phi_rad = 2 * (math.atan(math.pow((1 - ecc * math.sin(B_rad)) / (1 + ecc * math.sin(B_rad)), ecc / 2) * math.tan(B_rad / 2 + math.pi / 4)) - math.pi / 4)

    X_mer = atan(sin(phi_rad) / (cos(phi_rad) * cos(delta_L)))
    Y_mer = 0.5 * log((1 + cos(phi_rad) * sin(delta_L)) / (1 - cos(phi_rad) * sin(delta_L)))

    X_gk = R_L * (X_mer + (a2 * sin(2 * X_mer) * cosh(2 * Y_mer)) + (a4 * sin(4 * X_mer) * cosh(4 * Y_mer)) + (a6 * sin(6 * X_mer) * cosh(6 * Y_mer)) + (a8 * sin(8 * X_mer) * cosh(8 * Y_mer)))
    Y_gk = R_L * (Y_mer + (a2 * cos(2 * X_mer) * sinh(2 * Y_mer)) + (a4 * cos(4 * X_mer) * sinh(4 * Y_mer)) + (a6 * cos(6 * X_mer) * sinh(6 * Y_mer)) + (a8 * cos(8 * X_mer) * sinh(8 * Y_mer)))

    X_st = (2 * s_gaus_1965_3 * sin((X_gk - X_go_1965_3) / s_gaus_1965_3)) / (cos((X_gk - X_go_1965_3) / s_gaus_1965_3) + cosh(Y_gk / s_gaus_1965_3))
    Y_st = (2 * s_gaus_1965_3 * sinh(Y_gk / s_gaus_1965_3)) / (cos((X_gk - X_go_1965_3) / s_gaus_1965_3) + cosh(Y_gk / s_gaus_1965_3))

    coordinate_X = mo * X_st + X0_1965_3
    coordinate_Y = mo * Y_st + Y0_1965_3

    return coordinate_X, coordinate_Y


x = 5969541.92054924
y = 3440559.67892851

if __name__ == "__main__":
   B, L = in_1965_3(x, y)
   X, Y = out_1965_3(B, L)
   print(X, Y)
