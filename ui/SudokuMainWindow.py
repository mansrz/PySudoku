__author__ = 'user'

import sys
from PySide.QtCore import *
from PySide.QtGui import *
from PySide import QtCore
from ui import sudokuui
from ui import Numero
from ui import Funciones

class SudokuMainWindow(QMainWindow,sudokuui.Ui_MainWindow):
    def __init__(self, parent=None):
        super(SudokuMainWindow,self).__init__(parent)
        self.setupUi(self)
        self.sgnlMprNumero = QSignalMapper(self)
        self.sgnlMprOpcion = QSignalMapper(self)

        self.connect(self.btnLlenar, SIGNAL("clicked()"), self.clickBtnLlenar)



    def clickBtnLlenar(self):
        self.numeros =[]
        for i in range(9):
            for j in range(9):
                self.creacionNumeros(i*9+j,i*9+j,i,j,i==j)
        self.sgnlMprNumero.mapped[int].connect(self.obtenerCasilla)
        self.creacionBotones()


    def obtenerCasilla(self, n):
        self.casilla = n
        print ("estoy en obtener casilla " +str(self.casilla))


    def creacionNumeros(self, i, valor, col, fila, visible):
        self.numeros.append(Numero.Numero(valor,col,fila,visible))
        self.gridTablero.addWidget(self.numeros[i],col,fila,0)
        self.sgnlMprNumero.setMapping(self.numeros[i].boton, i)
        self.numeros[i].boton.clicked.connect(self.sgnlMprNumero.map)


    def creacionBotones(self):
        self.opcionesNumeros=[]
        for i in range(3):
            for j in range(3):
                self.opcionesNumeros.append(QPushButton(str(i*3+j+1)))
                self.gridNumeros.addWidget(self.opcionesNumeros[i*3+j],i,j,0)
                self.sgnlMprOpcion.setMapping(self.opcionesNumeros[i*3+j], i*3+j)
                self.opcionesNumeros[i*3+j].clicked.connect(self.sgnlMprOpcion.map)
        self.sgnlMprOpcion.mapped[int].connect(self.cambiarNumero)



    def cambiarNumero(self, n):
        if self.casilla != -1:
            self.numeros[self.casilla].boton.setText(str(n+1))



app= QApplication(sys.argv)
sudoku=SudokuMainWindow()
sudoku.show()
app.exec_()

