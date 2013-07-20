# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'acercade.ui'
#
# Created: Fri Jul 19 18:49:40 2013
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

class Ui_AcercaDe(object):
    def setupUi(self, AcercaDe):
        AcercaDe.setObjectName(_fromUtf8("AcercaDe"))
        AcercaDe.resize(400, 300)
        self.label_2 = QtGui.QLabel(AcercaDe)
        self.label_2.setGeometry(QtCore.QRect(20, 40, 331, 201))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Broadway"))
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label = QtGui.QLabel(AcercaDe)
        self.label.setGeometry(QtCore.QRect(10, 10, 351, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Broadway"))
        font.setPointSize(26)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName(_fromUtf8("label"))

        self.retranslateUi(AcercaDe)
        QtCore.QMetaObject.connectSlotsByName(AcercaDe)

    def retranslateUi(self, AcercaDe):
        AcercaDe.setWindowTitle(_translate("AcercaDe", "Dialog", None))
        self.label_2.setText(_translate("AcercaDe", "Juego de Sudoku en C++ con Qt\n"
"Autores: \n"
"Manuel Suárez    \n"
"Veronica Pozo", None))
        self.label.setText(_translate("AcercaDe", "ACERCA DE", None))

