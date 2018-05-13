# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'doraemon.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 442)
        MainWindow.setStyleSheet("QMainWindow{background-color: qlineargradient(spread:pad, x1:0.33, y1:0, x2:0.702, y2:1, stop:0.141509 rgba(159, 94, 124, 255), stop:0.721698 rgba(46, 65, 97, 255));}\n"
"QLabel{color: rgb(255, 255, 255);}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.label_tts = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(20)
        self.label_tts.setFont(font)
        self.label_tts.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_tts.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_tts.setObjectName("label_tts")
        self.gridLayout.addWidget(self.label_tts, 4, 0, 1, 6)
        self.label_stt = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(15)
        self.label_stt.setFont(font)
        self.label_stt.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_stt.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_stt.setObjectName("label_stt")
        self.gridLayout.addWidget(self.label_stt, 3, 0, 1, 6)
        self.label_notice = QtWidgets.QLabel(self.centralwidget)
        self.label_notice.setText("")
        self.label_notice.setObjectName("label_notice")
        self.gridLayout.addWidget(self.label_notice, 0, 0, 2, 2)
        self.pushButton_food = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_food.setObjectName("pushButton_food")
        self.gridLayout.addWidget(self.pushButton_food, 0, 3, 1, 1)
        self.pushButton_weather = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_weather.setEnabled(True)
        self.pushButton_weather.setObjectName("pushButton_weather")
        self.gridLayout.addWidget(self.pushButton_weather, 0, 5, 1, 1)
        self.pushButton_notice = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_notice.setObjectName("pushButton_notice")
        self.gridLayout.addWidget(self.pushButton_notice, 0, 4, 1, 1)
        self.pushButton_shuttle = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_shuttle.setObjectName("pushButton_shuttle")
        self.gridLayout.addWidget(self.pushButton_shuttle, 1, 2, 1, 2)
        self.pushButton_comfirm = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_comfirm.setObjectName("pushButton_comfirm")
        self.gridLayout.addWidget(self.pushButton_comfirm, 5, 4, 2, 2)
        self.horizontalLayout.addLayout(self.gridLayout)
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setObjectName("widget")
        self.horizontalLayout.addWidget(self.widget)
        self.horizontalLayout_2.addLayout(self.horizontalLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")

        #set invisible
        self.pushButton_notice.setVisible(False)
        self.pushButton_weather.setVisible(False)
        self.pushButton_food.setVisible(False)
        self.pushButton_shuttle.setVisible(False)
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_tts.setText(_translate("MainWindow", "..."))
        self.label_stt.setText(_translate("MainWindow", "..."))
        self.pushButton_food.setText(_translate("MainWindow", "PushButton"))
        self.pushButton_weather.setText(_translate("MainWindow", "PushButton"))
        self.pushButton_notice.setText(_translate("MainWindow", "PushButton"))
        self.pushButton_shuttle.setText(_translate("MainWindow", "PushButton"))
        self.pushButton_comfirm.setText(_translate("MainWindow", "Notice"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

