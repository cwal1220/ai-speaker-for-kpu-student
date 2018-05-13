# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'doraemon.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.widget = FoodWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(20, 20, 361, 421))
        self.widget.setObjectName("widget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(470, 250, 75, 23))
        self.pushButton.setObjectName("pushButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.pushButton.clicked.connect(self.hehe)
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "PushButton"))

    def hehe(self):
        self.widget.render([(6, '김치찌개돈까스', 'U9', 4500), (135, '초계비빔국수', '한스델리', 3500), (54, '비빔냉면', '김밥천국', 3500), (42, '탕수육볶음밥', '손쉐프', 5000), (108, '비빔모밀', 'U9', 3500), (65, '탕짜면', '손쉐프', 4500), (53, '라볶이', '김밥천국', 2500), (12, '김치알돌솥밥', 'U9', 4000), (105, '고구마치즈돈까스', 'U9', 4500), (46, '짬짜면', '손쉐프', 3500), (40, '쉐프치킨덮밥', '손쉐프', 4500), (90, '매운참치비빔밥', '한스델리', 3500), (61, '치즈불고기볶음밥', '김밥천국', 4500), (22, '돈도리볶음밥', '한스델리', 3500), (77, '우동', '손쉐프', 3000), (16, '갈릭함박스테이크오믈렛', '한스델리', 4000), (56, '돼지주물럭', '김밥천국', 4000), (1, '등심돈까스', 'U9', 4000), (141, '왕난자완스덮밥', '손쉐프', 4500), (41, '폭찹스테이크덮밥', '손쉐프', 4000), (30, '고기국수', '한스델리', 4000), (145, '매콤소금구이덮밥', '한스델리', 3500), (14, '냉모밀', 'U9', 3500), (51, '라면', '김밥천국', 2000), (18, '데리야끼치킨덮밥', '한스델리', 3500), (11, '치즈돈까스', 'U9', 4000), (55, '물냉면', '김밥천국', 3500), (157, '순두부찌개', '김밥천국', 3500), (97, 'U9우동+주먹밥', 'U9', 3500), (99, '다꼬야끼치킨덮밥', 'U9', 4000), (75, '궁보찜닭', '손쉐프', 4000), (161, '커리미야자키치킨덮밥', 'U9', 4500), (151, '소금구이덮밥', '한스델리', 3500), (50, '참치김밥', '김밥천국', 2000), (36, '탕수육', '손쉐프', 10000), (63, '목살스테이크덮밥', '김밥천국', 4500), (488, '참치김치만두찌개', '김밥천국', 4000), (87, '소고기쌀국수', '손쉐프', 4000), (64, '떡만두라면', '김밥천국', 3000), (165, '콩나물불고기덮밥', 'U9', 4000), (578, '닭갈비덮밥', '김밥천국', 3500), (124, '모듬수제비', '한스델리', 4000), (131, '냉쫄면', '김밥천국', 3500), (115, '제육장비빔밥', '한스델리', 3500), (70, '달달불고기도시락', 'U9', 4500), (24, '불닭오믈렛', '한스델리', 4000), (20, '우삼겹숙주덮밥', '한스델리', 4000), (8, '갈릭양파돈까스', 'U9', 4500), (58, '치즈베이컨김치볶음밥', '김밥천국', 4000), (44, '매콤치킨커리', '김밥천국', 4000), (15, '참치회덮밥', 'U9', 3500), (23, '해물미트스파게티', '한스델리', 4500), (38, '쉐프치킨세트', '손쉐프', 5000), (31, '짬뽕', '손쉐프', 3000), (32, '짜장면', '손쉐프', 2500), (47, '야채김밥', '김밥천국', 1500), (160, '철판참치김치덮밥', '김밥천국', 3500), (177, '카오팟무', '한스델리', 3500), (477, '모듬떡볶이', '김밥천국', 3500), (19, '간장닭갈비잡채덮밥', '한스델리', 4000), (66, '탕짬면', '손쉐프', 4500), (13, '양푼이비빔밥', 'U9', 3500), (95, '부타동', 'U9', 4000), (84, '철판주먹밥?', '손쉐프', 4500), (60, '파채돈까스', 'U9', 4500), (5, '돈카츠벤또', 'U9', 4000), (85, '모둠컵밥', 'U9', 3000), (43, '콩국수', '손쉐프', 4000), (123, '불닭치즈도리아', '한스델리', 4000), (500, '돌솥제육덮밥', '김밥천국', 4000), (4, '해물야끼우동', 'U9', 4500), (579, '철판쭈꾸미삼겹덮밥', '김밥천국', 4000), (35, '깐풍기', '손쉐프', 10000), (49, '참치비빔밥', '김밥천국', 3500), (82, '소고기필라프', '한스델리', 4000), (121, '뚝날치알밥', '손쉐프', 4000), (45, '빨간당면', '손쉐프', 4000), (34, '볶음밥+짜장', '손쉐프', 4000), (39, '크림짬뽕', '손쉐프', 4000), (153, '초계막국수', '한스델리', 3500), (158, '돌솥닭갈비', '김밥천국', 4000), (148, '양념감자오믈렛', '한스델리', 3500), (134, '카레제육덮밥', '김밥천국', 3500), (26, '치킨볼오믈렛', '한스델리', 4000), (2, '소고기덮밥', 'U9', 3000), (111, '우불덮밥', 'U9', 4000), (21, '치즈오븐치킨라이스', '한스델리', 4000), (140, '대패삼겹덮밥', '손쉐프', 4000), (37, '탕수육세트', '손쉐프', 5000), (28, '삼겹살강된장비빔밥', '한스델리', 4000)]
)


from FoodWidget import FoodWidget

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

