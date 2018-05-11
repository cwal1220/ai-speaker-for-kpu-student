from bs4 import BeautifulSoup
from requests import get
from json import loads, dumps


class Notice:
    def __init__(self):
        self.url_dict = {
            '학사': 'http://www.kpu.ac.kr/front/boardlist.do?searchField=ALL&searchValue=&currentPage=1&searchLowItem=ALL&bbsConfigFK=1&siteGubun=14&menuGubun=1',
            '장학': 'http://www.kpu.ac.kr/front/boardlist.do?searchField=ALL&searchValue=&currentPage=1&searchLowItem=ALL&bbsConfigFK=494&siteGubun=14&menuGubun=1',
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
        return BeautifulSoup(text.text.split('<!-- List 시작 -->')[1], 'html.parser')

    def get_notice(self):
        for x, y in self.url_dict.items():
            self.notice_dict[x] = dict()
            text = self.get_html(y)
            num = text.find('td', {'class': 'tac'}).text.strip().splitlines()[0]
            sub = text.find('span', {'class': 'text'}).text.strip().splitlines()[0]
            self.notice_dict[x]['num'] = num
            self.notice_dict[x]['sub'] = sub

    def save_file(self):
        try:
            with open('notice.txt', 'r') as f:
                loaded = loads(f.read())
                changed = False
                for x, y in loaded.items():
                    if y != self.notice_dict[x]:
                        print('새 %s공지 (%s) %s' % (x, y['num'], y['sub']))
                        changed = True
            if changed:
                raise FileNotFoundError
        except FileNotFoundError:
            print('파일을 새로 저장합니다.')
            with open('notice.txt', 'w') as f:
                f.write(dumps(self.notice_dict))


if __name__ == '__main__':
    nt = Notice()
    nt.get_notice()
    nt.save_file()
