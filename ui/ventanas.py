__author__ = 'user'
from PySide.QtGui import *
from ui import acercadeUI
from ui import ayudaUI
from ui import mejoresTiemposUI
from ui import jugador

class wAcercaDe(QMainWindow,acercadeUI.Ui_AcercaDe):
    def __init__(self, parent=None):
        super(wAcercaDe,self).__init__(parent)
        self.setupUi(self)


class wAyuda(QMainWindow,ayudaUI.Ui_Ayuda):
    def __init__(self, parent=None):
        super(wAyuda,self).__init__(parent)
        self.setupUi(self)



class wMejoresTiempos(QMainWindow,mejoresTiemposUI.Ui_MejoresTiempos):
    def __init__(self, parent=None):
        super(wMejoresTiempos,self).__init__(parent)
        self.setupUi(self)
        #self.guardarTiempos()
        self.cargarTiempos()
        self.mostrarTiempos()
        self.tableAvanzado.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableIntermedio.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tablePrincipiante.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.pushButton.clicked.connect(self.clickBtnSalir)


    def clickBtnSalir(self):
        self.close()

    def guardarTiempos(self):
        f = open("../bestTimes.sud", "w")
        text =""
        #inicializar Mejores Tiempos
        #for i in range (5):
         #   text += "1,n"+str(i+1)+",59:59:99,3599999\n"
          #  text += "2,n"+str(i+1)+",59:59:99,3599999\n"
           # text += "3,n"+str(i+1)+",59:59:99,3599999\n"
        #guardar Mejores tiempos
        for i in range(len(listaJugadores)):
            text+=listaJugadores[i].nivel+","+listaJugadores[i].nombre+","+listaJugadores[i].tiempo+","+listaJugadores[i].valor+"\n"
        f.write(text)



    def cargarTiempos(self):
        f = open("../bestTimes.sud", "r")
        for line in f:
            if len(line):
                line = line.rstrip()
                jugadorText=line.split(",")
                listaJugadores.append(jugador.Jugador(jugadorText[0],jugadorText[1],jugadorText[2],jugadorText[3]))


    def mostrarTiempos(self):
        principiante=0
        intermedio=0
        avanzado=0
        for i in range (len(listaJugadores)):
            if listaJugadores[i].nivel == "1" and principiante <5:
                self.tablePrincipiante.setItem(principiante,0, QTableWidgetItem(listaJugadores[i].nombre))
                self.tablePrincipiante.setItem(principiante,1, QTableWidgetItem(listaJugadores[i].tiempo))
                principiante=principiante+1
            elif listaJugadores[i].nivel == "2" and intermedio <5:
                self.tableIntermedio.setItem(intermedio,0, QTableWidgetItem(listaJugadores[i].nombre))
                self.tableIntermedio.setItem(intermedio,1, QTableWidgetItem(listaJugadores[i].tiempo))
                intermedio = intermedio+1
            elif listaJugadores[i].nivel == "3" and avanzado <5:
                self.tableAvanzado.setItem(avanzado,0, QTableWidgetItem(listaJugadores[i].nombre))
                self.tableAvanzado.setItem(avanzado,1, QTableWidgetItem(listaJugadores[i].tiempo))
                avanzado=avanzado+1


def insertarEnLista(jugador):
    i=0
    while i<(len(listaJugadores)-1) and int(listaJugadores[i].valor)<int(jugador.valor):
        i=i+1
    listaJugadores.insert(i,jugador)


listaJugadores=[]