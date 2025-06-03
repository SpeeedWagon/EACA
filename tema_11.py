
import ComplexPygame as C
import Color
import math


def Peano():
    c1 = (1 + 1j) / 6
    c2 = (1 + 3j) / 6
    c3 = (1 + 5j) / 6
    c4 = (3 + 5j) / 6
    c0 = (3 + 3j) / 6
    c5 = (3 + 1j) / 6
    c6 = (5 + 1j) / 6
    c7 = (5 + 3j) / 6
    c8 = (5 + 5j) / 6

    def s0(z):
        return c0 - (z - c0) / 3

    def s1(z):
        return c1 + (z - c0) / 3

    def s2(z):
        return c2 - (z - c0).conjugate() / 3

    def s3(z):
        return c3 + (z - c0) / 3

    def s4(z):
        return c4 + (z - c0).conjugate() / 3

    def s5(z):
        return c5 + (z - c0).conjugate() / 3

    def s6(z):
        return c6 + (z - c0) / 3

    def s7(z):
        return c7 - (z - c0).conjugate() / 3

    def s8(z):
        return c8 + (z - c0) / 3

    def transforma(li):
        rez = []
        for z in li:  rez.append(s1(z))
        for z in li:  rez.append(s2(z))
        for z in li:  rez.append(s3(z))
        for z in li:  rez.append(s4(z))
        for z in li:  rez.append(s0(z))
        for z in li:  rez.append(s5(z))
        for z in li:  rez.append(s6(z))
        for z in li:  rez.append(s7(z))
        for z in li:  rez.append(s8(z))
        return rez

    def traseaza(li):
        C.fillScreen()
        # trasam chenarul
        C.drawNgon([0, 1, 1 + 1j, 1j], Color.Black)
        for n in range(1, len(li)):
            col = Color.Red if n % 9 == 0 else Color.Blue
            C.drawLine(li[n - 1], li[n], col)

    C.setXminXmaxYminYmax(-0.1, 1.1, -0.1, 1.1)
    fig = [c0]
    for k in range(2):
        fig = transforma(fig)
        traseaza(fig)
        if C.mustClose(): return




##########################################################
def KochCu2Transformari():
    theta = math.pi / 6
    rho = 0.5 / math.cos(theta)
    w = C.fromRhoTheta(rho, theta)
    zA = 0
    zB = 1
    zC = zA + w * (zB - zA)
    omega1 = (zC - zA) / (zB - zA).conjugate()
    omega2 = (zC - zB) / (zA - zB).conjugate()

    def T1(z):
        return zA + omega1 * (z - zA).conjugate()

    def T2(z):
        return zB + omega2 * (z - zB).conjugate()

    def transforma(li):
        rez = [T1(z) for z in li]
        rez.extend([T2(z) for z in li])
        return rez

    C.setXminXmaxYminYmax(-0.1, 1.1, -0.1, 1.1)
    fig = [zA, zB]
    nrEtape = 10
    for k in range(nrEtape):
        fig = transforma(fig)
        C.fillScreen()
        col = Color.Index(300 + 10 * k)
        for h in range(1, len(fig)):
            C.drawLine(fig[h - 1], fig[h], col)
        if C.mustClose(): return
        C.wait(50)
    C.setAxis()

###############################################################
def SierpinskiTriunghiDrepunghic():
    zB = 0
    zC = 1
    zQ = (zB + zC) / 2
    zA = zQ + C.fromRhoTheta(C.rho(zC - zQ), 2 * math.pi / 5)
    k1 = (zA - zC) / (zB - zC).conjugate()
    k2 = (zA - zB) / (zC - zB).conjugate()

    def s1(z):
        return zC + k1 * (z - zC).conjugate()

    def s2(z):
        return zB + k2 * (z - zB).conjugate()

    def transforma(li):
        rez = []
        for z in li:
            rez.append(s1(z))
        for z in li:
            rez.append(s2(z))
        return rez

    def traseaza(li):

        C.fillScreen()
        z1 = li[0]
        z2 = li[1]
        z3 = li[2]
        zA = (z1 + z2 + z3) / 3
        C.drawLine(z1, z2, Color.Blue)
        C.drawLine(z2, z3, Color.Blue)
        C.drawLine(z3, z1, Color.Blue)
        if (len(li) == 3): return
        for n in range(5, len(li), 3):
            z1 = li[n - 2]
            z2 = li[n - 1]
            z3 = li[n]
            zB = (z1 + z2 + z3) / 3
            C.drawLine(z1, z2, Color.Blue)
            C.drawLine(z2, z3, Color.Blue)
            C.drawLine(z3, z1, Color.Blue)
            C.drawLine(zA, zB, Color.Red)
            zA = zB

    #   makeImage()
    #    {
    C.setXminXmaxYminYmax(-0.1, 1.1, -0.1, 1.1)
    fig = [zB, zA, zC]

    # traseaza(fig);
    for k in range(7):
        fig = transforma(fig)
        traseaza(fig)
        if C.mustClose(): return
    return

##############################################################

def HilberTriunghi():
    class Triunghi:
        def __init__(self, a, b, c):
            self.a, self.b, self.c = a, b, c

        def show(self, col):
            C.fillNgon([self.a, self.b, self.c], col)

        def centru(self):
            return (self.a + self.b + self.c ) / 3

    def transforma(li):
        rez = []
        for P in li:
            mab, mbc, mac = (P.a + P.b) / 2, (P.b + P.c) / 2, (P.c + P.a) / 2
            c0 = P.centru()
            rez.append(Triunghi(P.a, mab, mac))
            rez.append(Triunghi(mac, mab, mbc))
            rez.append(Triunghi(mab, mbc, P.b))
            rez.append(Triunghi(mac, mbc, P.c))
        return rez

    def traseaza(li):
        for k in range(len(li)):
            li[k].show(Color.Index(200 + k ))
            if C.mustClose(): return


    def liniaza(li):
        for k in range(1, len(li)):
            col = Color.Index(k // 5)
            C.drawLine(li[k - 1].centru(), li[k].centru(), col)
            if C.mustClose(): return

    C.setXminXmaxYminYmax(0, 10, 0, 10)
    C.fillScreen(Color.Navy)
    fig = [Triunghi(5*(0 + 0j),5*( 2+ 0j), 5*(1 + 2j))]
    # fig = [Patrat(0.5 + 1j, 1 + 9j, 7 + 8j, 9.5 + 1j)]
    nrEtape=5
    for k in range(nrEtape):
        fig = transforma(fig)
    traseaza(fig)
    # liniaza(fig)

def TriunghiLinie():
    class Triunghi:
        def __init__(self, a, b, c):
            self.a, self.b, self.c = a, b, c

        def show(self, col):
            C.fillNgon([self.a, self.b, self.c], col)
        def draw(self):
            C.drawLine(self.a,self.b,Color.Black)
            C.drawLine(self.b,self.c,Color.Black)
            C.drawLine(self.c,self.a,Color.Black)
            C.drawLine(self.a,self.centru(),Color.Black)
            C.drawLine(self.c,self.centru(),Color.Black)
        def centru(self):
            return (self.a + self.b + self.c ) / 3

    def transforma(li):
        rez = []
        for P in li:
            mab, mbc, mac = (P.a + P.b) / 2, (P.b + P.c) / 2, (P.c + P.a) / 2
            c0 = P.centru()
            rez.append(Triunghi(mab, mbc, P.b))
            rez.append(Triunghi(P.a, mab, mac))#nu
            rez.append(Triunghi(mab, mac, mbc))#nu
            rez.append(Triunghi(mac, P.c, mbc))#nu
        return rez

    def traseaza(li):
        for k in range(len(li)):
            li[k].show(Color.Index(200 + k ))
            if C.mustClose(): return


    def liniaza(li):
        for k in range(0, len(li)):
            col = Color.Index(k // 5)
            # print(li[k].a,li[k].centru())
            li[k].draw()
            # C.drawLine(li[k].centru(), li[k].c, col)
            # C.drawLine(li[k].b, li[k].centru(), col)
            if C.mustClose(): return

    C.setXminXmaxYminYmax(0, 10, 0, 10)
    C.fillScreen(Color.Whitesmoke)
    fig = [Triunghi(5*(0 + 0j),5*( 2+ 0j), 5*(1 + 2j))]
    # fig = [Patrat(0.5 + 1j, 1 + 9j, 7 + 8j, 9.5 + 1j)]
    nrEtape=1
    for k in range(nrEtape):
        fig = transforma(fig)
    print(len(fig))
    traseaza(fig)
    liniaza(fig)
if __name__ == '__main__':
    C.initPygame()
    # C.run(Peano)
    C.run(HilberTriunghi)
    C.run(TriunghiLinie)
    # C.run(KochCu2Transformari)
    # C.run(SierpinskiTriunghiDrepunghic)

