from PyQt5 import QtCore, QtGui, QtWidgets
from NoticeWidget import Ui_Notice
from json import loads


class Notice(QtWidgets.QWidget, Ui_Notice):
    def __init__(self, parent):
        QtWidgets.QWidget.__init__(self, parent)
        self.setupUi(self)
        self.retranslateUi(self)

    def label_update(self):
        with open('notice.txt', 'r') as f:
            dic = loads(f.read())
        # self.label_haksa1.setText('(%s) %s' % (dic['학사']['num'], dic['학사']['sub']))
        self.label_haksa_sub1.setText(self.too_long(dic['학사']['0']['sub']))
        self.label_haksa_sub2.setText(self.too_long(dic['학사']['1']['sub']))
        self.label_haksa_sub3.setText(self.too_long(dic['학사']['2']['sub']))
        self.label_job_sub1.setText(self.too_long(dic['취업']['0']['sub']))
        self.label_job_sub2.setText(self.too_long(dic['취업']['1']['sub']))
        self.label_job_sub3.setText(self.too_long(dic['취업']['2']['sub']))
        self.label_general_sub1.setText(self.too_long(dic['일반']['0']['sub']))
        self.label_general_sub2.setText(self.too_long(dic['일반']['1']['sub']))
        self.label_general_sub3.setText(self.too_long(dic['일반']['2']['sub']))
        self.label_haksa_num1.setText('- 번호 ' + dic['학사']['0']['num'])
        self.label_haksa_num2.setText('- 번호 ' + dic['학사']['1']['num'])
        self.label_haksa_num3.setText('- 번호 ' + dic['학사']['2']['num'])
        self.label_job_num1.setText('- 번호 ' + dic['취업']['0']['num'])
        self.label_job_num2.setText('- 번호 ' + dic['취업']['1']['num'])
        self.label_job_num3.setText('- 번호 ' + dic['취업']['2']['num'])
        self.label_general_num1.setText('- 번호 ' + dic['일반']['0']['num'])
        self.label_general_num2.setText('- 번호 ' + dic['일반']['1']['num'])
        self.label_general_num3.setText('- 번호 ' + dic['일반']['2']['num'])
        self.label_haksa_date1.setText('날짜 ' + dic['학사']['0']['date'])
        self.label_haksa_date2.setText('날짜 ' + dic['학사']['1']['date'])
        self.label_haksa_date3.setText('날짜 ' + dic['학사']['2']['date'])
        self.label_job_date1.setText('날짜 ' + dic['취업']['0']['date'])
        self.label_job_date2.setText('날짜 ' + dic['취업']['1']['date'])
        self.label_job_date3.setText('날짜 ' + dic['취업']['2']['date'])
        self.label_general_date1.setText('날짜 ' + dic['일반']['0']['date'])
        self.label_general_date2.setText('날짜 ' + dic['일반']['1']['date'])
        self.label_general_date3.setText('날짜 ' + dic['일반']['2']['date'])
        self.label_haksa_writer1.setText('작성자 ' + dic['학사']['0']['writer'])
        self.label_haksa_writer2.setText('작성자 ' + dic['학사']['1']['writer'])
        self.label_haksa_writer3.setText('작성자 ' + dic['학사']['2']['writer'])
        self.label_job_writer1.setText('작성자 ' + dic['취업']['0']['writer'])
        self.label_job_writer2.setText('작성자 ' + dic['취업']['1']['writer'])
        self.label_job_writer3.setText('작성자 ' + dic['취업']['2']['writer'])
        self.label_general_writer1.setText('작성자 ' + dic['일반']['0']['writer'])
        self.label_general_writer2.setText('작성자 ' + dic['일반']['1']['writer'])
        self.label_general_writer3.setText('작성자 ' + dic['일반']['2']['writer'])

    def too_long(self, string):
        if len(string) > 34:
            string = string[:34] + '...'
        return string
