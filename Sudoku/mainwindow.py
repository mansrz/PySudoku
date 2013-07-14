from PyQt4 import QtCore, QtGui



class MainWindow(QtGui.QMainWindow,QtGui.QWidget):

    def __init__(self):
        super(MainWindow,self).__init__()
        self.setAttribute(QtCore.Qt.WA_DeleteOnClose)
        self.setWindowTitle("SUDOKU")
        self.resize(400, 300)

    




if __name__ == '__main__':
    import sys
    app = QtGui.QApplication(sys.argv)
    mainWin = MainWindow()
    mainWin.show()
    sys.exit(app.exec_())




