# -*- coding: utf-8 -*-
import psycopg2

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QTableWidgetItem, QTableWidget


class zapros_window(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("zapros_window")
        MainWindow.resize(1912, 1096)
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(680, -30, 801, 131))
        font = QtGui.QFont()
        font.setPointSize(17)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_5.setObjectName("label_5")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, -20, 1931, 1121))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("../../../OneDrive/Рабочий стол/корабль запрос.jpg"))
        self.label.setObjectName("label")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(50, 130, 1541, 61))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.textEdit.setFont(font)
        self.textEdit.setStyleSheet("background-color: rgb(197, 166, 166);")
        self.textEdit.setObjectName("textEdit")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(50, 40, 801, 131))
        font = QtGui.QFont()
        font.setPointSize(17)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_6.setObjectName("label_6")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(1600, 130, 171, 61))
        self.pushButton.setObjectName("pushButton")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(50, 280, 1791, 661))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.label.raise_()
        self.label_5.raise_()
        self.textEdit.raise_()
        self.label_6.raise_()
        self.pushButton.raise_()
        self.tableWidget.raise_()
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

        self.pushButton.clicked.connect(self.zaprosit_pols)

    def ochistit_label(self):
        self.label_6.setText("")


    def zaprosit_pols(self):
        try:
            connection = psycopg2.connect(user="user_1", password="12345678", host="localhost", port="5432",
                                          database="korabli")
            print("база данных подключена")
            cursor = connection.cursor()

            query = self.textEdit.toPlainText()
            cursor.execute(query)

            column_names = [desc[0] for desc in cursor.description]
            self.tableWidget.setColumnCount(len(column_names))
            self.tableWidget.setHorizontalHeaderLabels(column_names)

            row = 0
            for record in cursor:
                self.tableWidget.insertRow(row)

                for column, value in enumerate(record):
                    self.tableWidget.setItem(row, column, QTableWidgetItem(str(value)))
                    self.tableWidget.setColumnWidth(column, 500)  # установка ширины столбца

                row += 1

        except Exception as e:
            print("Ошибка запроса:", e)
            self.label_6.setText("ОШИБКА, ПОВТОРИТЕ ПОПЫТКУ")

        self.textEdit.clear()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_5.setText(_translate("MainWindow", "Создатель запросов к базе данных"))
        self.label_6.setText(_translate("MainWindow", "Напишите ваш запрос для базы данных"))
        self.pushButton.setText(_translate("MainWindow", "ЗАПРОСИТЬ"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = zapros_window()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
