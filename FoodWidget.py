from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import os
import time

class FoodWidget(QWidget):
	def __init__(self, parent):
		super(FoodWidget, self).__init__(parent)
		self.food_name = QLabel(self)
		self.food_name.setAlignment(Qt.AlignCenter)
		self.food_name.setStyleSheet("background-color: rgb(255, 255, 255); border: 2px solid rgb(0, 0, 255); font: 14pt \"HY헤드라인M\";")
		self.restorant_name = QLabel(self)
		self.restorant_name.setAlignment(Qt.AlignCenter)
		self.restorant_name.setStyleSheet("background-color: rgb(255, 255, 255); border: 2px solid rgb(255, 0, 0); font: 14pt \"HY헤드라인M\";")
		self.price = QLabel(self)
		self.price.setAlignment(Qt.AlignCenter)
		self.price.setStyleSheet("color: rgb(0, 128, 100); background-color: rgb(255, 255, 255); border: 2px solid rgb(255, 0, 0); font: 14pt \"HY헤드라인M\";")

		self.is_click = False
		self.count = 0
		self.timer = QTimer(self)
		self.size = 0
		self.food_list = []

	def render(self, food_list):
		self.food_name.setGeometry(0, 0, self.rect().right(), 30)
		self.restorant_name.setGeometry(0, self.rect().bottom()-30, self.rect().right() / 2 , 30)
		self.price.setGeometry(self.rect().right() / 2, self.rect().bottom()-30, self.rect().right() / 2, 30)
		print(self.rect().bottom())
		self.food_list = food_list
		self.size = len(food_list)
		self.timer.timeout.connect(self.callback)
		self.timer.start()

	def callback(self):
		if self.size - 1 > self.count:
			self.is_click = True
			self.update()
			self.count = self.count + 1
			self.timer.start((self.count) ** 1.2 )

	def paintEvent(self, e):
		if self.is_click:
			painter = QPainter(self)
			print(self.size, self.count)

			file_path = "image/" + str(self.food_list[self.count][0]) + ".jpg"
			if os.path.exists(file_path):
				pixmap = QPixmap(file_path)
			else:
				pixmap = QPixmap("image/null.jpg")
			painter.drawPixmap(0, self.rect().top()+30, self.rect().right(), self.rect().bottom()-60, pixmap)
			self.food_name.setText("[ " + self.food_list[self.count][1] + " ]")
			self.restorant_name.setText("[ " + self.food_list[self.count][2] + " ]")
			self.price.setText("[ 가격 : " + format(self.food_list[self.count][3], ',') + "원 ]")
			print('호출!')
			painter.end()
			self.is_click = False
		
		

