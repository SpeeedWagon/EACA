import ComplexPygame as C
import math
import cmath
import Color

def Bisectoare():
    R = 6
    C.setXminXmaxYminYmax(-R, R, -R, R)

    A = cmath.rect(4, math.radians(80))  
    B = cmath.rect(3.5, math.radians(-50))  
    C_ = cmath.rect(4, math.radians(220))  

    def bisector_direction(P1, P2, P3):
        v1 = P2 - P1
        v2 = P3 - P1
        bisec_dir = (v1 / abs(v1) + v2 / abs(v2))
        return bisec_dir / abs(bisec_dir)  

    bis_dir_A = bisector_direction(A, B, C_)
    bis_dir_B = bisector_direction(B, A, C_)
    bis_dir_C = bisector_direction(C_, A, B)

    def calcularea_partii(point, line_point, line_direction):
        to_point = point - line_point
        cross = (to_point.real * line_direction.imag - to_point.imag * line_direction.real)
        return cross > 0

    for z in C.screenAffixes():
        side_A = calcularea_partii(z, A, bis_dir_A)
        side_B = calcularea_partii(z, B, bis_dir_B)
        side_C = calcularea_partii(z, C_, bis_dir_C)

        region = (side_A << 2) + (side_B << 1) + side_C

        colors = [
            Color.Crimson,  
            Color.Darkblue,  
            Color.Lightgreen,  
            Color.Crimson,  
            Color.Plum,  
            Color.Lightyellow,  
            Color.Wheat,  
            Color.Lavender  
        ]

        C.setPixel(z, colors[region])

    C.drawLine(A, B, Color.Black)
    C.drawLine(B, C_, Color.Black)
    C.drawLine(C_, A, Color.Black)



def triunghi_circumscris():
    R = 6
    C.setXminXmaxYminYmax(-R, R, -R, R)

    centru_cerc = complex(0, 0)  
    raza_cerc = 4.2

    A = centru_cerc + cmath.rect(raza_cerc, math.radians(90))  
    B = centru_cerc + cmath.rect(raza_cerc, math.radians(210))  
    C_ = centru_cerc + cmath.rect(raza_cerc, math.radians(330))  

    def which_side_of_line(point, line_start, line_end):
        v1 = line_end - line_start
        v2 = point - line_start
        cross = v1.real * v2.imag - v1.imag * v2.real
        return cross > 0

    def inside_circle(point, center, radius):
        return abs(point - center) <= radius

    for z in C.screenAffixes():
        side_AB = which_side_of_line(z, A, B)  
        side_BC = which_side_of_line(z, B, C_)  
        side_CA = which_side_of_line(z, C_, A)  

        inside_circ = inside_circle(z, centru_cerc, raza_cerc)

        if inside_circ:
            if side_AB and side_BC and side_CA:
                region = 0  
            elif side_AB and side_BC and not side_CA:
                region = 1  
            elif side_BC and side_CA and not side_AB:
                region = 2  
            elif side_CA and side_AB and not side_BC:
                region = 3  
            else:
                region = 0  
        else:
            if side_AB and side_BC and side_CA:
                region = 4  
            elif side_AB and side_BC and not side_CA:
                region = 5
            elif side_BC and side_CA and not side_AB:
                region = 6  
            elif side_CA and side_AB and not side_BC:
                region = 7  
            elif side_AB and not side_BC and not side_CA:
                region = 8  
            elif not side_AB and side_BC and not side_CA:
                region = 9  
            elif not side_AB and not side_BC and side_CA:
                region = 4  
            else:
                region = 4  

        colors = [
            Color.Darkgreen,  
            Color.Crimson,  
            Color.Blue,  
            Color.Darkblue,  
            Color.Purple,  
            Color.Purple,  
            Color.Violet,  
            Color.Orange,  
            Color.Lightyellow,  
            Color.Cornflowerblue  
        ]

        C.setPixel(z, colors[region])

    C.refreshScreen()

def recDraw(a, b, c, index):
    if index <= 20:
        recDraw(a, b, c, index + 1)
    C.drawNgon([a, b, c], Color.Navy)



def Mijloace():
    C.fillScreen()
    C.setXminXmaxYminYmax(0, 10, 0, 10)
    a = 1 + 1j
    b = 9 + 2j
    c = 5 + 9j
    col = Color.Navy

    for i in range(0, 20):
        C.drawNgon([(a), (b), (c)], col)
        aa = a
        bb = b
        cc = c
        a = aa * 4 / 5 + bb * 1 / 5
        b = bb * 4 / 5 + cc * 1 / 5
        c = cc * 4 / 5 + aa * 1 / 5


def prob2():
    C.setXminXmaxYminYmax(-10, 10, -10, 10)
    a = 0 + 1j
    b = 1 / 2 + 0j
    c = -1 / 2 + 0j
    aa = a
    bb = b
    cc = c
    for i in range(0, 12):
        C.drawNgon([a, b, c], Color.Navy)
        a = aa * 1.12 - cc * 0.20
        b = bb * 1.12 - aa * 0.20
        c = cc * 1.12 - bb * 0.20
        aa = a
        bb = b
        cc = c
    C.drawNgon([a, b, c], Color.Navy)

def vf_120(A, B, opposite):
    mij = (A + B) / 2
    v = B - A
    L = abs(v)
    h = L / (2 * math.sqrt(3))  
    u = v * 1j / abs(v)  

    cp = (B - A).real * (opposite - A).imag - (B - A).imag * (opposite - A).real
    if cp > 0:
        return mij - h * u
    else:
        return mij + h * u


def ex2():
    C.setXminXmaxYminYmax(-2,2, -2, 2)
    C.fillScreen(Color.Whitesmoke)

    zA = 0 + 1j
    zB = 1 - 1j
    b = math.sin(math.radians(50)) / math.sin(math.radians(100))
    zC = b * (math.cos(math.radians(30)) + 1j * math.sin(math.radians(30)))

    C.drawNgon([zA, zB, zC], Color.Black)
    C.setText("A", zA, Color.Black, 16)
    C.setText("B", zB, Color.Black, 16)
    C.setText("C", zC, Color.Black, 16)


    zD = vf_120(zA, zB, zC)
    C.drawNgon([zA, zB, zD], Color.Red)

    zE = vf_120(zB, zC, zA)
    C.drawNgon([zB, zC, zE], Color.Green)

    zF = vf_120(zC, zA, zB)
    C.drawNgon([zC, zA, zF], Color.Blue)

    Aprim = zE 
    Bprim = zF 
    Cprim = zD 

    C.drawNgon([Aprim, Bprim, Cprim], Color.Purple)
    C.setText("A'", Aprim, Color.Black, 16)
    C.setText("B'", Bprim, Color.Black, 16)
    C.setText("C'", Cprim, Color.Black, 16)

    C.refreshScreen()


def bazaUnghiUnghi(zB, zC, uB, uC, peStg=True):

    if not peStg:
        uB, uC = -uB, -uC
    d = zC - zB
    L = abs(d)
    AB = L * math.sin(uC)
    base_angle = math.atan2(d.imag, d.real)
    angle = base_angle + uB  
    A = zB + AB * complex(math.cos(angle), math.sin(angle))
    return A


def desenare2():
    
    C.setXminXmaxYminYmax(-8, 13, -12, 12)
    C.fillScreen(Color.Whitesmoke)

    a = 13.0  
    n_tri = 13

    spiral_points = []
    for idx in range(n_tri + 1):
        if idx % 2 == 0:
            sign = (-1) ** (idx // 2)
            x = sign * a / (math.sqrt(3) ** idx)
            y = 0
            V = complex(x, y)
        else:
            sign = (-1) ** ((idx - 1) // 2)
            x = 0
            y = sign * a / (math.sqrt(3) ** idx)
            V = complex(x, y)
        spiral_points.append(V)

    for i in range(len(spiral_points) - 1):
        tri_points = [spiral_points[i], 0 + 0j, spiral_points[i + 1]]
        C.drawNgon(tri_points, Color.Red)

    for i in range(len(spiral_points) - 1):
        C.drawLine(spiral_points[i], spiral_points[i + 1], Color.Blue)

    C.refreshScreen()



def unCercQR(q, r, N):
    alfa = 2 * math.pi / N
    return [q + C.fromRhoTheta(r, k * alfa) for k in range(N)]


def Mediatoare():
    C.setXminXmaxYminYmax(0, 10, 0, 10)
    zA = 2 + 2.5j
    zB = 8 + 2.5j
    zC = 3.5 + 9j

    sq_len_a = abs(zB - zC) ** 2
    sq_len_b = abs(zC - zA) ** 2
    sq_len_c = abs(zA - zB) ** 2

    alpha = sq_len_a * (sq_len_b + sq_len_c - sq_len_a)
    beta = sq_len_b * (sq_len_c + sq_len_a - sq_len_b)
    gamma = sq_len_c * (sq_len_a + sq_len_b - sq_len_c)

    denominator = alpha + beta + gamma
    C.setAxis()
    z0 = (alpha * zA + beta * zB + gamma * zC) / denominator

    for z in C.screenAffixes():
        za = C.rho(z - zA)
        zb = C.rho(z - zB)
        zc = C.rho(z - zC)
        k = 0
        if za < zb:
            k += 1
        if zb < zc:
            k += 2
        if zc < za:
            k += 4
        C.setPixel(z, Color.Index(600 + 50 * k))
    C.drawLine(z0, zA, Color.Black)
    C.drawLine(z0, zB, Color.Black)
    C.drawLine(z0, zC, Color.Black)
    C.drawNgon([zA, zB, zC], Color.Red)
    C.drawNgon(unCercQR(z0, abs(z0 - zA), 1000), Color.Red)




def LocGeomI():
    def cercInscris(zA, zB, zC):
        a = C.rho(zB - zC)
        b = C.rho(zC - zA)
        c = C.rho(zA - zB)
        p = (a + b + c) / 2
        S = math.sqrt(p * (p - c) * (p - b) * (p - a))
        zI = (a * zA + b * zB + c * zC) / (a + b + c)
        r = S / p
        return zI, r

    C.setXminXmaxYminYmax(-10, 10, -10, 10)
    q = 0
    R = 7
    nrPuncte = 720
    delta = 2 * math.pi / nrPuncte
    nB = nrPuncte // 2 + nrPuncte // 15
    nC = nrPuncte - nrPuncte // 15
    zB = C.fromRhoTheta(R, nB * delta)
    zC = C.fromRhoTheta(R, nC * delta)

    for n in range(10 * nrPuncte):
        C.fillScreen(Color.White)
        C.setNgon(unCercQR(q, R, nrPuncte), Color.Navy)
        zA = C.fromRhoTheta(R, n * delta)
        C.drawNgon([zA, zB, zC], Color.Navy)
        zI, r = cercInscris(zA, zB, zC)
        C.setNgon(unCercQR(zI, r, 300), Color.Green)
        C.drawNgon([zA, zI, zB, zI, zC, zI], Color.Green)
        if C.mustClose():
            return


###################################################################

def LocGeomH():
    def ortocentru(zA, zB, zC):

        sq_len_a = abs(zB - zC) ** 2
        sq_len_b = abs(zC - zA) ** 2
        sq_len_c = abs(zA - zB) ** 2

        alpha = (sq_len_c + sq_len_a - sq_len_b) * (sq_len_a + sq_len_b - sq_len_c)
        beta = (sq_len_a + sq_len_b - sq_len_c) * (sq_len_c + sq_len_b - sq_len_a)
        gamma = (sq_len_c + sq_len_b - sq_len_a) * (sq_len_b + sq_len_c - sq_len_a)
        if (alpha + beta + gamma != 0):
            zH = (alpha * zA + beta * zB + gamma * zC) / (alpha + beta + gamma)
        else:
            zH = 0
        return zH

    C.setXminXmaxYminYmax(-10, 10, -12, 8)
    q = 0
    R = 6
    nrPuncte = 720
    delta = 2 * math.pi / nrPuncte
    nB = nrPuncte // 2 + nrPuncte // 15
    nC = nrPuncte - nrPuncte // 15
    zB = C.fromRhoTheta(R, nB * delta)
    zC = C.fromRhoTheta(R, nC * delta)
    lista_puncte = []

    for n in range(10 * nrPuncte):

        if n % nrPuncte == nB or n % nrPuncte == nC:
            continue
        C.fillScreen(Color.White)
        for x in lista_puncte:
            C.setPixel(x, Color.Red)

        C.setNgon(unCercQR(q, R, nrPuncte), Color.Navy)
        zA = C.fromRhoTheta(R, n * delta)
        C.drawNgon([zA, zB, zC], Color.Navy)
        zH = ortocentru(zA, zB, zC)
        lista_puncte.append(zH)
        C.drawNgon([zA, zH, zB, zH, zC, zH], Color.Green)
        if C.mustClose():
            return

##################################################################################################TEMA 8

def HeptaPentagon2():
    def npGonQA(q, a0, n, p=1):
        theta = p * 2.0 * math.pi / n
        return [q + C.fromRhoTheta(1, k * theta) * (a0 - q) for k in range(n)]

    def bazaApex(zB, zC, uA, peStg=True):
        omegaA = C.fromRhoTheta(1, uA) if peStg else C.fromRhoTheta(1, -uA)
        zA = (zC - omegaA * zB) / (1 - omegaA)
        return zA

    def construiestePoligoanePeLaturi(poligoane, nExt, thetaExt, culoare):
        poligoaneNoi = []
        for poligon in poligoane:
            for k in range(len(poligon) - 1):
                qk = bazaApex(poligon[k], poligon[k + 1], thetaExt, False)
                pentagon = npGonQA(qk, poligon[k], nExt)
                pentagon.append(pentagon[0])
                C.drawNgon(pentagon[:-1], culoare)
                poligoaneNoi.append(pentagon)
        return poligoaneNoi

    def construiestePeVarfuriExterioareConsecutive(poligoane, nExt, thetaExt, culoare, centru=0):
        poligoaneNoi = []

        for i in range(len(poligoane) - 1):
            p1 = poligoane[i][:-1]  
            p2 = poligoane[i + 1][:-1]

            z1 = max(p1, key=lambda z: abs(z - centru))
            z2 = max(p2, key=lambda z: abs(z - centru))

            qk = bazaApex(z1, z2, thetaExt, peStg=False)

            pentagon = npGonQA(qk, z1, nExt)
            pentagon.append(pentagon[0])

            C.drawNgon(pentagon[:-1], culoare)
            poligoaneNoi.append(pentagon)

        return poligoaneNoi

    C.setXminXmaxYminYmax(-5, 5, -5, 5)
    C.fillScreen()

    q = 0
    a = 2
    nInt = 7
    nExt = 5
    thetaExt = 2 * math.pi / nExt
    numarIteratii = 1

    pInt = npGonQA(q, a, nInt)
    pInt.append(pInt[0])
    C.drawNgon(pInt[:-1], Color.Black)

    poligoaneCurente = [pInt]
    culori = [Color.Red, Color.Green, Color.Purple, Color.Orange, Color.Yellow]

    culoare1 = culori[0 % len(culori)]
    poligoanel1 = construiestePoligoanePeLaturi(poligoaneCurente, nExt, thetaExt, culoare1)

    if len(poligoanel1) >= 2:
        construiestePeVarfuriExterioareConsecutive(poligoanel1, nExt, thetaExt, Color.Black)






def HeptaPentagon3():
    def npGonQA(q, a0, n, p=1):
        theta = p * 2.0 * math.pi / n
        return [q + C.fromRhoTheta(1, k * theta) * (a0 - q) for k in range(n)]

    def bazaApex(zB, zC, uA, peStg=True):
        omegaA = C.fromRhoTheta(1, uA) if peStg else C.fromRhoTheta(1, -uA)
        zA = (zC - omegaA * zB) / (1 - omegaA)
        return zA

    def construiestePoligoanePeLaturi(poligoane, nExt, thetaExt, culoare):
        poligoaneNoi = []
        for poligon in poligoane:
            for k in range(len(poligon) - 1):
                qk = bazaApex(poligon[k], poligon[k + 1], thetaExt, False)
                pentagon = npGonQA(qk, poligon[k], nExt)
                pentagon.append(pentagon[0])
                C.fillNgon(pentagon[:-1], culoare)
                poligoaneNoi.append(pentagon)
        return poligoaneNoi

    def construiestePoligoanePeVarfuriExterioare(petaleRand1, nExt, thetaExt, culoare, centru=0):
        poligoaneNoi = []

        for i in range(len(petaleRand1)):
            p1 = petaleRand1[i]
            p2 = petaleRand1[(i + 1)%len(petaleRand1)]

            z1 = max(p1[:-1], key=lambda z: abs(z - centru))
            z2 = max(p2[:-1], key=lambda z: abs(z - centru))

            qk = bazaApex(z1, z2, thetaExt, peStg=False)

            pentagon = npGonQA(qk, z1, nExt)
            pentagon.append(pentagon[0])

            C.fillNgon(pentagon[:-1], culoare)
            poligoaneNoi.append(pentagon)

        return poligoaneNoi

    
    C.setXminXmaxYminYmax(-5, 5, -5, 5)
    C.fillScreen()

    q = 0
    a = 2
    nInt = 7       
    nExt = 5       
    thetaExt = 2 * math.pi / nExt

    pInt = npGonQA(q, a, nInt)
    pInt.append(pInt[0])

    culoareRand1 = Color.Wheat  
    petaleRand1 = construiestePoligoanePeLaturi([pInt], nExt, thetaExt, culoareRand1)

    culoareRand2 = Color.Lightpink
    construiestePoligoanePeVarfuriExterioare(petaleRand1, nExt, thetaExt, culoareRand2)

###########################################################################################TEMA 9

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


############################################################################################TEMA 10

def pentagoane(centru=0j, raza=1.0):
    varfuri = []
    for k in range(5):
        angle = 2 * math.pi * k / 5 - math.pi / 2  # începem de sus
        vf = centru + raza * cmath.exp(1j * angle)
        varfuri.append(vf)
    return varfuri


def Fulg_Koch(start, fin, theta=math.pi / 3, lam=1.0 / 3, nrIter=15):
    if nrIter == 0:
        return [start, fin]

    dir = fin - start
    length = abs(dir)
    unit_dir = dir / length if length > 0 else 1

    A = start
    B = start + lam * dir
    D = start + (1 - lam) * dir
    E = fin

    BD = D - B
    BD_rotit = BD * cmath.exp(1j * theta)
    C = B + BD_rotit

    points = []
    points.extend(Fulg_Koch(A, B, theta, lam, nrIter - 1)[:-1])
    points.extend(Fulg_Koch(B, C, theta, lam, nrIter - 1)[:-1])
    points.extend(Fulg_Koch(C, D, theta, lam, nrIter - 1)[:-1])
    points.extend(Fulg_Koch(D, E, theta, lam, nrIter - 1))

    return points


"""
def pentagonKoch():

    #Desenează pentagonul lui Koch cu curbe Koch pe fiecare latură
    C.setXminXmaxYminYmax(-2.5, 2.5, -2.5, 2.5)
    C.fillScreen(Color.White)

    # parametrii
    theta = math.pi / 3 
    lam = 1.0 / 3  
    nrIter = 4  

    # Generăm vârfurile pentagonului
    varfuri = vf_pentagon(centru=0j, raza=1.5)

    # Pentru fiecare latură a pentagonului, desenăm o curbă Koch
    colors = [Color.Red, Color.Blue, Color.Green, Color.Orange, Color.Purple]

    for i in range(5):
        vf_start = varfuri[i]
        vf_fin = varfuri[(i + 1) % 5]

        # Generăm curba Koch pentru această latură
        pct_koch = curba_koch_generalizata(vf_start, vf_fin, theta, lam, nrIter)

        # Desenăm curba punct cu punct
        color = colors[i % len(colors)]
        for j in range(len(pct_koch) - 1):
            C.drawLine(pct_koch[j], pct_koch[j + 1], color)

            # Verificăm dacă trebuie să oprim desenarea
            if C.mustClose():
                return
"""


def pentagon():
    C.setXminXmaxYminYmax(-2.2, 2.2, -2.2, 2.2)
    C.fillScreen(Color.Whitesmoke)

    theta = math.pi / 3  
    lam = 1.0 / 3
    nrIter = 4

    centru = 0j
    raza = 1.8

    varfuri = pentagoane(centru=centru, raza=raza)

    colors = [Color.Red, Color.Blue, Color.Green, Color.Orange, Color.Purple]

    for i in range(5):
        vf_start = varfuri[i]
        vf_fin = varfuri[(i + 1) % 5]

        pct_koch = Fulg_Koch(vf_start, vf_fin, theta, lam, nrIter)

        color = colors[i]
        for j in range(len(pct_koch) - 1):
            C.drawLine(pct_koch[j], pct_koch[j + 1], color)

            if C.mustClose():
                return


################################################

def pentagon_baza(R):
    pent = [R * math.e ** (1j * (math.pi / 2 + 2 * math.pi * k / 5)) for k in range(5)]
    pent.append(pent[0])
    return pent


def poligon(varfuri, color):
    for i in range(1, len(varfuri)):
        C.drawLine(varfuri[i - 1], varfuri[i], color)


def Sierpinski(a, b, lvl, r, P0, adancime):
    # a, b - parametrii transformarii curente (T(z)= a*z+b);
    # lvl – adancimea recursiei;
    # r      – factorul de contracție
    # P0     – lista de vf a pentagonului de bază
    # adancime  – adâncimea actuală, its useful for color

    if lvl == 0:
        polig = [a * v + b for v in P0]
        # Se alege culoarea în funcție de adâncimea recursiei curente.
        poligon(polig, Color.Index((adancime + 100) % 5))
    else:
        for i in range(5):
            # T_new(z) = r*(a*z+b) + (1-r)*P0[i]
            anou = r * a
            bnou = r * b + (1 - r) * P0[i]
            Sierpinski(anou, bnou, lvl - 1, r, P0, adancime + 1)


def SierpinskiPentagon():
    C.setXminXmaxYminYmax(-1.5, 1.5, -1.5, 1.5)
    C.fillScreen()

    R = 1.0
    # baza = un pentagon regulat centrat la 0.
    P0 = pentagon_baza(R)

    # factorul de contracție
    r = (3 - math.sqrt(5)) / 2.0  # ≈ 0.382

    lvl_maxim = 4

    # T(z) = 1*z + 0.
    Sierpinski(1, 0, lvl_maxim, r, P0, 0)

    C.refreshScreen()
    while not C.mustClose():
        C.wait(50)

####################################################################################TEMA 11
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


####################################################################################TEMA 12

def Newton4prim1():
    eps0 = C.fromRhoTheta(1.0,  math.pi / 4.0)
    eps1 = C.fromRhoTheta(1.0, 3.0 * math.pi / 4.0)
    eps2 = C.fromRhoTheta(1.0, 5.0 * math.pi / 4.0)
    eps3= C.fromRhoTheta(1.0, 7.0*math.pi/4.0)
    def f(z):
        return z-(z**4+1)/(4*z**3) if z != 0 else 10e10

    c0 = 0
    r = 2
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




def Newton3prim():
    eps0 = C.fromRhoTheta(1.0, 0.0 * math.pi / 3.0)
    eps1 = C.fromRhoTheta(1.0, 2.0 * math.pi / 3.0)
    eps2 = C.fromRhoTheta(1.0, 4.0 * math.pi / 3.0)

    def f(z):
        if z == 0:
            return 1.0e100
        else:
            return (2 * z * z * z + 1) / (3 * z * z)

    C.setXminXmaxYminYmax(-2, 2, -2, 2)
    nrIter = 300
    for coloana in C.screenColumns():
        for zeta in coloana:
            col = Color.Black
            z = zeta
            if z!=0:
                z=1/z
            for _ in range(nrIter):
                if C.rho(z - eps0) < 0.1:
                    col = Color.Darkblue
                    break
                if C.rho(z - eps1) < 0.1:
                    col = Color.Yellow
                    break
                if C.rho(z - eps2) < 0.1:
                    col = Color.Fuchsia
                    break
                z = f(z)
            C.setPixel(zeta, col)
        if C.mustClose(): return
    C.setAxis(Color.White)
    C.refreshScreen()

########################################################################################TEMA 13

def JuliaBazine():
    c = -0.21 - 0.7j

    def f(z):
        return z * z + c

    C.setXminXmaxYminYmax(-1.5, 1.5, -1.5, 1.5)
    C.fillScreen(Color.Black)
    nrIter = 1001 + 18
    rhoMax = 1.0e2
    for coloana in C.screenColumns():
        for zeta in coloana:
            z = zeta
            for k in range(nrIter):
                if abs(z) >= rhoMax: break
                z = f(z)
            if abs(z) < rhoMax:
                color = Color.Index(10 * sum(C.getHK(z)) + 200)
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
        return z ** (1.5) + c

    C.setXminXmaxYminYmax(x0 - l, x0 + l, y0 - l, y0 + l)
    nrIter = 1000
    for coloana in C.screenColumns():
        for zeta in coloana:
            z = zeta
            for k in range(nrIter):
                if C.rho(z) > 4: break
                z = f(z)
            C.setPixel(zeta, Color.Index(100 + 5 * k))
        if C.mustClose():
            return



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
                # C.setPixel(z, col)
        if C.mustClose():
            return

if __name__ == '__main__':
    C.initPygame()
    # C.run(Bisectoare)
    # C.run(triunghi_circumscris)
    # C.run(Mijloace)
    # C.run(prob2)
    # C.run(bazaUnghiUnghi)
    # C.run(desenare2)
    # C.run(Mediatoare)
    # C.run(LocGeomI)
    # C.run(LocGeomH)
    # C.run(HeptaPentagon2)
    # C.run(HeptaPentagon3)
    # C.run(GoldenRatio2024)
    # C.run(PseudoSpiralaLuiArhimede)
    # C.run(pentagon)
    # C.run(SierpinskiPentagon)
    # C.run(HilberTriunghi)
    # C.run(TriunghiLinie)
    C.run(Newton3prim)
    C.run(Newton4prim1)
    # C.run(Glyyn)
    # C.run(JuliaFinal)
    # C.run(JuliaPlina2)
