# coding: utf-8
 
import sys
from PyQt5 import QtWidgets
from PyQt5 import QtGui
from PyQt5 import uic
from PyQt5 import QtCore
from PyQt5.QtCore import pyqtSlot

from stt import STT
from tts import TTS
from shuttle import Shuttle
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
			tts.play_tts("뭐라했냐")
			self.ui.button_start.setEnabled(True)
			return

		if "안녕" in stt:
			tts.play_tts("반가워요!!!!!")
			self.ui.button_start.setEnabled(True)
			return

		if "셔틀" in stt and '정왕역' in stt:
			shuttle = Shuttle()
			s_list = shuttle.get_shuttle('산기대', '정왕역')
			if len(s_list) == 0:
				tts.play_tts("탑승 가능한 셔틀버스가 존재하지 않습니다!!!!!")
			else:
				tts.play_tts("탑승 가능한 가장 빠른 셔틀은 " + s_list[0][2] + "이고 출발까지 " + str(s_list[0][3]) + "시간 " + str(s_list[0][4]) + "분 남았습니다.")
			self.ui.button_start.setEnabled(True)
			return

		if "셔틀" in stt and '오이도' in stt:
			shuttle = Shuttle()
			s_list = shuttle.get_shuttle('산기대', '오이도')
			if len(s_list) == 0:
				tts.play_tts("탑승 가능한 셔틀버스가 존재하지 않습니다!!!!!")
			else:
				tts.play_tts("탑승 가능한 가장 빠른 셔틀은 " + s_list[0][2] + "이고 출발까지 " + str(s_list[0][3]) + "시간 " + str(s_list[0][4]) + "분 남았습니다.")
			self.ui.button_start.setEnabled(True)
			return

		if "셔틀" in stt and '학교' in stt:
			shuttle = Shuttle()
			s_list = shuttle.get_shuttle('정왕역', '산기대')
			if len(s_list) == 0:
				tts.play_tts("탑승 가능한 셔틀버스가 존재하지 않습니다!!!!!")
			else:
				tts.play_tts("탑승 가능한 가장 빠른 셔틀은 " + s_list[0][2] + "이고 출발까지 " + str(s_list[0][3]) + "시간 " + str(s_list[0][4]) + "분 남았습니다.")
			self.ui.button_start.setEnabled(True)
			return



		tts.play_tts(stt)
		self.ui.button_start.setEnabled(True)
		
if __name__ == '__main__':
	import os
	os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "/home/pi/MyMic-b737a86ac104.json"
	app = QtWidgets.QApplication(sys.argv)
	w = Form()
	sys.exit(app.exec())