import sys
from tokenize import String
import PySide
from PySide.QtCore import QSignalMapper, QTimer, QTime
from PySide.QtGui import QVBoxLayout, QFrame, QPushButton
import array


try:
    from PySide import QtUiTools, QtGui, QtCore
    USE_PYSIDE = True
except:
    from PyQt4 import uic, QtGui, QtCore
    USE_PYSIDE= False



class MainWindow(PySide.QtGui.QMainWindow,PySide.QtGui.QWidget):

    def __init__(self):
        super(MainWindow,self).__init__()
        self.setAttribute(PySide.QtCore.Qt.WA_DeleteOnClose)
        try:
            self.ui = QtUiTools.QUiLoader().load('../ui/mainwindow.ui')
        except:
            self.ui = uic.loadUi('../ui/mainwindow.ui')

        casilla=-1
        ayudaUsada=False
        colorCambiado=False
        num_dificultad=1
        sgnlMprNumero=QSignalMapper()
        sgnlMprOpcion=QSignalMapper()
        numeros=array.array('i',(0 for i in range(0,80)))
        gridNumeros=[(QVBoxLayout for i in range(0,80))]
        frameNumeros=[(QFrame for i in range(0,80))]
        opcionesNumeros=[(QPushButton for i in range(0,8))]
        texto=String
        nombre=String
        textTiempo=String
        timer=QTimer()
        timeInicial=QTime()
        ##  generador=Generador()
        valorTiempo=0;
        ##puntajeJugador=Puntaje
        ##mejoresTiempos=MejoresTiempos()
        ##ayuda=Ayuda()
        ##acercaDe=AcercaDe()
        ##listPrincipiante=Puntaje[5]
        ##listIntermedio=Puntaje[5]
        ##listAvanzado=Puntaje[5]

    def on_btnLlenar_clicked(self):
        num_dificultad=1+self.ui.cboDificultad.currentIndex()
        #generador->GenerarTablero(num_dificultad);
        #creacion de numeros
        for i in range(0,9):
            for j in range(0,9):
                    #creacionNumeros(i*9+j,generador->tablero[i*9+j],i,j,generador->casillas_visibles[i*9+j])


        #QtCore.connect(self.sgnlMprNumero, SIGNAL (mapped (int)), SLOT (obtenerCasilla(int)));

        #creacionBotones();
        #inicializarTimer();

        self.ui.btnLlenar.setEnabled(false)
        self.ui.btnFinalizar.setEnabled(true)
        self.ui.actionGuardar_partida.setEnabled(true)


    def creacionNumeros(param, param1, i, j, param2):
        pass










if __name__ == '__main__':
    import sys
    app = PySide.QtGui.QApplication(sys.argv)
    mainWin = MainWindow()
    mainWin.ui.show()
    sys.exit(app.exec_())




