import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from Reg_window import Ui_Reg_window


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_Reg_window()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
