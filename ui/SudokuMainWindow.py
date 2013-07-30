__author__ = 'user'

import sys
from PySide.QtCore import *
from PySide.QtGui import *
from ui import sudokuui
from ui import Numero
from ui import ventanas
from random import randint
from ui import Generador

class SudokuMainWindow(QMainWindow,sudokuui.Ui_MainWindow):
    def __init__(self, parent=None):
        super(SudokuMainWindow,self).__init__(parent)
        self.setupUi(self)
        self.sgnlMprNumero = QSignalMapper(self)
        self.sgnlMprOpcion = QSignalMapper(self)
        self.casilla =-1
        self.colorCambiado=False
        self.dificultad=1
        self.ayudaUsada=False
        self.connect(self.btnLlenar, SIGNAL("clicked()"), self.clickBtnLlenar)
        self.connect(self.btnAyuda, SIGNAL("clicked()"), self.clickBtnAyuda)
        self.connect(self.btnFinalizar,SIGNAL("clicked()"),self.clickBtnFinalizar)
        self.connect(self.chkAyuda, SIGNAL("stateChanged(int)"), self.stateChangedChkAyuda)
        self.connect(self.chkAlerta1, SIGNAL("stateChanged(int)"), self.stateChangedChkAlerta1)
        self.connect(self.chkAlerta2, SIGNAL("stateChanged(int)"), self.stateChangedChkAlerta2)
        self.connect(self.actionAcerca_de, SIGNAL("triggered()"), self.triggerAcercaDe)
        self.connect(self.actionAyuda, SIGNAL("triggered()"), self.triggerAyuda)
        self.connect(self.actionMejores_tiempos, SIGNAL("triggered()"), self.triggerMejoresTiempos)

        #timer
        self.timeInicial=QTime.currentTime()
        self.actualizarTimer()
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.actualizarTimer)


    def clickBtnLlenar(self):
        self.dificultad=self.cboDificultad.currentIndex()
        generador = Generador.Generador(self.dificultad)
        for i in range(81):
            print(generador.tablero[i])
        self.numeros =[]
        for i in range(9):
            for j in range(9):
                self.creacionNumeros(i*9+j,generador.tablero[i*9+j],i,j,generador.visibles[i*9+j])
        self.sgnlMprNumero.mapped[int].connect(self.obtenerCasilla)
        self.creacionBotones()
        self.timeInicial=QTime.currentTime()
        self.inicializarTimer()
        self.btnLlenar.setEnabled(False)
        self.btnFinalizar.setEnabled(True)
        self.actionGuardar_partida.setEnabled(True)


    def clickBtnFinalizar(self):
        self.timer.stop()
        self.btnLlenar.setEnabled(True)
        self.btnFinalizar.setEnabled(False)
        self.actionGuardar_partida.setEnabled(False)


    def clickBtnAyuda(self):
        arrayInt = []
        for i in range(81):
            if self.numeros[i].valor == -1:
                arrayInt.append(i)
        if len(arrayInt)!=0:
            n = randint(0, len(arrayInt)-1)
            self.numeros[arrayInt[n]].boton.setText(str(self.numeros[arrayInt[n]].valorCorrecto))
            self.numeros[arrayInt[n]].valor=self.numeros[arrayInt[n]].valorCorrecto
        #nik: sacar de comentario la siguiente linea para permitir una ayuda
        #self.btnAyuda.setEnabled(False)
        self.ayudaUsada=True

    def stateChangedChkAyuda(self):
        if self.chkAyuda.checkState() and not(self.ayudaUsada):
            self.btnAyuda.setEnabled(True)
        if not(self.chkAyuda.checkState()):
            self.btnAyuda.setEnabled(False)


    def stateChangedChkAlerta1(self):
        if self.chkAlerta1.checkState():
            self.colorInvalidas()
        else:
            for i in range(81):
                self.numeros[i].cambiarColorBotonOriginal()
            if self.chkAlerta2.checkState():
                self.colorIncorrectas()


    def stateChangedChkAlerta2(self):
        if self.chkAlerta2.checkState():
            self.colorIncorrectas()
        else:
            for i in range(81):
                self.numeros[i].cambiarColorBotonOriginal()
            if self.chkAlerta1.checkState():
                self.colorInvalidas()



    def obtenerCasilla(self, n):
        self.casilla = n
        print ("valor correcto " +str(self.numeros[n].valorCorrecto))
        self.colorOriginal()


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
        self.colorOriginal()
        if self.casilla != -1:
            self.numeros[self.casilla].boton.setText(str(n+1))
            self.numeros[self.casilla].valor=n+1
            if self.chkAlerta1.checkState():
                if not(self.jugadaValida(self.casilla,n+1)):
                    self.numeros[self.casilla].cambiarColorBotonAlerta()
                else:
                    self.numeros[self.casilla].cambiarColorBotonOriginal()
            if self.chkAlerta2.checkState():
                if not(self.jugadaCorrecta()):
                    self.numeros[self.casilla].cambiarColorBotonAlerta()
                else:
                    self.numeros[self.casilla].cambiarColorBotonOriginal()
            self.casilla =-1
        else:
            if self.chkPista.checkState():
                for i in range(81):
                    if self.jugadaValida(i,n+1) and self.numeros[i].valor==-1:
                        self.numeros[i].cambiarColorBotonPista()
                        self.colorCambiado=True


    def jugadaValida(self, casilla, valor):
        for i in range (81):
            if self.numeros[casilla].cuadricula == self.numeros[i].cuadricula or \
                            self.numeros[casilla].columna == self.numeros[i].columna or \
                            self.numeros[casilla].fila == self.numeros[i].fila:
                if i!=casilla and valor == self.numeros[i].valor:
                    return False
        return True

    def jugadaCorrecta(self):
        if self.numeros[self.casilla].valor==self.numeros[self.casilla].valorCorrecto:
            return True
        return False

    def colorOriginal(self):
        if self.colorCambiado:
            for i in range(81):
                if self.numeros[i].valor == -1:
                    self.numeros[i].cambiarColorBotonOriginal()
        self.colorCambiado = False

    def colorInvalidas(self):
        for i in range (81):
            if self.numeros[i].boton.isEnabled() and not(self.jugadaValida(i,self.numeros[i].valor)) and self.numeros[i].valor !=-1:
                self.numeros[i].cambiarColorBotonAlerta()

    def colorIncorrectas(self):
        for i in range(81):
            if self.numeros[i].boton.isEnabled() and self.numeros[i].valor!=self.numeros[i].valorCorrecto and self.numeros[i].valor !=-1:
                self.numeros[i].cambiarColorBotonAlerta()


    def inicializarTimer(self):
        self.timer.setSingleShot(False)
        if not self.timer.isActive():
            self.timer.start(10)


    def actualizarTimer(self):
        timeAct=QTime.currentTime()
        minIni=self.timeInicial.minute()
        minAct=timeAct.minute()
        segIni=self.timeInicial.second()
        segAct=timeAct.second()
        msegIni=self.timeInicial.msec()
        msegAct=timeAct.msec()
        if msegAct < msegIni:
            msegAct = 1000+msegAct
            segAct = segAct-1
        if segAct < segIni:
            segAct = 60 + segAct
            minAct = minAct-1
        time = QTime(0,minAct-minIni, segAct-segIni,msegAct-msegIni)
        #self.lcdNumber.display(time.toString("mm:ss.z"))
        self.lcdNumber.display(time.toString("mm:ss")+"."+str((msegAct-msegIni)//10).zfill(2))



    def triggerAcercaDe(self):
        acercaDe.show()

    def triggerAyuda(self):
        ayuda.show()

    def triggerMejoresTiempos(self):
        mejoresTiempos.show()

app= QApplication(sys.argv)
timer = QTimer()
sudoku=SudokuMainWindow()
acercaDe = ventanas.wAcercaDe()
ayuda = ventanas.wAyuda()
mejoresTiempos = ventanas.wMejoresTiempos()
sudoku.show()
app.exec_()

