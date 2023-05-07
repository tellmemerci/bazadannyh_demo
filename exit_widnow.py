import sys

from PyQt5 import QtCore, QtGui, QtWidgets

from sliyanie.glavnoe_menu_korabli import Glavnoe_menu


class exit_u(object):
    def exit_wundow(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(729, 307)
        MainWindow.setStyleSheet("background-color: rgb(255, 255, 202);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(410, 160, 141, 51))
        self.pushButton.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(190, 160, 141, 51))
        self.pushButton_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.pushButton_2.setObjectName("pushButton_2")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(60, 20, 611, 81))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 729, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.pushButton.clicked.connect(self.exit_user)
        self.pushButton_2.clicked.connect(self.dont_exit_user)

    def dont_exit_user(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Glavnoe_menu()
        self.ui.setupUi(self.window)
        self.window.show()

    def exit_user(self):
        sys.exit()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "ДА"))
        self.pushButton_2.setText(_translate("MainWindow", "НЕТ"))
        self.label.setText(_translate("MainWindow", "Вы действительно хотите выйти из приложения?"))