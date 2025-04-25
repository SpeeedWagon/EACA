import ComplexPygame as C
import Color
import random
import math
import cmath
def Nisshoki():
    C.setXminXmaxYminYmax(-2, 2, -2, 2)
    r = 3.0 / 5.0
    for z in C.screenAffixes():
        col = Color.Cyan
        cPx = C.getHK(z)
        #componenta [0] este orizontala componenta [1] este verticala
        #and (C.dim//9< cPx[1] < 4*C.dim//9)
        if((C.dim//8<= cPx[0] <= 7*C.dim//8) and (C.dim//4< cPx[1] < 3* C.dim//4)):
            col = Color.White
        if abs(z) < r: 
            col = Color.Crimson
        C.setPixel(z, col)
    
    # C.setAxis()
    C.refreshScreen()

def MasterCard():
    C.setXminXmaxYminYmax(-2, 2, -2, 2)
    r = 3.0 / 5.0
    for z in C.screenAffixes():
        col = Color.Cyan
        cPx = C.getHK(z)
        #componenta [0] este orizontala componenta [1] este verticala
        #and (C.dim//9< cPx[1] < 4*C.dim//9)
        ratio = 3/5
        if(C.dim//6< cPx[1] < 5* C.dim//6):
            col = Color.White
        if(abs(z+ratio)<1):
            col = Color.Red
        if(abs(z-ratio)<1):
            col = Color.Orange
        if(abs(z-ratio)<1 and abs(z+ratio)<1):
            col = '#FF5F00'
        #The intersection of these two circles creates a darker orange shade. 
        # The official Mastercard brand guidelines specify this intersection color as #FF5F00.
        C.setPixel(z, col)
    
    # C.setAxis()
    C.refreshScreen()

def DrapelHK():
    C.fillScreen()
    for h in range(C.dim):
        for k in range(C.dim):
            col = Color.Aqua
            if C.dim // 6< k < 5 * C.dim // 6:
                if h < C.dim // 3:
                    col = 0, 43, 127 # albastru cobalt
                elif h < 2 * C.dim // 3:
                    col = 252, 209, 22 # galben crom
                else:
                    col = 206, 17, 38 # rosu vermillon
            C.setPixelHK(h, k, col)
        C.refreshScreen()
    print("gata")

def Cercuri():
    C.setXminXmaxYminYmax(-10, 10, -10, 10)
    r = 3.0 / 2
    col = Color.Cyan
    #setez centrele 
    n = 3
    c1 = [k/10 for k in random.sample(range(-30,30), n+1)]
    c2 = [k/10 for k in random.sample(range(-30,30), n+1)]
    c = [complex(c1[x],c2[x]) for x in range(n)]
    p = [c1[n],c2[n]]
    r = [math.sqrt(x.real**2 + x.imag**2) for x in c]
    #abs(z+c[0]) < r[0]
    #abs(z+c[1]) < r[1]
    #abs(z+c[2]) < r[2]
    colors = [Color.Index(x) for x in random.sample(range(0,1000), n*2)]
    for z in C.screenAffixes():
        col = Color.Cyan
        if abs(z+c[0]) < r[0]:
            col = colors[0]
        if abs(z+c[2]) < r[2]:
            col = colors[1]
        if abs(z+c[1]) < r[1]:
            col = colors[2]
        if abs(z+c[1]) < r[1] and abs(z+c[2]) < r[2]:
            col = colors[3]
        if abs(z+c[0]) < r[0] and abs(z+c[1]) < r[1]:
            col = colors[4]
        if abs(z+c[0]) < r[0] and abs(z+c[2]) < r[2]:
            col = colors[5]

        C.setPixel(z, col)

def min_element_index(arr):
  return arr.index(min(arr))


def DiagramaVoronoi():
    C.setXminXmaxYminYmax(-10, 10, -10, 10)
    r = 3.0 / 2
    col = Color.Cyan
    #setez centrele 
    n = 20
    c1 = [k/10 for k in random.sample(range(-100,100), n)]
    c2 = [k/10 for k in random.sample(range(-100,100), n)]
    c = [complex(c1[x],c2[x]) for x in range(n)]
    print(c)
    # r = [math.sqrt(x.real**2 + x.imag**2) for x in c]
    colors = [Color.Index(x) for x in random.sample(range(0,1000), n)]
    for z in C.screenAffixes():
        col = Color.Cyan
        distante = [math.sqrt((z.real- x.real)**2 + (z.imag-x.imag)**2) for x in c]
        # print(distante)
        col = colors[min_element_index(distante)]
        # for i in range(n):
        #     if(abs(z+c[i])<1/10):
        #          col = Color.Black
        C.setPixel(z,col)



def Darts():
    R = 6
    C.setXminXmaxYminYmax(-R, R, -R, R)
    N = 5
    
    for z in C.screenAffixes():
        if(abs(z)>=R):
            col = Color.Black
        else:
            nTheta = round(N * (1 + C.theta(z) / math.pi))
            if(math.floor(abs(z)%2)):
                col = Color.Green
                if nTheta % 2 == 0: col = Color.Whitesmoke
            else:
                col = Color.Whitesmoke
                if nTheta % 2 == 0: col = Color.Green
            
        C.setPixel(z, col)
    C.refreshScreen()
    return


def Bisectoare():
    R = 2
    C.setXminXmaxYminYmax(-R, R, -R, R)
    n = 3
  
    c1 = [k/2+0.2 for k in random.sample(range(-R,R), n)]
    c2 = [k/2+0.5 for k in random.sample(range(-R,R), n)]
    c = [complex(c1[x],c2[x]) for x in range(n)]
    a = ((c[1].real - c[2].real)**2 + (c[1].imag - c[2].imag)**2) ** 0.5
    b = ((c[0].real - c[2].real)**2 + (c[0].imag - c[2].imag)**2) ** 0.5
    d = ((c[1].real - c[0].real )**2 + (c[1].imag  - c[0].imag )**2) ** 0.5
    Ix = (a*c[0].real + b*c[1].real + d*c[2].real) / (a + b + d)
    Iy = (a*c[0].imag + b*c[1].imag + d*c[2].imag) / (a + b + d)
    bis = complex(Ix,Iy)
    C.fillScreen()

    C.drawLine(c[1],c[2],Color.Black)
    C.drawLine(c[0],c[2],Color.Black)
    C.drawLine(c[0],c[1],Color.Black)
    C.drawLine(c[0],bis,Color.Black)
    C.drawLine(c[1],bis,Color.Black)
    C.drawLine(c[2],bis,Color.Black)
    print()
   
    C.refreshScreen()

def mySqrt(z):
    rho = abs(z)
    theta = cmath.phase(z)
    return cmath.rect(math.sqrt(rho), theta / 2)

def ecGr2(a,b,c):
    delta = b**2 - 4 * a * c
    z1 = (-b + mySqrt(delta))/2*a
    z2 = (-b - mySqrt(delta))/2*a
    return z1, z2

def mult_rec(ord,alpha):
    sm = 1
    for x in range(0,ord):
        sm*=(alpha-x)
    return sm

def seriaBinomiala(z):
    alpha = 1/2
    sum = 1
    for x in range(1,20):
        sum+=mult_rec(x,alpha)*(z**x)/math.factorial(x)
    return sum


def HyperTrochoida():
    C.fillScreen(Color.Navy)
    C.setXminXmaxYminYmax(-1.3, 1.3, -1.3, 1.3)
    r1 = 1
    r2 = 1/21
    h = 2/9
    omega1 = 0.011
    omega2 = 1.5005 * omega1
    fi = 0.1
    for t in range(10 ** 10):
        x = (r1-r2)*math.cos(t) + h*math.cos((r1-r2)/r2*t) 
        y = (r1-r2)*math.sin(t) - h*math.sin((r1-r2)/r2*t )
        C.setPixelXY(x, y, Color.Index(t // 5000))
        if t % 10000 == 0 and C.mustClose():
            break
    print(f"GATA")


def Spirala():
    # def z(t):
    #     return -t * (cos(t) + sin(t) * 1j)
    def z2(t):
        return complex( -t*math.cos(t) ,-t*math.sin(t) )
    def zprim(t):
        return math.cos(t) + math.sin(t) * 1j + t * (-math.sin(t) + math.cos(t) * 1j)
    C.setXminXmaxYminYmax(-50, 50, -50, 50)
    for z in C.screenAffixes():
        C.setPixel(z,Color.Cyan)

    for k in range(314159):
        tk = 0.0001 * k
        # print(dist)
        C.setPixel(z2(tk), Color.Black)
        # angl = C.theta(z(tk))
        C.drawNgon([z2(tk),1*(z2(tk-2*math.pi)),z2(tk+0.012),1*(z2(tk-2*math.pi+0.012))],Color.Index(math.floor(tk*12   *2*math.pi)))
        # C.drawLine(z2(tk),1*(z2(tk-2*math.pi)),Color.Index(math.floor(tk*10   *2*math.pi)))
        C.setPixel(z2(tk), Color.Blue)
        if(k%200==0):
            C.refreshScreen()
    for k in range(314159):
        tk = 0.0001 * k
        # print(dist)
        C.setPixel(z2(tk), Color.Black)
        # angl = C.theta(z(tk))
        C.drawNgon([z2(tk),1*(z2(tk-2*math.pi)),z2(tk+0.012),1*(z2(tk-2*math.pi+0.012))],Color.Cyan)
        # C.drawLine(z2(tk),1*(z2(tk-2*math.pi)),Color.Index(math.floor(tk*10   *2*math.pi)))
        C.setPixel(z2(tk), Color.Blue)
        if(k%200==0):
            C.refreshScreen()
    # t0 = 32
    # z0 = z(t0)
    # C.drawLine(z0, z0 + zprim(t0), Color.Red)



if __name__ == '__main__':
    C.initPygame()
    # TEMA 1
    # mySqrt
    # ecGr2
    # TEMA 2
    # C.run(Spirala)
    # C.run(HyperTrochoida)
    # TEMA 3
    # C.run(Cercuri)
    # C.run(DiagramaVoronoi)
    # C.run(MasterCard)
    # C.run(Nisshoki)
    # TEMA 4
    C.run(Darts)