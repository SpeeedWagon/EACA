import ComplexPygame as C
import Color
import math


def PseudoSpiralaLuiArhimede():
    nrPuncte = 1000
    alfa = math.pi/2
    omega = C.fromRhoTheta(1, alfa / nrPuncte)

    def traseazaArc(q, delta):
        for k in range(nrPuncte):
            delta *= omega
            C.setPixel(q + delta, Color.Red)
        versor = delta / C.rho(delta)
        q -= versor
        delta += versor
        C.drawLine(q, q + delta, Color.Black)
        return q, delta

    lat = 20
    C.setXminXmaxYminYmax(-lat, lat, -lat, lat)
    q = 0
    delta = 1j
    for k in range(20):
        q, delta = traseazaArc(q, delta)
    C.refreshScreen()

def GoldenRatio2024():
    fi = (1 + math.sqrt(5.0)) / 2
    omegaCDprimPeAD = -1j / fi

    def traseazaSiTransforma(sector):
        a = sector[0]
        d = sector[- 1]
        c = sector[-2]
        b = a + c - d
        dprim = c + (d - c) / fi
        C.fillNgon([a, b, c, d], Color.Gold)
        # C.fillNgon(sector, Color.Red)
        C.drawNgon([a, b, c, d], Color.Red)
        return [dprim + omegaCDprimPeAD * (z - d) for z in sector]

    C.setXminXmaxYminYmax(-0.5, 2, -0.75, 1.75)
    C.fillScreen(Color.Mediumaquamarine)
    a = 0
    b = 1j
    c = 1 + 1j
    d = 1
    C.setText("A", a - 0.1j)
    C.setText("B", b + 0.01j)
    C.setText("C", c + 0.01j)
    C.setText("D", d - 0.1j)
    nrPuncte = 1000
    alfa = -math.pi / (2 * nrPuncte)
    sector = [d + C.fromRhoTheta(1, n * alfa) * (a - d) for n in range(nrPuncte)]
    sector.append(d)
    for k in range(10):
        sector = traseazaSiTransforma(sector)
        C.refreshScreen()
        C.wait(100)

##############################################################

if __name__ == '__main__':
    C.initPygame()
    C.run(GoldenRatio2024)
    C.run(PseudoSpiralaLuiArhimede)
