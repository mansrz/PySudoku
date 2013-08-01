import random
class Generador:

    def __init__(self):
        self.tablero=[]*80
        for i in range(9):
            for j in range(9):
             self.tablero.insert(i*9+j,0)
        self.generarSolucionRandom()
        #for i in range (10):




    def generarSolucionRandom(self):
        resolver=False
        num_de_Random = 50
        j=0
        while not resolver:
            random.seed(0)
            while j<num_de_Random:
                x=random.randint(0,8)
                y=random.randint(0,8)
                v=random.randint(1,9)
                print(x,y,v)
                if self.MovimientoValido(x, y, v):
                     self.SetValor(x, y, v)
                     j+=1
            resolver=self.resolverTablero()


    def resolverTablero(self):
        resuelto = False
        esvalido=self.esValido()
        if esvalido:
            resuelto=self.escanearSolucion()
            resuelto=self.BackTrackSolucion(0,0)
        return resuelto

    def esValido(self):
        return self.ValidarVertical() & self.ValidarHorizontal() & self.ValidarBloque()

    def ValidarVertical(self):
        elementosVerticales=[]
        valido = True
        for j in range (10):
            elementosVerticales.insert(j,False)
        for i in range (9):
            if valido==False:
                break
            else:
                for j in range(9):
                    if valido:
                        curElem = self.tablero[(i*9)+j]
                        if elementosVerticales[curElem]:
                            valido=False
                        else:
                            valido=True
                        if (curElem != 0):
                            elementosVerticales[curElem] = True
                    else:
                        break
                    for k in range(10):
                        elementosVerticales[k] = False
        return valido

    def ValidarHorizontal(self):
        elementosVerticales=[]
        valido = True
        for j in range (10):
            elementosVerticales.insert(j,False)
        for i in range (9):
            if valido==False:
                break
            else:
                for j in range(9):
                    if valido:
                        curElem = self.tablero[(j*9)+i]
                        if elementosVerticales[curElem]:
                            valido=False
                        else:
                            valido=True
                        if (curElem != 0):
                            elementosVerticales[curElem] = True
                    else:
                        break
                    for k in range(10):
                        elementosVerticales[k] = False
        return valido

    def ValidarBloque(self):
        elementosBloque=[]
        startX=0
        startY=0
        i=0
        j=0
        valido = True
        for j in range(10):
            elementosBloque.insert(j,False)
        while startX<9 & valido:
            while startY<9 & valido:
                while valido &( i % 3 != 0 | i == startX):
                    while valido &( j % 3 != 0 | j == startY):
                        curElem = self.tablero[(j*9)+i]
                        if elementosBloque[curElem]:
                            valido=False
                        else:
                            valido=True
                        if (curElem != 0):
                            elementosBloque[curElem] = True
                        j+=1
                    i+=1
                for k in range(10):
                    elementosBloque[k] = False
                startY+=3
            startX += 3
        return valido;


    def escanearSolucion(self):
        encontrado = self.esValido()
        numPossible=0
        #possibleSolutions=[]*9[]*9[]*10
        possibleSolutions= [[ [ False for i in range(0,10) ] for j in range(0,9) ]for k in range(0,9)]
        for y in range (9):
            for x in range(9):
                for v in range(1,10):
                    possibleSolutions[y][x][v] = True
        completo=self.esCompleto()
        veces=0
        encontre=0
        while completo==False & encontrado:
            encontrado = False
            #for y in range(9)
            for y in range(0,9):
                for x in range(0,9):
                    numPossible = 0
                    for v in range(1,10):
                        if (possibleSolutions[x][y][v]):
                            possibleSolutions[x][y][v] = self.MovimientoValido(x, y, v)
                            if possibleSolutions[x][y][v]:
                                 numPossible+=1

                    if (numPossible == 1):

                        for v in range(1,10):
                            if(possibleSolutions[x][y][v]):
                                encontre+=1
                                self.SetValor(x, y, v)


            completo=True
            veces+=1
            encontrado = True
        return self.esCompleto();

    def esCompleto(self):
        lleno = True
        i=0
        j=0
        while lleno & i<9:
            while lleno & j<9:
                valor=self.GetValor(i,j)
                if  valor!=0:
                    lleno=True
                else:
                    lleno=False
                    return lleno
                j+=1
            i+=1
        return lleno

    def BackTrackSolucion(self,startx,starty):
        solved = self.esCompleto();
        foundzero = False;
        for x in range(startx,9):
            if not foundzero:
                for y in range(starty,9):
                    if self.tablero[x*9+y]==0:
                        foundzero=True
                        break
            else:
                break
        x-=1
        for v in range(1,10):
            if self.MovimientoValido(x,y,v):
                self.setValor(x,y,v)
                self.BackTrackSolucion(x,y+1)
            else:
                solved=False
        return False

    def SetValor(self,x,y,v ):
        self.tablero[(x*9)+y]=v;

    def MovimientoValido(self,x, y, v):
        horizontal=self.ChequearHorizontal(x, y, v)
        vertical=self.ChequearVertical(x, y, v)
        bloque=self.ChequearBloque(x, y, v)
        if horizontal & vertical & bloque:
            return True;
        else:
            return False;
    def GetValor(self,x,y):
        #valor=0
        #print("len tablero "+str(len(self.tablero))+" x*9+y " +str(x*9+y))
        if len(self.tablero)==(x*9+y):
            print("len tablero "+str(len(self.tablero))+" x*9+y " +str(x*9+y))
        valor=self.tablero[(x*9)+y]
        return valor

    def ChequearHorizontal(self,x, y, v):
        i=0
        if self.GetValor(x,y) == 0:
            valido=True
        else:
            valido=False
        while i<9:
            if i*9+y==81:
                print("fuera de indice "+str(i*9+y)+" i "+str(i)+" " + str(y))
            verdad= self.GetValor(i,y)!=v
            if (verdad==False):
                valido=False
                break
            else:
                valido=True

            i+=1

        return valido

    def ChequearVertical(self,x, y, v):
        #valido=False
        #i=0
        #if self.tablero[(x*9)+y-2] == 0:
            #valido=True
        #else:
            #valido=False
        #while i<9:
            #if self.GetValor(x,i) == v:
                #valido=False
                #break
            #else:
                #valido=True
            #i+=1
        valido = self.tablero[x*9+y]==0
        for i in range(9):
            if valido:
                valido=self.tablero[x*9+i]!=v
        return valido

    def ChequearBloque(self,x, y, v):
        if self.tablero[(x*9)+y] == 0:
            valido=True
        else:
            valido=False
        startx = x-(x % 3);
        starty = y-(y % 3);

        for i in range(starty,starty+3):
            if valido &(i % 3 != 0 | i == starty):
                for j in range(startx,startx+3):
                    if valido &(j % 3 != 0 | j == startx):
                        if self.tablero[(j*9)+i] == v:
                            valido=False
                            break
                        else:
                            valido=True

            else:
                break
        return valido

if __name__ == '__main__':
    Tablero=Generador()
    #Tablero.__init__()
    for i in range (9):
        for j in range(9):
            print(Tablero.tablero[(i*9)+j],(i*9)+j)
        print("\n")
