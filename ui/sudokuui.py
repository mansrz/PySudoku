# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'sudokuUI.ui'
#
# Created: Thu Jul 25 10:54:23 2013
#      by: pyside-uic 0.2.14 running on PySide 1.2.0
#
# WARNING! All changes made in this file will be lost!
## @package sudokuui
#  Interfaz gráfica creada en Qt Creator
#
from PySide import QtCore, QtGui
""" _Clase SudokuUi
Tiene la ventana con la interfáz gráfica creada en qt
"""
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(789, 542)
        MainWindow.setStyleSheet("")
        self.centralWidget = QtGui.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.gridLayoutWidget = QtGui.QWidget(self.centralWidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(40, 20, 461, 471))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridTablero = QtGui.QGridLayout(self.gridLayoutWidget)
        self.gridTablero.setSizeConstraint(QtGui.QLayout.SetDefaultConstraint)
        self.gridTablero.setSpacing(0)
        self.gridTablero.setContentsMargins(0, 0, 0, 0)
        self.gridTablero.setObjectName("gridTablero")
        self.label = QtGui.QLabel(self.gridLayoutWidget)
        self.label.setEnabled(True)
        font = QtGui.QFont()
        font.setFamily("Broadway")
        font.setPointSize(72)
        self.label.setFont(font)
        self.label.setStyleSheet("font: 72pt \"Broadway\";")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.gridTablero.addWidget(self.label, 0, 0, 1, 1)
        self.gbOpciones = QtGui.QGroupBox(self.centralWidget)
        self.gbOpciones.setGeometry(QtCore.QRect(540, 350, 231, 111))
        font = QtGui.QFont()
        font.setFamily("Broadway")
        font.setPointSize(12)
        font.setWeight(50)
        font.setItalic(False)
        font.setBold(False)
        self.gbOpciones.setFont(font)
        self.gbOpciones.setStyleSheet("font: 12pt \"Broadway\";")
        self.gbOpciones.setObjectName("gbOpciones")
        self.chkAlerta1 = QtGui.QCheckBox(self.gbOpciones)
        self.chkAlerta1.setGeometry(QtCore.QRect(10, 20, 201, 17))
        font = QtGui.QFont()
        font.setFamily("Broadway")
        font.setPointSize(10)
        font.setWeight(50)
        font.setItalic(False)
        font.setBold(False)
        self.chkAlerta1.setFont(font)
        self.chkAlerta1.setStyleSheet("font: 10pt \"Broadway\";")
        self.chkAlerta1.setObjectName("chkAlerta1")
        self.chkAlerta2 = QtGui.QCheckBox(self.gbOpciones)
        self.chkAlerta2.setGeometry(QtCore.QRect(10, 40, 211, 17))
        font = QtGui.QFont()
        font.setFamily("Broadway")
        font.setPointSize(10)
        font.setWeight(50)
        font.setItalic(False)
        font.setBold(False)
        self.chkAlerta2.setFont(font)
        self.chkAlerta2.setStyleSheet("font: 10pt \"Broadway\";")
        self.chkAlerta2.setObjectName("chkAlerta2")
        self.chkAyuda = QtGui.QCheckBox(self.gbOpciones)
        self.chkAyuda.setGeometry(QtCore.QRect(10, 60, 151, 17))
        font = QtGui.QFont()
        font.setFamily("Broadway")
        font.setPointSize(10)
        font.setWeight(50)
        font.setItalic(False)
        font.setBold(False)
        self.chkAyuda.setFont(font)
        self.chkAyuda.setStyleSheet("font: 10pt \"Broadway\";")
        self.chkAyuda.setObjectName("chkAyuda")
        self.chkPista = QtGui.QCheckBox(self.gbOpciones)
        self.chkPista.setGeometry(QtCore.QRect(10, 80, 151, 17))
        font = QtGui.QFont()
        font.setFamily("Broadway")
        font.setPointSize(10)
        font.setWeight(50)
        font.setItalic(False)
        font.setBold(False)
        self.chkPista.setFont(font)
        self.chkPista.setStyleSheet("font: 10pt \"Broadway\";")
        self.chkPista.setObjectName("chkPista")
        self.btnLlenar = QtGui.QPushButton(self.centralWidget)
        self.btnLlenar.setGeometry(QtCore.QRect(590, 110, 141, 51))
        font = QtGui.QFont()
        font.setFamily("Broadway")
        font.setPointSize(16)
        self.btnLlenar.setFont(font)
        self.btnLlenar.setStyleSheet("border-color: none;\n"
"font: 16pt \"Broadway\";")
        self.btnLlenar.setObjectName("btnLlenar")
        self.gbNumeros = QtGui.QGroupBox(self.centralWidget)
        self.gbNumeros.setGeometry(QtCore.QRect(590, 170, 141, 121))
        font = QtGui.QFont()
        font.setFamily("Broadway")
        font.setPointSize(12)
        font.setWeight(50)
        font.setItalic(False)
        font.setBold(False)
        self.gbNumeros.setFont(font)
        self.gbNumeros.setStyleSheet("font: 12pt \"Broadway\";")
        self.gbNumeros.setObjectName("gbNumeros")
        self.gridLayoutWidget_2 = QtGui.QWidget(self.gbNumeros)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(10, 20, 121, 91))
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
        self.gridNumeros = QtGui.QGridLayout(self.gridLayoutWidget_2)
        self.gridNumeros.setContentsMargins(0, 0, 0, 0)
        self.gridNumeros.setObjectName("gridNumeros")
        self.btnAyuda = QtGui.QPushButton(self.centralWidget)
        self.btnAyuda.setEnabled(False)
        self.btnAyuda.setGeometry(QtCore.QRect(550, 300, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Broadway")
        font.setPointSize(10)
        self.btnAyuda.setFont(font)
        self.btnAyuda.setAcceptDrops(False)
        self.btnAyuda.setStyleSheet("")
        self.btnAyuda.setObjectName("btnAyuda")
        self.lcdNumber = QtGui.QLCDNumber(self.centralWidget)
        self.lcdNumber.setGeometry(QtCore.QRect(550, 10, 221, 51))
        self.lcdNumber.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lcdNumber.setDigitCount(9)
        self.lcdNumber.setObjectName("lcdNumber")
        self.btnFinalizar = QtGui.QPushButton(self.centralWidget)
        self.btnFinalizar.setEnabled(False)
        self.btnFinalizar.setGeometry(QtCore.QRect(670, 300, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Broadway")
        font.setPointSize(10)
        self.btnFinalizar.setFont(font)
        self.btnFinalizar.setObjectName("btnFinalizar")
        self.layoutWidget = QtGui.QWidget(self.centralWidget)
        self.layoutWidget.setGeometry(QtCore.QRect(550, 80, 221, 23))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout = QtGui.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.lblDificultad = QtGui.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Broadway")
        font.setPointSize(10)
        font.setWeight(75)
        font.setBold(True)
        self.lblDificultad.setFont(font)
        self.lblDificultad.setObjectName("lblDificultad")
        self.horizontalLayout.addWidget(self.lblDificultad)
        self.cboDificultad = QtGui.QComboBox(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Broadway")
        font.setPointSize(9)
        self.cboDificultad.setFont(font)
        self.cboDificultad.setStyleSheet("color: qradialgradient(spread:repeat, cx:0.5, cy:0.5, radius:0.077, fx:0.5, fy:0.5, stop:0 rgba(0, 169, 255, 147), stop:0.497326 rgba(0, 0, 0, 147), stop:1 rgba(0, 169, 255, 147));")
        self.cboDificultad.setObjectName("cboDificultad")
        self.cboDificultad.addItem("")
        self.cboDificultad.addItem("")
        self.cboDificultad.addItem("")
        self.horizontalLayout.addWidget(self.cboDificultad)
        MainWindow.setCentralWidget(self.centralWidget)
        self.menuBar = QtGui.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 789, 25))
        font = QtGui.QFont()
        font.setFamily("Broadway")
        font.setPointSize(12)
        self.menuBar.setFont(font)
        self.menuBar.setObjectName("menuBar")
        self.menuMenu = QtGui.QMenu(self.menuBar)
        self.menuMenu.setObjectName("menuMenu")
        self.menuAyuda = QtGui.QMenu(self.menuBar)
        self.menuAyuda.setObjectName("menuAyuda")
        MainWindow.setMenuBar(self.menuBar)
        self.mainToolBar = QtGui.QToolBar(MainWindow)
        self.mainToolBar.setObjectName("mainToolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.mainToolBar)
        self.actionNueva_partida = QtGui.QAction(MainWindow)
        font = QtGui.QFont()
        font.setFamily("Broadway")
        font.setPointSize(10)
        self.actionNueva_partida.setFont(font)
        self.actionNueva_partida.setObjectName("actionNueva_partida")
        self.actionGuardar_partida = QtGui.QAction(MainWindow)
        self.actionGuardar_partida.setEnabled(False)
        font = QtGui.QFont()
        font.setFamily("Broadway")
        font.setPointSize(10)
        self.actionGuardar_partida.setFont(font)
        self.actionGuardar_partida.setObjectName("actionGuardar_partida")
        self.actionCargar_partida = QtGui.QAction(MainWindow)
        font = QtGui.QFont()
        font.setFamily("Broadway")
        font.setPointSize(10)
        self.actionCargar_partida.setFont(font)
        self.actionCargar_partida.setObjectName("actionCargar_partida")
        self.actionSalir = QtGui.QAction(MainWindow)
        font = QtGui.QFont()
        font.setFamily("Broadway")
        font.setPointSize(10)
        self.actionSalir.setFont(font)
        self.actionSalir.setObjectName("actionSalir")
        self.actionAyuda = QtGui.QAction(MainWindow)
        font = QtGui.QFont()
        font.setFamily("Broadway")
        font.setPointSize(10)
        self.actionAyuda.setFont(font)
        self.actionAyuda.setObjectName("actionAyuda")
        self.actionAcerca_de = QtGui.QAction(MainWindow)
        font = QtGui.QFont()
        font.setFamily("Broadway")
        font.setPointSize(10)
        self.actionAcerca_de.setFont(font)
        self.actionAcerca_de.setObjectName("actionAcerca_de")
        self.actionMejores_tiempos = QtGui.QAction(MainWindow)
        font = QtGui.QFont()
        font.setFamily("Broadway")
        font.setPointSize(10)
        self.actionMejores_tiempos.setFont(font)
        self.actionMejores_tiempos.setObjectName("actionMejores_tiempos")
        self.menuMenu.addAction(self.actionNueva_partida)
        self.menuMenu.addAction(self.actionGuardar_partida)
        self.menuMenu.addAction(self.actionCargar_partida)
        self.menuMenu.addAction(self.actionMejores_tiempos)
        self.menuMenu.addAction(self.actionSalir)
        self.menuAyuda.addAction(self.actionAyuda)
        self.menuAyuda.addSeparator()
        self.menuAyuda.addAction(self.actionAcerca_de)
        self.menuBar.addAction(self.menuMenu.menuAction())
        self.menuBar.addAction(self.menuAyuda.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "Sudoku", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("MainWindow", "SUDOKU", None, QtGui.QApplication.UnicodeUTF8))
        self.gbOpciones.setTitle(QtGui.QApplication.translate("MainWindow", "Opciones", None, QtGui.QApplication.UnicodeUTF8))
        self.chkAlerta1.setText(QtGui.QApplication.translate("MainWindow", "Alerta jugadas invalidas", None, QtGui.QApplication.UnicodeUTF8))
        self.chkAlerta2.setText(QtGui.QApplication.translate("MainWindow", "Alerta jugadas incorrectas", None, QtGui.QApplication.UnicodeUTF8))
        self.chkAyuda.setText(QtGui.QApplication.translate("MainWindow", "Ayuda", None, QtGui.QApplication.UnicodeUTF8))
        self.chkPista.setText(QtGui.QApplication.translate("MainWindow", "Pista", None, QtGui.QApplication.UnicodeUTF8))
        self.btnLlenar.setText(QtGui.QApplication.translate("MainWindow", "Iniciar", None, QtGui.QApplication.UnicodeUTF8))
        self.gbNumeros.setTitle(QtGui.QApplication.translate("MainWindow", "Numeros", None, QtGui.QApplication.UnicodeUTF8))
        self.btnAyuda.setText(QtGui.QApplication.translate("MainWindow", "Ayuda", None, QtGui.QApplication.UnicodeUTF8))
        self.btnFinalizar.setText(QtGui.QApplication.translate("MainWindow", "Finalizar", None, QtGui.QApplication.UnicodeUTF8))
        self.lblDificultad.setText(QtGui.QApplication.translate("MainWindow", "Dificultad", None, QtGui.QApplication.UnicodeUTF8))
        self.cboDificultad.setItemText(0, QtGui.QApplication.translate("MainWindow", "1 Facil", None, QtGui.QApplication.UnicodeUTF8))
        self.cboDificultad.setItemText(1, QtGui.QApplication.translate("MainWindow", "2 Intermedio", None, QtGui.QApplication.UnicodeUTF8))
        self.cboDificultad.setItemText(2, QtGui.QApplication.translate("MainWindow", "3 Dificil", None, QtGui.QApplication.UnicodeUTF8))
        self.menuMenu.setTitle(QtGui.QApplication.translate("MainWindow", "Menu", None, QtGui.QApplication.UnicodeUTF8))
        self.menuAyuda.setTitle(QtGui.QApplication.translate("MainWindow", "Ayuda", None, QtGui.QApplication.UnicodeUTF8))
        self.actionNueva_partida.setText(QtGui.QApplication.translate("MainWindow", "Nueva partida", None, QtGui.QApplication.UnicodeUTF8))
        self.actionGuardar_partida.setText(QtGui.QApplication.translate("MainWindow", "Guardar partida", None, QtGui.QApplication.UnicodeUTF8))
        self.actionCargar_partida.setText(QtGui.QApplication.translate("MainWindow", "Cargar partida", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSalir.setText(QtGui.QApplication.translate("MainWindow", "Salir", None, QtGui.QApplication.UnicodeUTF8))
        self.actionAyuda.setText(QtGui.QApplication.translate("MainWindow", "Ayuda", None, QtGui.QApplication.UnicodeUTF8))
        self.actionAcerca_de.setText(QtGui.QApplication.translate("MainWindow", "Acerca de", None, QtGui.QApplication.UnicodeUTF8))
        self.actionMejores_tiempos.setText(QtGui.QApplication.translate("MainWindow", "Mejores tiempos", None, QtGui.QApplication.UnicodeUTF8))

