# coding: utf-8
 
import sys
from PyQt5 import QtWidgets
from PyQt5 import QtGui
from PyQt5 import uic
from PyQt5 import QtCore
from PyQt5.QtCore import pyqtSlot

from hehe import STT
from haha import TTS
import threading
class Form(QtWidgets.QDialog):
	def __init__(self, parent=None):
		QtWidgets.QDialog.__init__(self, parent)
		self.ui = uic.loadUi("untitled.ui", self)
		self.ui.show()
		
		
		

	@pyqtSlot()
	def slot_start(self):
		self.ui.stt.setText("--인식중--")
		self.ui.button_start.setEnabled(False)
		t = threading.Thread(target=self.gg)
		t.daemon = True
		t.start()

	@pyqtSlot()
	def slot_pause(self):
		print("정지?")


	def gg(self):
		self.gsp = STT()
		print("스레드 시작")
		# 음성 인식 될때까지 대기 한다.
		stt = self.gsp.getText()
		# 만약 None이 반환되면
		if stt is None:
			return
		print(stt)
		self.ui.stt.setText(stt)
		tts = TTS()

		if "꺼져" in stt:
			tts.play_tts("뭐라했냐 개새끼야")
			self.ui.button_start.setEnabled(True)
			return

		if "안녕" in stt:
			tts.play_tts("반가워요!!!!!")
			self.ui.button_start.setEnabled(True)
			return
		tts.play_tts(stt)
		self.ui.button_start.setEnabled(True)
if __name__ == '__main__':
	app = QtWidgets.QApplication(sys.argv)
	w = Form()
	sys.exit(app.exec())