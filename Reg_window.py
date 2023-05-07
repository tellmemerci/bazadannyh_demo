from PyQt5 import uic
import psycopg2
from psycopg2 import Error
from PyQt5.QtWidgets import QApplication
import pygame
from datetime import datetime
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5 import uic
import psycopg2
from psycopg2 import Error
from PyQt5.QtWidgets import QApplication
import pygame
from datetime import datetime
from glavnoe_menu_korabli import Glavnoe_menu

class Ui_Reg_window(object):
    def setupUi(self, Reg_window):
        Reg_window.setObjectName("Reg_window")
        Reg_window.resize(1732, 1015)
        self.label_2 = QtWidgets.QLabel(Reg_window)
        self.label_2.setGeometry(QtCore.QRect(250, -10, 481, 71))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_2.setObjectName("label_2")
        self.lineEdit_2 = QtWidgets.QLineEdit(Reg_window)
        self.lineEdit_2.setGeometry(QtCore.QRect(340, 350, 441, 61))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setStyleSheet("background-color: rgb(255, 245, 184);")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_4 = QtWidgets.QLabel(Reg_window)
        self.label_4.setGeometry(QtCore.QRect(70, 260, 261, 51))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_4.setObjectName("label_4")
        self.pushButton_2 = QtWidgets.QPushButton(Reg_window)
        self.pushButton_2.setGeometry(QtCore.QRect(410, 490, 191, 101))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("background-color: rgb(255, 255, 205);")
        self.pushButton_2.setObjectName("pushButton_2")
        self.label_5 = QtWidgets.QLabel(Reg_window)
        self.label_5.setGeometry(QtCore.QRect(70, 350, 261, 51))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_5.setObjectName("label_5")
        self.pushButton = QtWidgets.QPushButton(Reg_window)
        self.pushButton.setGeometry(QtCore.QRect(170, 490, 191, 101))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("background-color: rgb(255, 255, 205);")
        self.pushButton.setObjectName("pushButton")
        self.label = QtWidgets.QLabel(Reg_window)
        self.label.setGeometry(QtCore.QRect(-50, -70, 2181, 1071))
        font = QtGui.QFont()
        font.setPointSize(7)
        self.label.setFont(font)
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("../../../OneDrive/Рабочий стол/0e485c4b3dcbec817239f68fb7f28e53.jpg"))
        self.label.setObjectName("label")
        self.label_3 = QtWidgets.QLabel(Reg_window)
        self.label_3.setGeometry(QtCore.QRect(280, 40, 481, 71))
        font = QtGui.QFont()
        font.setPointSize(25)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_3.setObjectName("label_3")
        self.lineEdit = QtWidgets.QLineEdit(Reg_window)
        self.lineEdit.setGeometry(QtCore.QRect(340, 260, 441, 61))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.lineEdit.setFont(font)
        self.lineEdit.setStyleSheet("background-color: rgb(255, 245, 184);")
        self.lineEdit.setObjectName("lineEdit")
        self.label_6 = QtWidgets.QLabel(Reg_window)
        self.label_6.setGeometry(QtCore.QRect(1080, 290, 271, 71))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.label.raise_()
        self.label_2.raise_()
        self.lineEdit_2.raise_()
        self.label_4.raise_()
        self.pushButton_2.raise_()
        self.label_5.raise_()
        self.pushButton.raise_()
        self.label_3.raise_()
        self.lineEdit.raise_()
        self.label_6.raise_()

        self.retranslateUi(Reg_window)
        QtCore.QMetaObject.connectSlotsByName(Reg_window)

        self.pushButton.clicked.connect(self.registracion_user_code)

    def registracion_user_code(self):
        user_login = self.lineEdit.text()
        user_password = self.lineEdit_2.text()
        try:
            connection = psycopg2.connect(user=user_login, password=user_password,
                                          host="localhost", port="5432", database="korabli")
            print("ok")
            self.window = QtWidgets.QMainWindow()
            self.ui = Glavnoe_menu()
            self.ui.setupUi(self.window)
            self.window.show()
            self.Reg_window.close()

        except:
            print("no")



    def retranslateUi(self, Reg_window):
        _translate = QtCore.QCoreApplication.translate
        Reg_window.setWindowTitle(_translate("Reg_window", "Form"))
        self.label_2.setText(_translate("Reg_window", "База данных \"Морские сражения\""))
        self.label_4.setText(_translate("Reg_window", "Имя пользователя"))
        self.pushButton_2.setText(_translate("Reg_window", "Отмена"))
        self.label_5.setText(_translate("Reg_window", "Пароль"))
        self.pushButton.setText(_translate("Reg_window", "Войти"))
        self.label_3.setText(_translate("Reg_window", "РЕГИСТРАЦИЯ"))
        self.label_6.setText(_translate("Reg_window", "TEXT_HERE"))

