from PyQt5 import QtCore, QtGui, QtWidgets
from bs4 import BeautifulSoup
from requests import get
from json import loads, dumps
from time import sleep


class NoticeTrd(QtCore.QThread):
    changed_notice = QtCore.pyqtSignal(object)

    def __init__(self, parent=None):
        QtCore.QThread.__init__(self, parent)
        self.enabled = False
        self.url_dict = {
            '학사': 'http://www.kpu.ac.kr/front/boardlist.do?searchField=ALL&searchValue=&currentPage=1&searchLowItem=ALL&bbsConfigFK=1&siteGubun=14&menuGubun=1',
            '취업': 'http://www.kpu.ac.kr/front/boardlist.do?searchField=ALL&searchValue=&currentPage=1&searchLowItem=ALL&bbsConfigFK=339&siteGubun=14&menuGubun=1',
            '일반': 'http://www.kpu.ac.kr/front/boardlist.do?searchField=ALL&searchValue=&currentPage=1&searchLowItem=ALL&bbsConfigFK=357&siteGubun=14&menuGubun=1'
        }
        self.notice_dict = dict()

    def stop(self):
        self.enabled = False

    def run(self):
        self.enabled = True
        try:
            while self.enabled:
                self.get_notice()
                sleep(20)
        except Exception as e:
            print(e)
            self.enabled = False

    def get_html(self, url):
        while True:
            text = get(url)
            if text.status_code is 200:
                break
            else:
                print(url + 'page loading error!')
        return text.text.split('<!-- List 시작 -->')[1].split('</tr>')

    def get_notice(self):
        for x, y in self.url_dict.items():
            self.notice_dict[x] = dict()
            text = self.get_html(y)
            for i in range(3):
                t = BeautifulSoup(text[i], 'html.parser')
                self.notice_dict[x][str(i)] = dict()
                self.notice_dict[x][str(i)]['sub'] = t.find('span', {'class': 'text'}).text.strip()
                tac = t.find_all('td', {'class': 'tac'})
                self.notice_dict[x][str(i)]['num'] = tac[0].text
                self.notice_dict[x][str(i)]['writer'] = tac[1].text.strip()
                self.notice_dict[x][str(i)]['date'] = tac[3].text.strip()
        self.save_file()

    def save_file(self):
        try:
            with open('notice.txt', 'r') as f:
                loaded = loads(f.read())
                changed = False
                for x, y in loaded.items():
                    if y['0'] != self.notice_dict[x]['0']:
                        print('새 %s공지 %s' % (x, self.notice_dict[x]['0']['sub']))
                        changed = True
            if changed:
                self.changed_notice.emit(True)
                raise FileNotFoundError
        except FileNotFoundError:
            print('파일을 새로 저장합니다.')
            with open('notice.txt', 'w') as f:
                f.write(dumps(self.notice_dict))
