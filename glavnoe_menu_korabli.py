import sys

from PyQt5 import QtCore, QtGui, QtWidgets



class Glavnoe_menu(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1912, 1096)
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(30, 20, 601, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("")
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(1200, 140, 411, 61))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("background-color: rgb(255, 253, 176);")
        self.pushButton.setObjectName("pushButton")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(1280, 10, 801, 131))
        font = QtGui.QFont()
        font.setPointSize(17)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("")
        self.label_5.setObjectName("label_5")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(0, 0, 2111, 1111))
        self.label_9.setText("")
        self.label_9.setPixmap(QtGui.QPixmap("../../../Downloads/1613656210_8-p-fon-dlya-prezentatsii-korabli-13.jpg"))
        self.label_9.setObjectName("label_9")
        self.pushButton_6 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_6.setGeometry(QtCore.QRect(40, 70, 131, 41))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_6.setFont(font)
        self.pushButton_6.setStyleSheet("background-color: rgb(255, 253, 176);")
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_7 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_7.setGeometry(QtCore.QRect(190, 70, 131, 41))
        font = QtGui.QFont()
        font.setPointSize(7)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_7.setFont(font)
        self.pushButton_7.setStyleSheet("background-color: rgb(255, 253, 176);")
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(1200, 220, 411, 61))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setStyleSheet("background-color: rgb(255, 253, 176);")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(1200, 300, 411, 61))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setStyleSheet("background-color: rgb(255, 253, 176);")
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(1200, 380, 411, 61))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setStyleSheet("background-color: rgb(255, 253, 176);")
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_8 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_8.setGeometry(QtCore.QRect(1200, 470, 411, 61))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_8.setFont(font)
        self.pushButton_8.setStyleSheet("background-color: rgb(255, 253, 176);")
        self.pushButton_8.setObjectName("pushButton_8")
        self.label_9.raise_()
        self.label.raise_()
        self.pushButton.raise_()
        self.pushButton_6.raise_()
        self.pushButton_7.raise_()
        self.label_5.raise_()
        self.pushButton_3.raise_()
        self.pushButton_4.raise_()
        self.pushButton_5.raise_()
        self.pushButton_8.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1912, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "БАЗА ДАННЫХ \"МОРСИЕ СРАЖЕНИЯ\""))
        self.pushButton.setText(_translate("MainWindow", "Создать запись о корабле и битвах"))
        self.label_5.setText(_translate("MainWindow", "ГЛАВНОЕ МЕНЮ"))
        self.pushButton_6.setText(_translate("MainWindow", "Включить музыку"))
        self.pushButton_7.setText(_translate("MainWindow", "Отключить музыку"))
        self.pushButton_3.setText(_translate("MainWindow", "Изменить данные"))
        self.pushButton_4.setText(_translate("MainWindow", "Удалить данные"))
        self.pushButton_5.setText(_translate("MainWindow", "Сделать запрос к базе данных"))
        self.pushButton_8.setText(_translate("MainWindow", "Выйти из приложения"))
        self.pushButton_5.clicked.connect(self.open_zapros_window)
        self.pushButton_8.clicked.connect(self.exit_from_programm)


    def open_zapros_window(self):
        self.window = QtWidgets.QMainWindow()
        from sliyanie.zapros_new import Zapros
        self.ui = Zapros()
        self.ui.zapros_window_new(self.window)
        self.window.show()



    def exit_from_programm(self):
        self.window = QtWidgets.QMainWindow()
        from sliyanie.exit_widnow import exit_u
        self.ui = exit_u()
        self.ui.exit_wundow(self.window)
        self.window.show()