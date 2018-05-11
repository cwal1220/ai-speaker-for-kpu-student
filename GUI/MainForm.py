# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainForm.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 450)
        MainWindow.setStyleSheet("QMainWindow{background-color: qlineargradient(spread:pad, x1:0.33, y1:0, x2:0.702, y2:1, stop:0.141509 rgba(159, 94, 124, 255), stop:0.721698 rgba(46, 65, 97, 255));}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(370, -20, 431, 451))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.widget = Test(self.verticalLayoutWidget)
        self.widget.setObjectName("widget")
        self.verticalLayout.addWidget(self.widget)
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(280, 40, 67, 67))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_notice = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_notice.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_notice.setObjectName("verticalLayout_notice")
        self.label_notice = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label_notice.setText("")
        self.label_notice.setPixmap(QtGui.QPixmap("img/notice.png"))
        self.label_notice.setObjectName("label_notice")
        self.verticalLayout_notice.addWidget(self.label_notice)
        self.pushButton_notice = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_notice.setGeometry(QtCore.QRect(260, 330, 93, 28))
        self.pushButton_notice.setObjectName("pushButton_notice")
        self.pushButton_test = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_test.setGeometry(QtCore.QRect(260, 290, 93, 28))
        self.pushButton_test.setObjectName("pushButton_test")
        self.pushButton_read = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_read.setGeometry(QtCore.QRect(260, 370, 93, 28))
        self.pushButton_read.setObjectName("pushButton_read")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Intelligent Speaker for KPU Student"))
        self.pushButton_notice.setText(_translate("MainWindow", "Notice"))
        self.pushButton_test.setText(_translate("MainWindow", "Test"))
        self.pushButton_read.setText(_translate("MainWindow", "read"))

from test import Test
from notice import Notice

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

