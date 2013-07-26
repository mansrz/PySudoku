__author__ = 'user'

import sys
from PySide.QtCore import *
from PySide.QtGui import *
from ui import Funciones

class Numero (QFrame):
    casilla =-1

    def __init__(self, valor, fila, columna, visible):
        QFrame.__init__(self)

        font = QFont()
        font.setFamily("Broadway")
        font.setPointSize(22)

        sizePolicy = QSizePolicy (QSizePolicy.Ignored, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)

        self.fila = fila
        self.columna = columna
        self.valorCorrecto = valor
        self.valor = -1

        self.textOpciones= QLineEdit()
        self.boton = QPushButton("")

        self.setCuadricula()

        if visible:
            self.valor=valor
            self.boton.setText(str(valor))

        self.boton.setEnabled(not(visible))

        self.cambiarColorBotonOriginal();
        self.setFrameStyle(2)
        self.boton.setStyleSheet("border:none")
        self.boton.setFont(font)
        sizePolicy.setHeightForWidth(self.boton.sizePolicy().hasHeightForWidth())
        self.boton.setSizePolicy(sizePolicy)

        gridNumero = QVBoxLayout()
        gridNumero.setContentsMargins(0,0,0,0)
        gridNumero.addWidget(self.textOpciones)
        gridNumero.addWidget(self.boton)
        self.setLayout(gridNumero)


    def cambiarColorBotonAlerta(self):
        self.setStyleSheet("background-color: rgb(229, 0, 141);")


    def cambiarColorBotonPista(self):
        self.setStyleSheet("background-color: rgb(0, 170, 255);")


    def cambiarColorBotonOriginal(self):
        if self.cuadricula%2==0:
            self.setStyleSheet("background-color: rgb(255, 205, 135);")
        else:
            self.setStyleSheet("background-color: rgb(255, 255, 127);")


    def setCuadricula(self):
        filadiv=self.fila//3
        columnadiv=self.columna//3

        if filadiv==0:
            if columnadiv==0:
                self.cuadricula=0
            elif columnadiv==1:
                self.cuadricula=1
            elif columnadiv==2:
                self.cuadricula=2
        elif filadiv==1:
            if columnadiv==0:
                self.cuadricula=3
            elif columnadiv==1:
                self.cuadricula=4
            elif columnadiv==2:
                self.cuadricula=5
        elif filadiv==2:
            if columnadiv==0:
                self.cuadricula=6
            elif columnadiv==1:
                self.cuadricula=7
            elif columnadiv==2:
                self.cuadricula=8

