# coding: utf-8
 
import sys
from PyQt5 import QtWidgets
from PyQt5 import QtGui
from PyQt5 import uic
from PyQt5 import QtCore
from PyQt5.QtCore import pyqtSlot

import recorder
import transcribe_streaming

from tts import TTS

from shuttle import Shuttle
import threading
import snowboy.snowboydecoder as snowboydecoder

class Form(QtWidgets.QDialog):
	def __init__(self, parent=None):
		QtWidgets.QDialog.__init__(self, parent)
		self.ui = uic.loadUi("untitled.ui", self)
		self.ui.show()
		self.detector = snowboydecoder.HotwordDetector('snowboy/resources/이놈아.pmdl', sensitivity=0.6)

		self.rc = recorder.Recorder()

		t = threading.Thread(target=self.speechRecogStart)
		t.daemon = True
		t.start()
		
		
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


	def speechRecogStart(self):
		self.detector.start(detected_callback=self.gg , sleep_time=0.03)



	def gg(self):
		snowboydecoder.play_audio_file()
		self.detector.terminate()

		audio_buffer = self.rc.record_audio()
		text = transcribe_streaming.transcribe_streaming(audio_buffer)

		print(text)
		self.ui.stt.setText(text)
		tts = TTS()

		if "꺼져" in text:
			tts.play_tts("뭐라했냐")
			self.detector.start(detected_callback=self.gg , sleep_time=0.03)
			return

		if "안녕" in text:
			tts.play_tts("반가워요!!!!!")
			self.detector.start(detected_callback=self.gg , sleep_time=0.03)
			return

		if "셔틀" in text and '정왕역' in text:
			shuttle = Shuttle()
			s_list = shuttle.get_shuttle('산기대', '정왕역')
			if len(s_list) == 0:
				tts.play_tts("탑승 가능한 셔틀버스가 존재하지 않습니다!!!!!")
			else:
				tts.play_tts("탑승 가능한 가장 빠른 셔틀은 " + s_list[0][2] + "이고 출발까지 " + str(s_list[0][3]) + "시간 " + str(s_list[0][4]) + "분 남았습니다.")
			self.detector.start(detected_callback=self.gg , sleep_time=0.03)
			return

		if "셔틀" in text and '오이도' in text:
			shuttle = Shuttle()
			s_list = shuttle.get_shuttle('산기대', '오이도')
			if len(s_list) == 0:
				tts.play_tts("탑승 가능한 셔틀버스가 존재하지 않습니다!!!!!")
			else:
				tts.play_tts("탑승 가능한 가장 빠른 셔틀은 " + s_list[0][2] + "이고 출발까지 " + str(s_list[0][3]) + "시간 " + str(s_list[0][4]) + "분 남았습니다.")
			self.detector.start(detected_callback=self.gg , sleep_time=0.03)
			return

		if "셔틀" in text and '학교' in text:
			shuttle = Shuttle()
			s_list = shuttle.get_shuttle('정왕역', '산기대')
			if len(s_list) == 0:
				tts.play_tts("탑승 가능한 셔틀버스가 존재하지 않습니다!!!!!")
			else:
				tts.play_tts("탑승 가능한 가장 빠른 셔틀은 " + s_list[0][2] + "이고 출발까지 " + str(s_list[0][3]) + "시간 " + str(s_list[0][4]) + "분 남았습니다.")
			self.detector.start(detected_callback=self.gg , sleep_time=0.03)
			return



		tts.play_tts(text)
		self.detector.start(detected_callback=self.gg , sleep_time=0.03)
		
if __name__ == '__main__':
	import os
	os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "/home/pi/MyMic-b737a86ac104.json"
	app = QtWidgets.QApplication(sys.argv)
	w = Form()
	sys.exit(app.exec())