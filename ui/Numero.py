__author__ = 'user'

import sys
from PySide.QtCore import *
from PySide.QtGui import *
from PySide import QtCore

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

class Numero (QFrame):

    def __init__(self, val, fil, col, visible):
        super(Numero,self).__init__(self)

        font = QFont()
        font.setFamily(_fromUtf8("Broadway"))
        font.setPointSize(72)

        #sizePolicy = QSizePolicy ()
        #sizePolicy.setHorizontalStretch(0)
        #sizePolicy.setVerticalStretch(0)

        self.fila = fil
        self.columna = col
        self.valorCorrecto = val
        self.valor = -1
        
        numero = QtCore.QString("")
        textOpciones= QLineEdit()
        boton = QPushButton(numero)

        #setCuadricula(fila, columna)

        #if (visible)
            #editarBoton(valor)

        #boton->setEnabled(!visible);

        #cambiarColorBotonOriginal();
        self.setFrameStyle(2)
        boton.setStyleSheet(_fromUtf8 ("border:none"))
        boton.setFont(font)
        #sizePolicy.setHeightForWidth(boton->sizePolicy().hasHeightForWidth());
        #boton->setSizePolicy(sizePolicy);

        gridNumero = QVBoxLayout(self)
        gridNumero.setContentsMargins(0,0,0,0)
        gridNumero.addWidget(textOpciones)
        gridNumero.addWidget(boton)



