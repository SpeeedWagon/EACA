import ComplexPygame as C
import Color
import random
import math
def JuliaBazine():
    c = -0.21 -0.7j

    def f(z):
        return z * z + c
    C.setXminXmaxYminYmax(-1.5, 1.5, -1.5, 1.5)
    C.fillScreen(Color.Black)
    nrIter = 1001+18
    rhoMax = 1.0e2
    for coloana in C.screenColumns():
        for zeta in coloana:
            z = zeta
            for k in range(nrIter):
                if abs(z) >= rhoMax: break
                z = f(z)
            if abs(z) < rhoMax:
                color=Color.Index(10 * sum(C.getHK(z)) + 200)
                C.setPixel(zeta, color)
                # C.setPixel(z,color)
        if C.mustClose():
            return

def Glyyn():
    c = -0.2
    x0 = 0.235
    y0 = 0.5
    l = 0.2
    def f(z):
        return z **(1.5)+ c

    C.setXminXmaxYminYmax(x0-l, x0+l, y0-l, y0+l)
    nrIter = 1000
    for coloana in C.screenColumns():
        for zeta in coloana:
            z = zeta
            for k in range(nrIter):
                if C.rho(z) > 4: break
                z = f(z)
            C.setPixel(zeta, Color.Index(100 + 5*k))
        if C.mustClose():
            return

def Nautilius():
    c = 0.45 + 0.2j
    rhoMax = 1.0e20
    omega = (C.fromRhoTheta(1.001,math.pi/12))
    def f(z):
       return (z*z*z-z)/(omega*z*z+1)
        

    def zar():
        return random.uniform(-0.5, 0.5)

    C.setXminXmaxYminYmax(-20, 20, -20, 20)
    C.fillScreen()
    prec = 0.01
    nrIter = 800    
    for coloana in C.screenColumns():
        for zeta in coloana:
            z1 = zeta + prec * complex(zar(), zar())
            z2 = zeta + prec * complex(zar(), zar())
            for k in range(nrIter):
                z1 = f(z1)
                z2 = f(z2)
                if C.rho(z1) + C.rho(z2) >= rhoMax:
                    break

            col = Color.White
            if C.rho(z1) >= rhoMax and C.rho(z2) >= rhoMax or C.rho(z1 - z2) < prec:
                col = Color.Red
            C.setPixel(zeta, col)
        if C.mustClose():
            return


####################################################
def JuliaPlina2():
    rhoMax = 1.0e2

    def f(z):
        if z == 0:
            return rhoMax
        u = z * z
        return u - 1 / u

    C.setXminXmaxYminYmax(-2, 2, -2, 2)
    nrIter = 100
    for coloana in C.screenColumns():
        for zeta in coloana:
            z = zeta
            for k in range(nrIter):
                z = f(z)
                if abs(z) > rhoMax: break
            C.setPixel(zeta, Color.Index(100 * k))
        if C.mustClose():
            break

####################################################
def JuliaFinal():
    c = 0.001

    def f(z):
        if z == 0: return rhoMax
        return (z * z * z + c) / z

    C.setXminXmaxYminYmax(-1.1, 1.1, -1.1, 1.1)
    C.fillScreen(Color.Black)
    C.refreshScreen()
    rhoMax = 100
    nrIter = 107
    for coloana in C.screenColumns():
        for zeta in coloana:
            z = zeta
            for k in range(nrIter):
                if abs(z) > rhoMax: break
                z = f(z)
            if abs(z) <= rhoMax:
                col = Color.Index(abs(sum(C.getHK(20 * z))) + 650)
                C.setPixel(zeta, col)
                #C.setPixel(z, col)
        if C.mustClose():
            return


####################################################

if __name__ == '__main__':
    C.initPygame()
    # C.run(JuliaBazine)
    # C.run(JuliaPlina2)
    C.run(Glyyn)
    # C.run(JuliaFinal)
