import ComplexPygame as C
import Color
import math, random, cmath


####################################################
def Mandelbrot_parametrizat():
    nrIter = 1001
    C.setXminXmaxYminYmax(-2.0, 4.0, -3, 3)
    C.fillScreen()
    for coloana in C.screenColumns():
        for omega in coloana:
            c = (1 - (omega - 1) ** 2) / 4
            z = 0
            col = Color.Black
            for k in range(nrIter):
                z = z * z + c
                if abs(z) > 2:
                    col = Color.Index(k)
                    break
            C.setPixel(omega, col)
        if C.mustClose():
            return

####################################################


if __name__ == '__main__':
    C.initPygame()

    C.run(Mandelbrot_parametrizat)

