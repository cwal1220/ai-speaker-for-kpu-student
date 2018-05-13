from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

import os
import pymysql
import random
import time

class FoodWidget(QWidget):
	def __init__(self, parent):
		super(FoodWidget, self).__init__(parent)
		self.path = os.getcwd()
		self.gridLayout_2 = QGridLayout(self)
		self.gridLayout_2.setObjectName("gridLayout_2")
		self.gridLayout = QGridLayout()
		self.gridLayout.setObjectName("gridLayout")
		self.restorant_name = QLabel(self)
		self.restorant_name.setStyleSheet(" border: 2px solid rgb(255, 0, 0); font: 14pt \"HY헤드라인M\";")
		self.restorant_name.setText("")
		self.restorant_name.setAlignment(Qt.AlignCenter)
		self.restorant_name.setObjectName("restorant_name")
		self.gridLayout.addWidget(self.restorant_name, 7, 0, 1, 1)
		self.image = QLabel(self)
		self.image.setText("")
		self.image.setObjectName("image")
		self.gridLayout.addWidget(self.image, 1, 0, 6, 2)
		self.food_name = QLabel(self)
		self.food_name.setStyleSheet("border: 2px solid rgb(0, 0, 255); font: 14pt \"HY헤드라인M\";")
		self.food_name.setText("")
		self.food_name.setAlignment(Qt.AlignCenter)
		self.food_name.setObjectName("food_name")
		self.gridLayout.addWidget(self.food_name, 0, 0, 1, 2)
		self.price = QLabel(self)
		self.price.setStyleSheet("color: rgb(0, 128, 100);border: 2px solid rgb(255, 0, 0); font: 14pt \"HY헤드라인M\";")
		self.price.setText("")
		self.price.setAlignment(Qt.AlignCenter)
		self.price.setObjectName("price")
		self.gridLayout.addWidget(self.price, 7, 1, 1, 1)
		self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)

		self.is_click = False
		self.count = 0
		self.timer = QTimer(self)
		self.size = 0
		self.food_list = self.get_food_list()


	def get_food_list(self):
		conn = pymysql.connect(host='localhost', user='root', password='root', db='speaker', charset='utf8')
		curs = conn.cursor()
		sql = "select * from foodcourt"
		curs.execute(sql)
		rows = curs.fetchall()
		conn.close()
		rows = random.sample(rows, len(rows))
		return rows

	def render(self):
		self.size = len(self.food_list)
		self.timer.timeout.connect(self.callback)
		self.timer.start()

	def callback(self):
		if self.size - 1 > self.count:
			self.is_click = True
			self.drawer()
			self.count = self.count + 1
			self.timer.start((self.count) ** 1.2 )
		else:
			self.timer.stop()

	def drawer(self):
		if self.is_click:
			file_path = self.path + '/gui/food/image/' + str(self.food_list[self.count][0]) + ".jpg"
			if os.path.exists(file_path):
				self.image.setStyleSheet("image: url({});".format(file_path))
			else:
				self.image.setStyleSheet("image: url(" + self.path + "/gui/food/image/null.jpg);")

			self.food_name.setText("[ " + self.food_list[self.count][1] + " ]")
			self.restorant_name.setText("[ " + self.food_list[self.count][2] + " ]")
			self.price.setText("[ 가격 : " + format(self.food_list[self.count][3], ',') + "원 ]")
			self.is_click = False
