import ComplexPygame as C
import Color

def recDraw(a,b,c,index):
    if index <= 20:
        recDraw(a,b,c,index+1)
    C.drawNgon([a,b,c],Color.Navy)

        # C.drawNgon([(a*4/5+b*1/5), (b*4/5+c*1/5), (c*4/5+a*1/5)], Color.Navy)

def Mijloace():
    C.fillScreen()
    C.setXminXmaxYminYmax(0, 10, 0, 10)
    a = 1 + 1j
    b = 9 + 2j
    c = 5 + 9j
    col=Color.Navy
    
    for i in range(0,20):
        C.drawNgon([(a), (b), (c)], col)
        aa=a
        bb=b
        cc = c
        a=aa*4/5+bb*1/5
        b=bb*4/5+cc*1/5
        c=cc*4/5+aa*1/5
def prob2():
    C.setXminXmaxYminYmax(-10, 10, -10, 10)
    a = 0 + 1j
    b = 1/2 + 0j
    c = -1/2 + 0j
    aa = a
    bb = b
    cc = c
    for i in range(0,12):
        C.drawNgon([a, b, c], Color.Navy)
        a = aa*1.12 - cc*0.20
        b = bb*1.12 - aa*0.20
        c = cc*1.12 - bb*0.20
        aa = a
        bb = b
        cc = c
    C.drawNgon([a,b,c],Color.Navy)
if __name__ == '__main__':
    C.initPygame()
    C.run(Mijloace)
    C.run(prob2)
