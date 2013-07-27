# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'acercade.ui'
#
# Created: Fri Jul 26 17:27:18 2013
#      by: pyside-uic 0.2.14 running on PySide 1.2.0
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_AcercaDe(object):
    def setupUi(self, AcercaDe):
        AcercaDe.setObjectName("AcercaDe")
        AcercaDe.resize(400, 300)
        self.label_2 = QtGui.QLabel(AcercaDe)
        self.label_2.setGeometry(QtCore.QRect(20, 40, 331, 201))
        font = QtGui.QFont()
        font.setFamily("Broadway")
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label = QtGui.QLabel(AcercaDe)
        self.label.setGeometry(QtCore.QRect(10, 10, 351, 31))
        font = QtGui.QFont()
        font.setFamily("Broadway")
        font.setPointSize(26)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")

        self.retranslateUi(AcercaDe)
        QtCore.QMetaObject.connectSlotsByName(AcercaDe)

    def retranslateUi(self, AcercaDe):
        AcercaDe.setWindowTitle(QtGui.QApplication.translate("AcercaDe", "Dialog", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("AcercaDe", "Juego de Sudoku en Python con Qt\n\n"
"Autores: \n"
"   Manuel Suárez    \n"
"   Veronica Pozo\n"
"   Alvaro Ortiz", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("AcercaDe", "ACERCA DE", None, QtGui.QApplication.UnicodeUTF8))

