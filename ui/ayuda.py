# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ayuda.ui'
#
# Created: Fri Jul 19 18:47:48 2013
#      by: PyQt4 UI code generator 4.10.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Ayuda(object):
    def setupUi(self, Ayuda):
        Ayuda.setObjectName(_fromUtf8("Ayuda"))
        Ayuda.resize(460, 432)
        self.label = QtGui.QLabel(Ayuda)
        self.label.setGeometry(QtCore.QRect(20, 20, 421, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Broadway"))
        font.setPointSize(26)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(Ayuda)
        self.label_2.setGeometry(QtCore.QRect(30, 50, 431, 331))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Broadway"))
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setTextFormat(QtCore.Qt.AutoText)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.pushButton = QtGui.QPushButton(Ayuda)
        self.pushButton.setGeometry(QtCore.QRect(190, 380, 81, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Broadway"))
        font.setPointSize(12)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))

        self.retranslateUi(Ayuda)
        QtCore.QMetaObject.connectSlotsByName(Ayuda)

    def retranslateUi(self, Ayuda):
        Ayuda.setWindowTitle(_translate("Ayuda", "Dialog", None))
        self.label.setText(_translate("Ayuda", "AYUDA", None))
        self.label_2.setText(_translate("Ayuda", "El sudoku se presenta normalmente como una \n"
"tabla de 9 × 9, compuesta por subtablas de \n"
"3 × 3 denominadas \"regiones\" (también se le \n"
"llaman \"cajas\" o \"bloques\").\n"
"Algunas celdas ya contienen números, conocidos \n"
"como \"números dados\" (o a veces \"pistas\").\n"
"El objetivo es rellenar las celdas vacías, \n"
"con un número en cada una de ellas, de tal \n"
"forma que cada columna, fila y región contenga \n"
"los números 1–9 sólo una vez.\n"
"Además, cada número de la solución aparece \n"
"sólo una vez en cada una de las tres \n"
"\"direcciones\", de ahí el \"los números deben \n"
"estar solos\" que evoca el nombre del juego.", None))
        self.pushButton.setText(_translate("Ayuda", "Salir", None))

