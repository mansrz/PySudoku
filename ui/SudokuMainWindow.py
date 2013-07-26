__author__ = 'user'

import sys
from PySide.QtCore import *
from PySide.QtGui import *
from PySide import QtCore
from ui import sudokuui
from ui import Numero

class SudokuMainWindow(QMainWindow,sudokuui.Ui_MainWindow):
    def __init__(self, parent=None):
        super(SudokuMainWindow,self).__init__(parent)
        self.setupUi(self)

        self.connect(self.btnLlenar, SIGNAL("clicked()"), self.clickBtnLlenar)

    def clickBtnLlenar(self):
        numeros =[]
        for i in range(9):
            for j in range(9):
                #self.creacionNumeros(i*9+j,1,i,j,1)
                #numero = Numero.Numero(i*9+j,i,j)
                numeros.append(Numero.Numero(i*9+j,i,j,i==j))
                #numero = Numero(1,i,j,1)
                #numeros[i*9+j] = Numero(1,i,j,1)
                self.gridTablero.addWidget(numeros[i*9+j],i,j,0)


    #def creacionNumeros(self, i, valor, col, fila, visible):
        #numeros[i] =  Numero(valor,col,fila,visible)


    #ui->gridTablero->addWidget(numeros[i], col, fila, 0);
    #sgnlMprNumero->setMapping(numeros[i]->boton,i);



app= QApplication(sys.argv)
sudoku=SudokuMainWindow()
sudoku.show()
app.exec_()

