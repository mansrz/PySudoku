try:
    import  PySide
    USE_PYSIDE = True
except:
    from PyQt4 import uic, QtGui, QtCore, phonon
    PySide.QtCore.Signal = PySide.QtCore.pyqtSignal
    PySide.QtCore.Slot = PySide.QtCore.pyqtSlot
    USE_PYSIDE = False

class MainWindow(PySide.QtGui.QMainWindow,PySide.QtGui.QWidget):

    def __init__(self):
        super(MainWindow,self).__init__()
        self.setAttribute(PySide.QtCore.Qt.WA_DeleteOnClose)
        self.setWindowTitle("SUDOKU")
        try:
           ### self.ui = QtUiTools.QUiLoader().load('../ui/mainwindow.ui')
        except:
            self.ui = uic.loadUi('../ui/mainwindow.ui')

        self.resize(400, 300)






if __name__ == '__main__':
    import sys
    app = PySide.QtGui.QApplication(sys.argv)
    mainWin = MainWindow()
    mainWin.show()
    sys.exit(app.exec_())




