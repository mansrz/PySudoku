__author__ = 'user'
import random

class numero:

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









celda = [[numero(fila, columna, "") for columna in range(9)] for fila in range(9)]

def validateCellAtPointerWithNumber(row, column, value, counter):
    i, j = 0, 0

    while i < 9:
        while j < 9:
            if(i == row or j == column or celda[i][j].getCuadricula() == celda[row][column].getCuadricula()):
                if(celda[i][j].getValorCorrecto()):
                    if(value == celda[i][j].getValorCorrecto() and not(i == row and j == column - counter)):
                        return False

            j += 1
        j = 0
        i += 1
    return True


def numberAssigner(counter, row, column, value):
    if (counter > column):
        return False
    if((not counter and validateCellAtPointerWithNumber(row, column, value, 0)) or (counter and validateCellAtPointerWithNumber(row, column, celda[row][column - counter].getValorCorrecto(), counter) and validateCellAtPointerWithNumber(row, column - counter, value, 0))):
        if(not counter):
            celda[row][column].setValorCorrecto(value)
        else:
            celda[row][column].setValorCorrecto(celda[row][column - counter].getValorCorrecto())
            celda[row][column - counter].setValorCorrecto(value)
        return True
    else:
        counter += 1
        return numberAssigner(counter, row, column, value)


def sudokuGenerator(row):
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
                if(numberAssigner(0, row, i, digitArray[j])):
                    digitArray[j] = -1
                    flag = True

            if(flag):
                break
            j += 1
        j = 0
        i += 1

    for index in range(9):
        rowArray[index] = celda[row][index].getValorCorrecto()

    sudokuGenerator(row + 1)

def printSudokuBoard():
    i, j = 0, 0
    crypt = ""

    while i < 9:
        while j < 9:
            crypt += ("%d " % celda[i][j].getValorCorrecto())
            j += 1
        crypt += "\n"
        j = 0
        i += 1
    print(crypt)

def checkSudokuForZero():
    i, j = 0, 0

    while i < 9:
        while j < 9:
            if (not celda[i][j].getValorCorrecto()):
                return False
            j += 1
        j = 0
        i += 1
    return True

def wipeSudokuClean():
    i, j = 0, 0

    while i < 9:
        while j < 9:
            celda[i][j].setText("")
            celda[i][j].setValorCorrecto(0)
            celda[i][j].setValor(0)
            j += 1
        j = 0
        i += 1

def hexConvert(decimal):
    s = ""
    h = [str(i) for i in range(10)]+["a","b","c","d","e","f"]

    while decimal:
        s += h[decimal % 16]
        decimal //= 16
    return s[::-1]

def biConvert(hex):
    return bin(int(hex, 16))[2:].zfill(9)

def encrypt():
    i, j, binaryBuffer, delta = 0, 0, 0, 0

    crypt = ""
    code = [""] * 9
    key = [""] * 9
    hint = [""] * 9

    while i < 9:
        while j < 9:

            if j == 0:
                delta = celda[i][j].getValorCorrecto()
                code[i] = chr(96 + delta)
            else:
                delta = celda[i][j].getValorCorrecto() - celda[i][j - 1].getValorCorrecto()
                code[i] += chr(96 + abs(delta))

            if delta >= 0:
                binaryBuffer += 2 ** (8 - j)

            hint[i] += str(celda[8 - i][8 - j].getValor())
            j += 1

        key[i] = str(hexConvert(binaryBuffer))
        binaryBuffer = 0
        crypt += ("%s\n" % code[i])
        crypt += ("%s\n" % key[i])
        crypt += ("%s\n" % hint[i])

        j = 0
        i += 1
        #print(crypt)
    return crypt


#crypt += ("%d\n" % timer.time + timer.timeAdd)

def saveGame(code):
    f = open("../savedGame.sud", "w")
    f.write(code)
    #print(code)


def openGame():
    index = 0
    code = [""] * 9
    key = [""] * 9
    hint = [""] * 9

    f = open("../savedGame.sud", "r")
    for line in f:



        if len(line):

            line = line.rstrip()

            if index == 27:
                print("hello")

            elif index % 3 == 0:
                code[index // 3] = line

            elif index % 3 == 1:
                key[index // 3] = line

            elif index % 3 == 2:
                hint[index // 3] = line

        index += 1

    decrypt(code, key, hint)


def decrypt(code, key, hint):
    i, j, binary, alpha, sign, deltaInverse, showNumber = 0, 0, "", "", 0, 0, 0

    while i < 9:
        binary = biConvert(str(key[i]))



        while j < 9:

            sign = int(binary[j])
            alpha = ord(code[i][j]) - 96

            deltaInverse = ((-1) ** (sign + 1)) * alpha

            if j == 0:
                celda[i][j].setValorCorrecto(deltaInverse)

            else:
                celda[i][j].setValorCorrecto(celda[i][j - 1].getValorCorrecto() + deltaInverse)



            showNumber = int(hint[i][j])

            if showNumber == 0:
                celda[8 - i][8 - j].setText("")

            else:
                celda[8 - i][8 - j].setText(str(showNumber))

            celda[8 - i][8 - j].setValor(showNumber)

            j += 1


        binary = ""
        j = 0
        i += 1







#saveGame(encrypt())
#openGame()

#print(biConvert("0f5"))
while (not checkSudokuForZero()):
    wipeSudokuClean()
    sudokuGenerator(0)
printSudokuBoard()

saveGame(encrypt())
openGame()
printSudokuBoard()