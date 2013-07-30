import random

class Celda:

    def __init__(self, fila, columna, text):
        self.fila = fila
        self.columna = columna
        self.cuadricula = (fila // 3) * 3 + (columna // 3)
        self.valor = 0
        self.valorCorrecto = 0
        self.text = text

    def getValor(self):
        return self.valor

    def getValorCorrecto(self):
        return self.valorCorrecto

    def getCuadricula(self):
        return self.cuadricula

    def setText(self, text):
        self.text = text

    def setValor(self, valor):
        self.valor = valor

    def setValorCorrecto(self, valorCorrecto):
        self.valorCorrecto = valorCorrecto




class Generador:
    celda = [[Celda(fila, columna, "") for columna in range(9)] for fila in range(9)]
    tablero=[]*80
    visibles= [ True for i in range(80)]
    def __init__(self, dificultad):

        #for i in range (10):
        while (not self.checkSudokuForZero()):
            self.wipeSudokuClean()
            self.sudokuGenerator(0)

        for i in range (0,9):
            for j in range (0,9):
                self.tablero.append(self.celda[i][j].valorCorrecto)
        self.CasillasVisibles(1)



    def CasillasVisibles(self, dificultad):
        lista=[Celda(0,0,"") for i in range (40) ]
        mov_posibles=[[False for i in range(1,10)] for j in range(0,40)]
        n=40
        random.seed(0)
        j=0
        contador=0
        contador_golbal=0
        SeCumple=False
        while SeCumple!=True:
            while j<n:
                x=random.randint(0,8)
                y=random.randint(0,8)
                if self.tablero[(x*9)+y]!=0:
                    lista[j].columna=y
                    lista[j].fila=x
                    lista[j].valorCorrecto=self.tablero[(x*9)+y]
                    self.tablero[(x*9)+y]=0
                    j+=1
            for pos in range (0,40):
                for v in range(1,9):
                    mov_posibles[pos][v]=self.MovimientoValido(lista[pos].fila,lista[pos].columna,v)
            for pos in range (0,40):

                for v in range(1,9):
                    if mov_posibles[pos][v]:
                        contador+=1

                if dificultad==1:
                    if contador>0 & contador<4:
                        contador_golbal+=1
                if dificultad==2:
                    if contador>3 & contador<6:
                        contador_golbal+=1
                if dificultad==3:
                    if contador>3 & contador<8:
                        contador_golbal+=1
                contador=0
            if contador_golbal>35:
                SeCumple=True
            else:
                SeCumple=False
        for i in range (40):
            self.tablero[(lista[i].fila*9) +lista[i].columna]=lista[i].valorCorrecto
            self.visibles[lista[i].fila*9 +lista[i].columna]=False






    def validateCellAtPointerWithNumber(self,row, column, value, counter):
        i, j = 0, 0

        while i < 9:
            while j < 9:
                if(i == row or j == column or self.celda[i][j].getCuadricula() == self.celda[row][column].getCuadricula()):
                    if(self.celda[i][j].getValorCorrecto()):
                        if(value == self.celda[i][j].getValorCorrecto() and not(i == row and j == column - counter)):
                            return False

                j += 1
            j = 0
            i += 1
        return True


    def numberAssigner(self,counter, row, column, value):
        if (counter > column):
            return False
        if((not counter and self.validateCellAtPointerWithNumber(row, column, value, 0)) or (counter and self.validateCellAtPointerWithNumber(row, column, self.celda[row][column - counter].getValorCorrecto(), counter) and self.validateCellAtPointerWithNumber(row, column - counter, value, 0))):
            if(not counter):
                self.celda[row][column].setValorCorrecto(value)
            else:
                self.celda[row][column].setValorCorrecto(self.celda[row][column - counter].getValorCorrecto())
                self.celda[row][column - counter].setValorCorrecto(value)
            return True
        else:
            counter += 1
            return self.numberAssigner(counter, row, column, value)


    def sudokuGenerator(self,row):
        if (row > 8):
            return
        i, j = 0, 0
        digitArray = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        rowArray = [0] * 9
        random.shuffle(digitArray)


        flag = False
        while i < 9:
            while j < 9:
                flag = False
                if(digitArray[j] >= 1):
                    if(self.numberAssigner(0, row, i, digitArray[j])):
                        digitArray[j] = -1
                        flag = True

                if(flag):
                    break
                j += 1
            j = 0
            i += 1

        for index in range(9):
            rowArray[index] = self.celda[row][index].getValorCorrecto()

        self.sudokuGenerator(row + 1)


    def checkSudokuForZero(self):
        i, j = 0, 0

        while i < 9:
            while j < 9:
                if (not self.celda[i][j].getValorCorrecto()):
                    return False
                j += 1
            j = 0
            i += 1
        return True

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

    def wipeSudokuClean(self):
        i, j = 0, 0

        while i < 9:
            while j < 9:
                self.celda[i][j].setText("")
                self.celda[i][j].setValorCorrecto(0)
                self.celda[i][j].setValor(0)
                j += 1
            j = 0
            i += 1




if __name__ == '__main__':
    #Tablero=Generador(1)
    #Tab=Generador(2)
    Ta=Generador(3)


    for i in range (9):
        for j in range(9):
            print(Ta.tablero[(i*9)+j],(i*9)+j)
        print("\n")