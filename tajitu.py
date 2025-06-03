import ComplexPygame as C
import Color
import math
def Taijitu_01():
    def UnSemiDisc(q, r, sens, col):
# q:centru, r:raza, sens: stanga sau dreapta, col:culoarea
        for z in C.screenAffixes():
            if sens == "stg" and z.real > q.real:
                continue
            if sens == "drp" and z.real < q.real:
                continue
            if C.rho(z - q) < r:
                C.setPixel(z, col)
    a = 6.1
    C.setXminXmaxYminYmax(-a, a, -a, a)
    
    
    Alb = Color.White
    Negru = Color.Navy
    C.fillScreen(Color.Cyan)
    UnSemiDisc(0, 6, "stg", Alb)
    UnSemiDisc(0, 6, "drp", Negru)
    UnSemiDisc(3j, 3, "drp", Alb)
    UnSemiDisc(-3j, 3, "stg", Negru)
    
    
    UnSemiDisc(3j, 1, "stg", Alb)
    UnSemiDisc(-3j, 1, "drp", Negru)
    UnSemiDisc(1.5j, 1/2, "drp", Alb)
    UnSemiDisc(-1.5j, 1/2, "stg", Negru)
    
    
    # UnSemiDisc(3j, 1, None, Negru)
    # UnSemiDisc(-3j, 1, None, Alb)
if __name__ == '__main__':
    C.initPygame()
    C.run(Taijitu_01)