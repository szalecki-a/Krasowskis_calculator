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

d11 = -0.00000084078048
d12 = -0.00000408959962
d13 = -0.00000025614575
d21 = 0.00000408960007
d22 = -0.00000084078196
d23 = 0.00000173888389
d31 = 0.00000025613864
d32 = -0.00000173888494
d33 = -0.00000084077363
Tx = -33.4297
Ty = 146.5746
Tz = 76.2865

ag = 6378137
bg = 6356752.31414
eg = 0.0818191910428
eg_2 = eg * eg


# Jest to przejście z współrzędnych BL dla układów korzystających z elipsoidy Krasnowskiego (1942, 1965)
# do układu BL dla współrzędnych korzystających z elipsoidy GRS-80 (2000, 1992, WGS-84)
# ważna funkcja pełniąca role konwertera pomiędzy tymi układami
def from_BL_Kras_to_BL_WGS(B, L):
    # BLk to XYZk
    B_rad = math.radians(B)
    L_rad = math.radians(L)

    Rn = ak / math.pow(1 - ek_2 * math.sin(B_rad) * math.sin(B_rad), 1/2)

    X_k = (Rn + 200) * cos(B_rad) * cos(L_rad)
    Y_k = (Rn + 200) * cos(B_rad) * sin(L_rad)
    Z_k = (Rn * (1 - ek_2) + 200) * sin(B_rad)

    # XYZk to XYZg
    X_g = X_k + d11 * (X_k - Tx) + d12 * (Y_k - Ty) + d13 * (Z_k - Tz) - Tx
    Y_g = Y_k + d21 * (X_k - Tx) + d22 * (Y_k - Ty) + d23 * (Z_k - Tz) - Ty
    Z_g = Z_k + d31 * (X_k - Tx) + d32 * (Y_k - Ty) + d33 * (Z_k - Tz) - Tz

    # XYZg to BLg
    Rp = math.sqrt(X_g * X_g + Y_g * Y_g)

    B1 = atan(Z_g/Rp)
    C1 = eg * sin(B1)
    I1 = ag * eg * C1 / math.sqrt(1 - C1 * C1)

    B2 = atan((Z_g + I1) / Rp)
    C2 = eg * sin(B2)
    I2 = ag * eg * C2 / math.sqrt(1 - C2 * C2)


    B3 = math.atan((Z_g + I2) / Rp)
    C3 = eg * math.sin(B3)
    I3 = ag * eg * C3 / math.sqrt(1 - C3 ** 2)
    
    B4 = math.atan((Z_g + I3) / Rp)

    B_g = math.degrees(B4)
    L_g = math.degrees(math.acos(X_g / Rp))

    return B_g, L_g


B_k = 49.550321958628
L_k = 23.9352855277045

if __name__ == "__main__":
   B, L = from_BL_Kras_to_BL_WGS(B_k, L_k)
   print(B, L)
   # 49.5500719646959
   # 23.9335941579051
