from bs4 import BeautifulSoup
from requests import get
from json import loads, dumps
from time import sleep


class NoticeTrd:
    def __init__(self):
        self.url_dict = {
            '학사': 'http://www.kpu.ac.kr/front/boardlist.do?searchField=ALL&searchValue=&currentPage=1&searchLowItem=ALL&bbsConfigFK=1&siteGubun=14&menuGubun=1',
            '취업': 'http://www.kpu.ac.kr/front/boardlist.do?searchField=ALL&searchValue=&currentPage=1&searchLowItem=ALL&bbsConfigFK=339&siteGubun=14&menuGubun=1',
            '일반': 'http://www.kpu.ac.kr/front/boardlist.do?searchField=ALL&searchValue=&currentPage=1&searchLowItem=ALL&bbsConfigFK=357&siteGubun=14&menuGubun=1'
        }
        self.notice_dict = dict()

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


if __name__ == '__main__':
    obj = NoticeTrd()
    obj.get_notice()
    print(obj.notice_dict)
