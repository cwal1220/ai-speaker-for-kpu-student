from PyQt5 import QtCore, QtGui, QtWidgets
from MainForm import *
from noticeTrd import *


class Main(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        self.notice_trd = NoticeTrd(self)
        self.notice_trd.changed_notice.connect(self.on_or_off_mark)
        self.setupUi(self)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(400, 0, 400, 450))
        self.pushButton_test.clicked.connect(self.onClickTest)
        self.pushButton_notice.clicked.connect(self.onClickNotice)
        self.pushButton_read.clicked.connect(self.onClickRead)
        self.notice_trd.start()
        self.on_or_off_mark()

    def onClickTest(self):
        self.widget.close()
        self.verticalLayout.removeWidget(self.widget)
        self.widget = Test(self.verticalLayoutWidget)
        self.verticalLayout.addWidget(self.widget)

    def onClickNotice(self):
        self.widget.close()
        self.verticalLayout.removeWidget(self.widget)
        self.widget = Notice(self.verticalLayoutWidget)
        self.verticalLayout.addWidget(self.widget)
        self.widget.label_update()

    def onClickRead(self):
        self.on_or_off_mark()

    def on_or_off_mark(self, on=False):
        if on:
            self.label_notice.setPixmap(QtGui.QPixmap("img/notice.png"))
        else:
            self.label_notice.clear()


if __name__ == '__main__':
    import sys

    app = QtWidgets.QApplication(sys.argv)
    instance = Main()
    instance.show()
    sys.exit(app.exec_())
