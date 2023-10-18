import math

sin = math.sin
cos = math.cos
tan = math.tan
atan = math.atan
sinh = math.sinh
cosh = math.cosh
log = math.log
pi = math.pi

ak = 6378245
bk = 6356863.01877
ek = 0.0818133340169
ek_2 = ek * ek

c11 = 0.00000084007644
c12 = 0.00000408960694
c13 = 0.00000025613907
c21 = -0.0000040896065
c22 = 0.00000084076292
c23 = -0.00000173888787
c31 = -0.00000025614618
c32 = 0.00000173888682
c33 = 0.00000084077125

Tx = -33.4297
Ty = 146.5746
Tz = 76.2865

ag = 6378137
bg = 6356752.31414
eg = 0.0818191910428
eg_2 = eg * eg


# Jest to przejście z współrzędnych BL dla układów korzystających z elipsoidy elipsoidy GRS-80 (2000, 1992, WGS-84)
# do układu BL dla współrzędnych korzystających z elipsoidy Krasnowskiego (1942, 1965) 
# ważna funkcja pełniąca role konwertera pomiędzy tymi układami
def from_BL_WGS_to_BL_Kras(B, L):
    # BLg to XYZg
    B_rad = math.radians(B)
    L_rad = math.radians(L)

    Rn = ag / math.pow(1 - eg_2 * math.sin(B_rad) * math.sin(B_rad), 1/2)

    X_g = (Rn + 200) * cos(B_rad) * cos(L_rad)
    Y_g = (Rn + 200) * cos(B_rad) * sin(L_rad)
    Z_g = (Rn * (1 - eg_2) + 200) * sin(B_rad)

    # XYZg to XYZk
    X_k = X_g + c11 * X_g + c12 * Y_g + c13 * Z_g + Tx
    Y_k = Y_g + c21 * X_g + c22 * Y_g + c23 * Z_g + Ty
    Z_k = Z_g + c31 * X_g + c32 * Y_g + c33 * Z_g + Tz

    # XYZk to BLk
    Rp = math.sqrt(X_k * X_k + Y_k * Y_k)

    B1 = atan(Z_k/Rp)
    C1 = ek * sin(B1)
    I1 = ak * ek * C1 / math.sqrt(1 - C1 * C1)

    B2 = atan((Z_k + I1) / Rp)
    C2 = ek * sin(B2)
    I2 = ak * ek * C2 / math.sqrt(1 - C2 * C2)


    B3 = math.atan((Z_k + I2) / Rp)
    C3 = ek * math.sin(B3)
    I3 = ak * ek * C3 / math.sqrt(1 - C3 ** 2)
    
    B4 = math.atan((Z_k + I3) / Rp)

    B_k = math.degrees(B4)
    L_k = math.degrees(math.acos(X_k / Rp))

    return B_k, L_k


# B_k = 49.550321958628
# L_k = 23.9352855277045

# if __name__ == "__main__":
#    B, L = from_BL_WGS_to_BL_Kras(B, L)
#    print(B, L)
#    # 49.5500719646959
#    # 23.9335941579051
