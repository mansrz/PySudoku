# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mejorestiempos.ui'
#
# Created: Fri Jul 26 17:30:51 2013
#      by: pyside-uic 0.2.14 running on PySide 1.2.0
#
# WARNING! All changes made in this file will be lost!
## @package mejoresTiemposUI
#  Este archivo contiene las Ventana de mejores tiempos
#
from PySide import QtCore, QtGui
""" _Clase MejoresTiempos
Tiene la ventana con la información de MejoresTiempos
"""
class Ui_MejoresTiempos(object):
    def setupUi(self, MejoresTiempos):
        MejoresTiempos.setObjectName("MejoresTiempos")
        MejoresTiempos.resize(346, 364)
        self.tab = QtGui.QTabWidget(MejoresTiempos)
        self.tab.setGeometry(QtCore.QRect(40, 60, 261, 231))
        font = QtGui.QFont()
        font.setFamily("Broadway")
        font.setPointSize(10)
        font.setWeight(75)
        font.setBold(True)
        self.tab.setFont(font)
        self.tab.setObjectName("tab")
        self.tabPrincipiante = QtGui.QWidget()
        self.tabPrincipiante.setObjectName("tabPrincipiante")
        self.tablePrincipiante = QtGui.QTableWidget(self.tabPrincipiante)
        self.tablePrincipiante.setGeometry(QtCore.QRect(20, 10, 221, 181))
        self.tablePrincipiante.setAutoScroll(False)
        self.tablePrincipiante.setObjectName("tablePrincipiante")
        self.tablePrincipiante.setColumnCount(2)
        self.tablePrincipiante.setRowCount(5)
        item = QtGui.QTableWidgetItem()
        self.tablePrincipiante.setVerticalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tablePrincipiante.setVerticalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.tablePrincipiante.setVerticalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        self.tablePrincipiante.setVerticalHeaderItem(3, item)
        item = QtGui.QTableWidgetItem()
        self.tablePrincipiante.setVerticalHeaderItem(4, item)
        item = QtGui.QTableWidgetItem()
        self.tablePrincipiante.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tablePrincipiante.setHorizontalHeaderItem(1, item)
        self.tab.addTab(self.tabPrincipiante, "")
        self.tabIntermedio = QtGui.QWidget()
        self.tabIntermedio.setObjectName("tabIntermedio")
        self.tableIntermedio = QtGui.QTableWidget(self.tabIntermedio)
        self.tableIntermedio.setGeometry(QtCore.QRect(20, 10, 221, 181))
        self.tableIntermedio.setAutoScroll(False)
        self.tableIntermedio.setObjectName("tableIntermedio")
        self.tableIntermedio.setColumnCount(2)
        self.tableIntermedio.setRowCount(5)
        item = QtGui.QTableWidgetItem()
        self.tableIntermedio.setVerticalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tableIntermedio.setVerticalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.tableIntermedio.setVerticalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        self.tableIntermedio.setVerticalHeaderItem(3, item)
        item = QtGui.QTableWidgetItem()
        self.tableIntermedio.setVerticalHeaderItem(4, item)
        item = QtGui.QTableWidgetItem()
        self.tableIntermedio.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tableIntermedio.setHorizontalHeaderItem(1, item)
        self.tab.addTab(self.tabIntermedio, "")
        self.tabAvanzado = QtGui.QWidget()
        self.tabAvanzado.setObjectName("tabAvanzado")
        self.tableAvanzado = QtGui.QTableWidget(self.tabAvanzado)
        self.tableAvanzado.setGeometry(QtCore.QRect(20, 10, 221, 181))
        self.tableAvanzado.setAutoScroll(False)
        self.tableAvanzado.setDragEnabled(False)
        self.tableAvanzado.setGridStyle(QtCore.Qt.SolidLine)
        self.tableAvanzado.setObjectName("tableAvanzado")
        self.tableAvanzado.setColumnCount(2)
        self.tableAvanzado.setRowCount(5)
        item = QtGui.QTableWidgetItem()
        self.tableAvanzado.setVerticalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tableAvanzado.setVerticalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.tableAvanzado.setVerticalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        self.tableAvanzado.setVerticalHeaderItem(3, item)
        item = QtGui.QTableWidgetItem()
        self.tableAvanzado.setVerticalHeaderItem(4, item)
        item = QtGui.QTableWidgetItem()
        self.tableAvanzado.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tableAvanzado.setHorizontalHeaderItem(1, item)
        self.tab.addTab(self.tabAvanzado, "")
        self.labelMejoresTiempos = QtGui.QLabel(MejoresTiempos)
        self.labelMejoresTiempos.setGeometry(QtCore.QRect(30, 10, 281, 31))
        self.labelMejoresTiempos.setStyleSheet("font: 75 20pt \"Broadway\";")
        self.labelMejoresTiempos.setObjectName("labelMejoresTiempos")
        self.pushButton = QtGui.QPushButton(MejoresTiempos)
        self.pushButton.setGeometry(QtCore.QRect(130, 310, 81, 31))
        font = QtGui.QFont()
        font.setFamily("Broadway")
        font.setPointSize(12)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(MejoresTiempos)
        self.tab.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MejoresTiempos)

    def retranslateUi(self, MejoresTiempos):
        MejoresTiempos.setWindowTitle(QtGui.QApplication.translate("MejoresTiempos", "Dialog", None, QtGui.QApplication.UnicodeUTF8))
        self.tablePrincipiante.verticalHeaderItem(0).setText(QtGui.QApplication.translate("MejoresTiempos", "1", None, QtGui.QApplication.UnicodeUTF8))
        self.tablePrincipiante.verticalHeaderItem(1).setText(QtGui.QApplication.translate("MejoresTiempos", "2", None, QtGui.QApplication.UnicodeUTF8))
        self.tablePrincipiante.verticalHeaderItem(2).setText(QtGui.QApplication.translate("MejoresTiempos", "3", None, QtGui.QApplication.UnicodeUTF8))
        self.tablePrincipiante.verticalHeaderItem(3).setText(QtGui.QApplication.translate("MejoresTiempos", "4", None, QtGui.QApplication.UnicodeUTF8))
        self.tablePrincipiante.verticalHeaderItem(4).setText(QtGui.QApplication.translate("MejoresTiempos", "5", None, QtGui.QApplication.UnicodeUTF8))
        self.tablePrincipiante.horizontalHeaderItem(0).setText(QtGui.QApplication.translate("MejoresTiempos", "Nombre", None, QtGui.QApplication.UnicodeUTF8))
        self.tablePrincipiante.horizontalHeaderItem(1).setText(QtGui.QApplication.translate("MejoresTiempos", "Tiempo", None, QtGui.QApplication.UnicodeUTF8))
        self.tab.setTabText(self.tab.indexOf(self.tabPrincipiante), QtGui.QApplication.translate("MejoresTiempos", "Facil", None, QtGui.QApplication.UnicodeUTF8))
        self.tableIntermedio.verticalHeaderItem(0).setText(QtGui.QApplication.translate("MejoresTiempos", "1", None, QtGui.QApplication.UnicodeUTF8))
        self.tableIntermedio.verticalHeaderItem(1).setText(QtGui.QApplication.translate("MejoresTiempos", "2", None, QtGui.QApplication.UnicodeUTF8))
        self.tableIntermedio.verticalHeaderItem(2).setText(QtGui.QApplication.translate("MejoresTiempos", "3", None, QtGui.QApplication.UnicodeUTF8))
        self.tableIntermedio.verticalHeaderItem(3).setText(QtGui.QApplication.translate("MejoresTiempos", "4", None, QtGui.QApplication.UnicodeUTF8))
        self.tableIntermedio.verticalHeaderItem(4).setText(QtGui.QApplication.translate("MejoresTiempos", "5", None, QtGui.QApplication.UnicodeUTF8))
        self.tableIntermedio.horizontalHeaderItem(0).setText(QtGui.QApplication.translate("MejoresTiempos", "Nombre", None, QtGui.QApplication.UnicodeUTF8))
        self.tableIntermedio.horizontalHeaderItem(1).setText(QtGui.QApplication.translate("MejoresTiempos", "Tiempo", None, QtGui.QApplication.UnicodeUTF8))
        self.tab.setTabText(self.tab.indexOf(self.tabIntermedio), QtGui.QApplication.translate("MejoresTiempos", "Intermedio", None, QtGui.QApplication.UnicodeUTF8))
        self.tableAvanzado.setSortingEnabled(False)
        self.tableAvanzado.verticalHeaderItem(0).setText(QtGui.QApplication.translate("MejoresTiempos", "1", None, QtGui.QApplication.UnicodeUTF8))
        self.tableAvanzado.verticalHeaderItem(1).setText(QtGui.QApplication.translate("MejoresTiempos", "2", None, QtGui.QApplication.UnicodeUTF8))
        self.tableAvanzado.verticalHeaderItem(2).setText(QtGui.QApplication.translate("MejoresTiempos", "3", None, QtGui.QApplication.UnicodeUTF8))
        self.tableAvanzado.verticalHeaderItem(3).setText(QtGui.QApplication.translate("MejoresTiempos", "4", None, QtGui.QApplication.UnicodeUTF8))
        self.tableAvanzado.verticalHeaderItem(4).setText(QtGui.QApplication.translate("MejoresTiempos", "5", None, QtGui.QApplication.UnicodeUTF8))
        self.tableAvanzado.horizontalHeaderItem(0).setText(QtGui.QApplication.translate("MejoresTiempos", "Nombre", None, QtGui.QApplication.UnicodeUTF8))
        self.tableAvanzado.horizontalHeaderItem(1).setText(QtGui.QApplication.translate("MejoresTiempos", "Tiempo", None, QtGui.QApplication.UnicodeUTF8))
        self.tab.setTabText(self.tab.indexOf(self.tabAvanzado), QtGui.QApplication.translate("MejoresTiempos", "Dificil", None, QtGui.QApplication.UnicodeUTF8))
        self.labelMejoresTiempos.setText(QtGui.QApplication.translate("MejoresTiempos", "MEJORES TIEMPOS", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton.setText(QtGui.QApplication.translate("MejoresTiempos", "Salir", None, QtGui.QApplication.UnicodeUTF8))

