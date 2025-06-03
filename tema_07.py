import ComplexPygame as C
import Color
import math
def unCercQR(q, r, N):
    alfa = 2 * math.pi / N
    return [q + C.fromRhoTheta(r, k * alfa) for k in range(N)]

def Mediatoare():
    C.setXminXmaxYminYmax(0, 10, 0, 10) 
    zA = 2 + 2.5j
    zB = 8 + 2.5j
    zC = 3.5 + 9j

    sq_len_a = abs(zB - zC)**2
    sq_len_b = abs(zC - zA)**2
    sq_len_c = abs(zA - zB)**2

    alpha = sq_len_a * (sq_len_b + sq_len_c - sq_len_a)
    beta  = sq_len_b * (sq_len_c + sq_len_a - sq_len_b)
    gamma = sq_len_c * (sq_len_a + sq_len_b - sq_len_c)
   
    denominator = alpha + beta + gamma
    C.setAxis()
    z0 = (alpha*zA+beta*zB+gamma*zC)/denominator

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
    C.drawLine(z0,zA,Color.Black)
    C.drawLine(z0,zB,Color.Black)
    C.drawLine(z0,zC,Color.Black)
    C.drawNgon([zA, zB, zC], Color.Red)
    C.drawNgon(unCercQR(z0, abs(z0-zA), 1000), Color.Red)

###################################################################



def LocGeomI():

    def cercInscris(zA, zB, zC):
        # returneaza zI si r pentru cercul inscris
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
        
        sq_len_a = abs(zB - zC)**2
        sq_len_b = abs(zC - zA)**2
        sq_len_c = abs(zA - zB)**2

        alpha = (sq_len_c + sq_len_a - sq_len_b)*(sq_len_a + sq_len_b - sq_len_c)
        beta  = (sq_len_a + sq_len_b - sq_len_c) * (sq_len_c + sq_len_b - sq_len_a)
        gamma = (sq_len_c + sq_len_b - sq_len_a) * (sq_len_b + sq_len_c - sq_len_a)
        if(alpha+beta+gamma !=0):
            zH = (alpha*zA+beta*zB+gamma*zC)/(alpha+beta+gamma)
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
            C.setPixel(x,Color.Red)
        
        
        C.setNgon(unCercQR(q, R, nrPuncte), Color.Navy)
        zA = C.fromRhoTheta(R, n * delta)
        C.drawNgon([zA, zB, zC], Color.Navy)
        zH = ortocentru(zA, zB, zC)
        lista_puncte.append(zH)
        C.drawNgon([zA, zH, zB, zH, zC, zH], Color.Green)
        if C.mustClose():
            return
##########################################################
if __name__ == '__main__':
    C.initPygame()
    C.run(Mediatoare)
    # C.run(LocGeomI)
    C.run(LocGeomH)

