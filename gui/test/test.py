from PyQt5 import QtCore, QtGui, QtWidgets
from gui.test.TestWidget import Ui_Test


class Test(QtWidgets.QWidget, Ui_Test):
    def __init__(self, parent):
        QtWidgets.QWidget.__init__(self, parent)
        self.setupUi(self)
        self.retranslateUi(self)
