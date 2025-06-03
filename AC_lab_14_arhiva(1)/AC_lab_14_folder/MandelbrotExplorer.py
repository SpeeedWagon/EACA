import ComplexPygame as C
import Color

def MandelbrotExplorer():
    x0 = -0.5
    y0 = 0.0
    r0 = 1.0
    nrIter = 279

    def oDerulareCompleta():
        C.fillScreen()
        for coloana in C.screenColumns():
            for c in coloana:
                z = 0
                for k in range(nrIter):
                    z = z * z + c
                    if abs(z) > 2:
                        break
                C.setPixel(c, Color.Index(k))
            if saComandat():
                return False
        return True

    def saComandat():
        nonlocal x0, y0, r0, nrIter
        C.refreshScreen()
        rez = False
        for event in C.pygame.event.get():
            if event.type == C.pygame.QUIT:
                C.mustExit = True
                return True  # parasim unClick()
            if event.type == C.pygame.MOUSEBUTTONDOWN:
                ii, jj = event.pos
                x0, y0 = C.getXY(ii, C.dim - jj)
                r0 *= 0.1
                rez = True
            elif event.type == C.pygame.KEYDOWN:
                if event.key == C.pygame.K_SPACE:
                    C.mustPainting = False
                    rez = True
                elif event.key == C.pygame.K_n:
                    nrIter *= 2
                    rez = True
                elif event.key == C.pygame.K_m:
                    nrIter //= 2
                    rez = True
                elif event.key == C.pygame.K_b:
                    r0 *= 5
                    rez = True
        return rez


    print("\nMENIU:")
    print("<click> pentru zoom")
    print("<space> pentru start/stop")
    print("<n> pentru nrIter *= 2")
    print("<m> pentru nrIter //= 2")
    print("<b> pentru r0 *= 5")
    # bucla derularilor
    while True:
        C.setXminXmaxYminYmax(x0 - r0, x0 + r0, y0 - r0, y0 + r0)
        C.pygame.display.set_caption(f"x0={x0:.15f}, y0={y0:.15f}, n={nrIter}, r0={r0:.1e}")
        saDerulatPanaLaCapat = oDerulareCompleta()
        if C.mustExit or not C.mustPainting:
            break  # parasim bucla derularilor
        if saDerulatPanaLaCapat:
            C.saveScreenPNG("mandelbrot")
            while not saComandat():  # asteptam o noua comanda
                pass        #  pana atunci nu facem nimic
            # am primit o comanda:
            if C.mustExit or not C.mustPainting:
                break  # parasim bucla derularilor
        # reluam derularea
    return

if __name__ == '__main__':
    C.initPygame()
    C.run(MandelbrotExplorer)
