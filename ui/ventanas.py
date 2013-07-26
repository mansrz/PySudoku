__author__ = 'user'
from PySide.QtGui import *
from ui import acercadeUI
from ui import ayudaUI
from ui import mejoresTiemposUI

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