import ComplexPygame as C
import Color

def Nisshoki():
    C.setXminXmaxYminYmax(-2, 2, -2, 2)
    r = 3.0 / 5.0;
    for z in C.screenAffixes():
        col = Color.Cyan
        if abs(z) < r:
            col = Color.Crimson
        C.setPixel(z, col)
    # C.setAxis()
    C.refreshScreen()



if __name__ == '__main__':
    C.initPygame()
    C.run(Nisshoki)

