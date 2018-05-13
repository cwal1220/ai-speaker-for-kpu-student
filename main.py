# ---------- Made from PyQt5 ----------
from PyQt5 import QtCore, QtGui, QtWidgets
# ---------- MainWindow & Widget ----------
from gui.MainForm import Ui_MainWindow
from gui.notice.notice import Notice
from gui.notice.noticeTrd import NoticeTrd
from gui.food.FoodWidget import FoodWidget
from gui.weather.WeatherWidget import WeatherWidget
from gui.shuttle.ShuttleWidget import ShuttleWidget
# ---------- Modules ----------
import snowboy.snowboydecoder as snowboydecoder
import utils.recorder as recorder
import utils.transcribe_streaming as transcribe_streaming
import weather.weather as weather
import utils.gps as gps
from utils.tts import TTS
from utils.shuttle import Shuttle
from utils.stt import STT
# ---------- pkgs ----------
import threading
from json import loads
import subprocess


class Main(QtWidgets.QMainWindow, Ui_MainWindow):
	def __init__(self):
		QtWidgets.QMainWindow.__init__(self)
		self.notice_trd = NoticeTrd(self)
		self.notice_trd.changed_notice.connect(self.on_or_off_mark)
		self.setupUi(self)
		self.move(-2, 0)
		self.verticalLayoutWidget.setGeometry(QtCore.QRect(400, 0, 400, 450))
		self.pushButton_notice.clicked.connect(self.onClickNotice)
		self.pushButton_food.clicked.connect(self.onClickFood)
		self.pushButton_weather.clicked.connect(self.onClickWeather)
		self.pushButton_shuttle.clicked.connect(self.onClickShuttle)
		self.notice_trd.start()
		self.on_or_off_mark()
		self.lat = 37.340348
		self.lon = 126.6984882
		self.detector = snowboydecoder.HotwordDetector('snowboy/resources/이놈아.pmdl', sensitivity=0.6)
		self.rc = recorder.Recorder()
		self.tts = TTS()
		self.stt = STT()
		self.speaker = 'mijin'
		speech_thread = threading.Thread(target=self.speechRecogStart)
		speech_thread.daemon = True
		speech_thread.start()
		gps_thread = threading.Thread(target=self.gpsStart)
		gps_thread.daemon = True
		gps_thread.start()

	def onClickNotice(self):
		self.on_or_off_mark()
		self.widget.close()
		self.verticalLayout.removeWidget(self.widget)
		self.widget = Notice(self.verticalLayoutWidget)
		self.verticalLayout.addWidget(self.widget)
		self.widget.label_update()

	def onClickFood(self):
		self.widget.close()
		self.verticalLayout.removeWidget(self.widget)
		self.widget = FoodWidget(self.verticalLayoutWidget)
		self.verticalLayout.addWidget(self.widget)
		self.widget.render()

	def onClickWeather(self):
		self.widget.close()
		self.verticalLayout.removeWidget(self.widget)
		self.widget = WeatherWidget(self.verticalLayoutWidget)
		self.widget.render(self.wd)
		self.verticalLayout.addWidget(self.widget)

	def onClickShuttle(self):
		self.widget.close()
		self.verticalLayout.removeWidget(self.widget)
		self.widget = ShuttleWidget(self.verticalLayoutWidget)
		self.widget.render(self.s_list)
		self.verticalLayout.addWidget(self.widget)

	def on_or_off_mark(self, on=False):
		if on:
			self.label_notice.setPixmap(QtGui.QPixmap("gui/notice/image/notice.png"))
		else:
			self.label_notice.clear()

	def setLatLon(self, value):
		self.lat = value[0]
		self.lon = value[1]

	def speechRecogStart(self):
		self.detector.start(detected_callback=self.gg, sleep_time=0.03)

	def gpsStart(self):
		mygps = gps.GPS()
		mygps.on_changed_gps.connect(self.setLatLon)
		mygps.run()

	def gg(self):
		self.detector.terminate()
		snowboydecoder.play_audio_file(snowboydecoder.DETECT_DING)
		# audio_buffer = self.rc.record_audio()
		text = self.stt.get_str(self.label_stt.setText)
		snowboydecoder.play_audio_file(snowboydecoder.DETECT_DONG)

		# text = transcribe_streaming.transcribe_streaming(audio_buffer)

		self.label_stt.setText(text)

		if text is None:
			self.label_tts.setText('...')
			self.detector.start(detected_callback=self.gg, sleep_time=0.03)
			return

		elif "날씨" in text:
			self.wd = weather.get_weather(self.lat, self.lon)
			spch = self.wd['str']
			self.pushButton_weather.click()

		elif "꺼져" in text:
			spch = "꺼지라고요? 말씀이 심하시네요.."

		elif "안녕" in text:
			spch = "반가워요!"

		elif "셔틀" in text:
			shuttle = Shuttle()
			if '정왕역' in text:
				self.s_list = shuttle.get_shuttle('산기대', '정왕역')
			elif '오이도' in text:
				self.s_list = shuttle.get_shuttle('산기대', '오이도')
			elif '학교' in text:
				self.s_list = shuttle.get_shuttle('정왕역', '산기대')
			else:
				spch = '위치를 정확히 말해주세요.'
				self.label_tts.setText(spch)
				self.tts.play_tts(spch, self.speaker)
				self.detector.start(detected_callback=self.gg, sleep_time=0.03)
				return
			if len(self.s_list) == 0:
				spch = "탑승 가능한 셔틀버스가 존재하지 않습니다!"
			else:
				spch = "탑승 가능한 가장 빠른 셔틀은 " + self.s_list[0][2] + "이고 출발까지 " + str(self.s_list[0][3]) + "시간 " + str(
					self.s_list[0][4]) + "분 남았습니다."
			self.pushButton_shuttle.click()

		elif "공지" in text:
			self.pushButton_notice.click()
			if "읽" in text:
				with open('notice.txt', 'r') as f:
					loaded = loads(f.read())
				spch = '학사공지, ' + loaded['학사']['0']['sub'] + ', 취업공지, ' + loaded['취업']['0']['sub'] + ', 일반공지, ' +\
				       loaded['일반']['0']['sub']
			else:
				spch = '공지사항을 보여드릴게요.'

		elif "학식" in text or "메뉴" in text:
			self.pushButton_food.click()
			spch = '메뉴를 추천해드릴게요!'

		elif "유리" in text or '일본' in text:
			self.speaker = 'yuri'
			spch = '저는 한국말을 잘 못해요!'

		elif "미진" in text or '한국' in text:
			self.speaker = 'mijin'
			spch = '저를 찾으셨나요?'

		elif "교수님" in text:
			spch = '교수님, 저희는 A+가 받고 싶습니다!'

		elif "이놈아" in text:
			spch = '저의 이름을 불러주시다니 정말 기쁘네요~'

		elif "아빠" in text and "누구" in text:
			spch = '저는 아빠가 두명이에요~ 헤헤헤...'

		elif "나쁜 놈" in text:
			spch = '으어어어엉.... ㅠㅠ 저 상처받았어요...'

		else:
			spch = '잘 알아듣지 못했습니다? 정확하게 말해 주세요'

		self.label_tts.setText(spch)
		self.tts.play_tts(spch, self.speaker)
		subprocess.Popen(['mpg123', '-q', "snowboy/resources/ring.mp3"]).wait()
		self.detector.start(detected_callback=self.gg, sleep_time=0.03)
		

if __name__ == '__main__':
	import sys

	app = QtWidgets.QApplication(sys.argv)
	instance = Main()
	instance.show()
	sys.exit(app.exec_())
