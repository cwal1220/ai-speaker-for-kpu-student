# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'TestWidget.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Test(object):
    def setupUi(self, Test):
        Test.setObjectName("Test")
        Test.resize(400, 450)
        self.label = QtWidgets.QLabel(Test)
        self.label.setGeometry(QtCore.QRect(180, 210, 64, 15))
        self.label.setObjectName("label")

        self.retranslateUi(Test)
        QtCore.QMetaObject.connectSlotsByName(Test)

    def retranslateUi(self, Test):
        _translate = QtCore.QCoreApplication.translate
        Test.setWindowTitle(_translate("Test", "TestWidget"))
        self.label.setText(_translate("Test", "Test"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Test = QtWidgets.QWidget()
    ui = Ui_Test()
    ui.setupUi(Test)
    Test.show()
    sys.exit(app.exec_())

