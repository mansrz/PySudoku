import sys
import PySide
from ui.mainwindow import Ui_MainWindow


try:
    from PySide import QtUiTools, QtGui, QtCore
    USE_PYSIDE = True
except:
    from PyQt4 import uic, QtGui, QtCore
    USE_PYSIDE= False



class Main(PySide.QtGui.QMainWindow,PySide.QtGui.QWidget):
    def __init__(self):
        ui_c=Ui_MainWindow
        super(Main,self).__init__()
        self.setAttribute(PySide.QtCore.Qt.WA_DeleteOnClose)
        try:
            self.ui = QtUiTools.QUiLoader().load('../ui/mainwindow.ui')
        except:
            self.ui = uic.loadUi('../ui/mainwindow.ui')




if __name__ == '__main__':
    import sys
    app = PySide.QtGui.QApplication(sys.argv)
    main=Main()
    main.ui.show()
    sys.exit(app.exec_())


