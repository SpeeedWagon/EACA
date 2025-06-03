import ComplexPygame as C
import Color
import math
import cmath

def cercQR(q, r):
        def gamma(t):
            return q + C.fromRhoTheta(r, t)

        return gamma

def desenareCerc(centru, raza,culoare):
    epsilon = 0.04
    for z in C.screenAffixes():
        if(abs(z-centru)<=raza +epsilon and abs(z-centru)>=raza-epsilon ):
            C.setPixel(z,culoare)
    
def inversiunea(centru,raza):
    centrul_inversiune = 7 - 5j
    raza_inversiune = 6
    P_denominator = abs(centru - centrul_inversiune)**2 - raza**2
    epsilon = 1e-9 
    if abs(P_denominator) < epsilon:
        return [None, None] # Indicate that circle parameters cannot be returned
    c_inv = centrul_inversiune + (raza_inversiune**2 * (centru - centrul_inversiune)) / P_denominator
    r_inv = (raza_inversiune**2 * raza) / abs(P_denominator)
    # centrul_inversiune = -5 + 0j
    # raza_inversiune = 1
    # c_inv = centrul_inversiune+raza_inversiune**2/(centru-centrul_inversiune).conjugate()
    # r_inv = raza_inversiune**2 * raza /abs(abs(centru-centrul_inversiune)**2 - raza**2)
    return [c_inv,r_inv]

def Steiner():
    n = 15
    C.setXminXmaxYminYmax(-10, 10, -10, 10)
    C.fillScreen(Color.Whitesmoke)
    C.setAxis()
    centrul_inversiune = 7 - 0j
    raza_inversiune = 6
    # desenareCerc(centrul_inversiune,raza_inversiune,Color.Black)
    epsilon = 0.04
    c = 0+0j
    thetha = math.pi /n
    r = 2
    r2 = 6
    rho = (r*math.sin(thetha))/(1-math.sin(thetha))
    centrul_steiner = r+rho
    c1 = centrul_steiner +0j
    [ci,ri] = inversiunea(c,r)
    # desenareCerc(c,r)
    desenareCerc(ci,ri,Color.Blue)
    [ci,ri] = inversiunea(c,r+2*rho)
    desenareCerc(ci,ri,Color.Blueviolet)
    # desenareCerc(c,r+2*rho)
    cercurile_initiale = [

    ]
    for k in range(0,n):
        unghi_actual = k*2*thetha
        centru_x = centrul_steiner* math.cos(unghi_actual)
        centru_y = centrul_steiner* math.sin(unghi_actual)
        # cercurile_initiale.append([(centru_x,centru_y),rho])
        centru = centrul_steiner*cmath.exp(1j* unghi_actual)
        cercurile_initiale.append(centru)
        # desenareCerc(centru,rho,Color.Crimson)
        [ci,ri]=inversiunea(centru, rho)
        desenareCerc(ci,ri,Color.Blue)

    print(cercurile_initiale)

    # r1 = 7.0
    # r2 = 7
   
    # rho_s = (r2- r)/2
    # col = Color.Cyan
    # n = 3
    # unghi = 2*math.asin(r2/(r2+rho_s))
    
# Steiner(9)

def inversiunea2(centru,raza,centrul_inversiune, raza_inversiune):
    # centrul_inversiune = 0 - 10j
    # raza_inversiune = 8
    P_denominator = abs(centru - centrul_inversiune)**2 - raza**2
    epsilon = 1e-9 
    if abs(P_denominator) < epsilon:
        return [None, None]
    c_inv = centrul_inversiune + (raza_inversiune**2 * (centru - centrul_inversiune)) / P_denominator
    r_inv = (raza_inversiune**2 * raza) / abs(P_denominator)
    
    return [c_inv,r_inv]

def Steiner2():
    C.setXminXmaxYminYmax(-10,10,-10,10)
    C.fillScreen(Color.Whitesmoke)
    C.setAxis()
    raza = 2
    centrele_cercurilor = []
    
    for i in range(0,8):
        centrele_cercurilor.append([complex(-8+x*2,-i*2) for x in range(0,9)])
    print(centrele_cercurilor)
    
    for j in centrele_cercurilor:
        for c in j:
            # desenareCerc(c,1/2,Color.Coral)
            # desenareCerc(c,1,Color.Black)
            [ci,ri] = inversiunea2(c,1,0+10j,9)
            [c2,r2] = inversiunea2(ci,ri,0-6j,6)
            print(c2,r2)
            desenareCerc(c2,r2,Color.Crimson)
if __name__ == '__main__':
    C.initPygame()
    C.run(Steiner2)
    
