from PyQt5 import QtCore, QtGui, QtWidgets
from gui.mainwidget.MainWidget import Ui_MainWidget


class MainWidget(QtWidgets.QWidget, Ui_MainWidget):
	def __init__(self, parent):
		QtWidgets.QWidget.__init__(self, parent)
		self.setupUi(self)