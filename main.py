from PyQt5 import QtCore, QtGui, QtWidgets
from gui.MainForm import *
from gui.notice.notice import Notice
from gui.notice.noticeTrd import *
from json import loads

import recorder
import transcribe_streaming

from tts import TTS

from shuttle import Shuttle
import threading
import snowboy.snowboydecoder as snowboydecoder
import weather.weather as weather
import gps


class Main(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        self.notice_trd = NoticeTrd(self)
        self.notice_trd.changed_notice.connect(self.on_or_off_mark)
        self.setupUi(self)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(400, 0, 400, 450))
        self.pushButton_test.clicked.connect(self.onClickTest)
        self.pushButton_notice.clicked.connect(self.onClickNotice)
        self.notice_trd.start()
        self.on_or_off_mark()
        self.pushButton_test.setVisible(False)
        self.pushButton_notice.setVisible(False)
        self.lat = 37.340348
        self.lon = 126.6984882
        self.detector = snowboydecoder.HotwordDetector('snowboy/resources/이놈아.pmdl', sensitivity=0.6)
        self.rc = recorder.Recorder()
        self.tts = TTS()
        speech_thread = threading.Thread(target=self.speechRecogStart)
        speech_thread.daemon = True
        speech_thread.start()
        gps_thread = threading.Thread(target=self.gpsStart)
        gps_thread.daemon = True
        gps_thread.start()

    def onClickTest(self):
        self.widget.close()
        self.verticalLayout.removeWidget(self.widget)
        self.widget = Test(self.verticalLayoutWidget)
        self.verticalLayout.addWidget(self.widget)

    def onClickNotice(self):
        self.on_or_off_mark()
        self.widget.close()
        self.verticalLayout.removeWidget(self.widget)
        self.widget = Notice(self.verticalLayoutWidget)
        self.verticalLayout.addWidget(self.widget)
        self.widget.label_update()

    def on_or_off_mark(self, on=False):
        if on:
            self.label_notice.setPixmap(QtGui.QPixmap("image/notice.png"))
        else:
            self.label_notice.clear()

    def setLatLon(self, value):
        self.lat = value[0]
        self.lon = value[1]

    def speechRecogStart(self):
        self.detector.start(detected_callback=self.gg , sleep_time=0.03)

    def gpsStart(self):
        mygps = gps.GPS()
        mygps.on_changed_gps.connect(self.setLatLon)
        mygps.run()

    def gg(self):
        print('listening...')
        self.detector.terminate()
        snowboydecoder.play_audio_file(snowboydecoder.DETECT_DING)
        audio_buffer = self.rc.record_audio()
        snowboydecoder.play_audio_file(snowboydecoder.DETECT_DONG)

        text = transcribe_streaming.transcribe_streaming(audio_buffer)

        self.label_stt.setText(text)

        

        if text is None:
            self.label_tts.setText('...')
            self.detector.start(detected_callback=self.gg , sleep_time=0.03)
            return

        elif "날씨" in text:
        	spch = weather.get_weather(self.lat, self.lon)

        elif "꺼져" in text:
            spch = "뭐라했냐"

        elif "안녕" in text:
            spch = "반가워요!!!!!"

        elif "셔틀" in text and '정왕역' in text:
            shuttle = Shuttle()
            s_list = shuttle.get_shuttle('산기대', '정왕역')
            if len(s_list) == 0:
                spch = "탑승 가능한 셔틀버스가 존재하지 않습니다!!!!!"
            else:
                spch = "탑승 가능한 가장 빠른 셔틀은 " + s_list[0][2] + "이고 출발까지 " + str(s_list[0][3]) + "시간 " + str(s_list[0][4]) + "분 남았습니다."

        elif "셔틀" in text and '오이도' in text:
            shuttle = Shuttle()
            s_list = shuttle.get_shuttle('산기대', '오이도')
            if len(s_list) == 0:
                spch = "탑승 가능한 셔틀버스가 존재하지 않습니다!!!!!"
            else:
                spch = "탑승 가능한 가장 빠른 셔틀은 " + s_list[0][2] + "이고 출발까지 " + str(s_list[0][3]) + "시간 " + str(s_list[0][4]) + "분 남았습니다."

        elif "셔틀" in text and '학교' in text:
            shuttle = Shuttle()
            s_list = shuttle.get_shuttle('정왕역', '산기대')
            if len(s_list) == 0:
                spch = "탑승 가능한 셔틀버스가 존재하지 않습니다!!!!!"
            else:
                spch = "탑승 가능한 가장 빠른 셔틀은 " + s_list[0][2] + "이고 출발까지 " + str(s_list[0][3]) + "시간 " + str(s_list[0][4]) + "분 남았습니다."

        elif "공지" in text:
            self.pushButton_notice.click()
            if "읽" in text:
                with open('notice.txt', 'r') as f:
                    loaded = loads(f.read())
                spch = '학사공지, ' + loaded['학사']['0']['sub'] + ', 취업공지, ' + loaded['취업']['0']['sub'] + ', 일반공지, ' + loaded['일반']['0']['sub']
            else:
            	spch = '공지사항을 보여드릴게요.'

        elif "메인" in text:
        	self.pushButton_test.click()
        	spch = '메인으로 돌아왔어요'

        else:
            spch = '잘 알아듣지 못했습니다? 똑바로 말해라?'

        self.label_tts.setText(spch)
        self.tts.play_tts(spch)
        self.detector.start(detected_callback=self.gg , sleep_time=0.03)

if __name__ == '__main__':
    import sys

    app = QtWidgets.QApplication(sys.argv)
    instance = Main()
    instance.show()
    sys.exit(app.exec_())
