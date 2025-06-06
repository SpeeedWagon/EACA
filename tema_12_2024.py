import ComplexPygame as C
import Color
import math

def Newton4prim():
    eps0 = C.fromRhoTheta(1.0, math.pi*(2*0 + 1) / 4.0)
    eps1 = C.fromRhoTheta(1.0,math.pi*(2*1 + 1)  / 4.0)
    eps2 = C.fromRhoTheta(1.0, math.pi*(2*2 + 1) / 4.0)
    eps3 = C.fromRhoTheta(1.0,math.pi*(2*3 + 1) / 4.0)
    def f(z):
        return (3*z*z*z*z -1)/( 4*z*z*z ) if z != 0 else 10e10

    c0 = 0
    r = 1
    C.setXminXmaxYminYmax(c0.real - r, c0.real + r, c0.imag - r, c0.imag + r)
    nrIter = 300
    for coloana in C.screenColumns():
        for zeta in coloana:
            col = Color.Black
            z = zeta
            for _ in range(nrIter):
                if abs(z - eps0) < 0.1:
                    col = Color.Darkblue
                    break
                if abs(z - eps1) < 0.1:
                    col = Color.Yellow
                    break
                if abs(z - eps2) < 0.1:
                    col = Color.Fuchsia
                    break
                if abs(z - eps3) < 0.1:
                    col = Color.Green
                    break
                z = f(z)
            C.setPixel(zeta, col)
        if C.mustClose(): return
    C.drawLine(c0 - r, c0 + r, Color.White)
    C.drawLine(c0 - r * 1j, c0 + r * 1j, Color.White)

def NewtonGeneralizat(a,n):
    eps0 = C.fromRhoTheta(pow(a,1/n), math.pi*(2*0 + 1) / 4.0)
    eps1 = C.fromRhoTheta(,math.pi*(2*1 + 1)  / 4.0)
    eps2 = C.fromRhoTheta(1.0, math.pi*(2*2 + 1) / 4.0)
    eps3 = C.fromRhoTheta(1.0,math.pi*(2*3 + 1) / 4.0)
    def f(z):
        return (3*z*z*z*z -1)/( 4*z*z*z ) if z != 0 else 10e10

    c0 = 0
    r = 1
    C.setXminXmaxYminYmax(c0.real - r, c0.real + r, c0.imag - r, c0.imag + r)
    nrIter = 300
    for coloana in C.screenColumns():
        for zeta in coloana:
            col = Color.Black
            z = zeta
            for _ in range(nrIter):
                if abs(z - eps0) < 0.1:
                    col = Color.Darkblue
                    break
                if abs(z - eps1) < 0.1:
                    col = Color.Yellow
                    break
                if abs(z - eps2) < 0.1:
                    col = Color.Fuchsia
                    break
                if abs(z - eps3) < 0.1:
                    col = Color.Green
                    break
                z = f(z)
            C.setPixel(zeta, col)
        if C.mustClose(): return
    C.drawLine(c0 - r, c0 + r, Color.White)
    C.drawLine(c0 - r * 1j, c0 + r * 1j, Color.White)

####################################################

if __name__ == '__main__':
    C.initPygame()
    C.run(Newton4prim)

